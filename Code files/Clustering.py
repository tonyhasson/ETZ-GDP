from imports import *

# Continents and their respective number
dict = {
    0: "Asia",
    1: "Europe",
    5: "Oceania",
    6: "Africa",
    2: "Central America",
    3: "North America",
    4: "South America",
}

# Columns to be removed from the dataframe
REMOVE_COLUMN = ["Continent", "Least Developed Country", "Third World"]

df = pd.read_csv(FULL_DB_PATH)
df_scrape = pd.read_csv(SCRAP_DB_PATH)
Country_list = df["Country"].tolist()

df_temp = df.drop(REMOVE_COLUMN, axis=1)
df_total = df_temp[(df_temp["Country"] == Country_list) & (df["Year"] >= 2009)].merge(
    df_scrape, on=["Country", "Year"]
)
df_total.to_csv(r"../CSV files/df_total.csv", index=False)


def get_best_num_of_clusters_for_k_means(
    dataset, num_cluster_options, init_val="k-means++", n_init_val=10, rand_state=None
):
    """Check and return the best number of clusters for k-means clustering

    Args:
        dataset (DataFrame): Dataframe with all our data.
        num_cluster_options (list): List of number of clusters to test.
        init_val (str): Initialization method to test.
        n_init_val (int): Number of times to run the algorithm.
        rand_state

    Returns:
        score(float): number of clusters
    """
    best_score = float("-inf")
    for k in num_cluster_options:
        model, pred = perform_k_means(dataset, k, init_val, n_init_val, rand_state)
        if best_score < silhouette_score(dataset, pred):
            best_score = silhouette_score(dataset, pred)
            num_clusters = k

    return best_score, num_clusters


def perform_k_means(
    dataset, num_clusters, init_val="k-means++", n_init_val=10, rand_state=None
):
    """Perform k-means clustering

    Args:
        dataset (DataFrame): Dataframe with all our data.
        num_cluster_options (int): Number of clusters to test.
        init_val (str): Initialization method to test.
        n_init_val (int): Number of times to run the algorithm.
        rand_state - Tony please fil (str): name of the

    Returns:
        model, predicted_vals
    """
    model = KMeans(
        n_clusters=num_clusters,
        init=init_val,
        n_init=n_init_val,
        random_state=rand_state,
    )
    kmeans = model.fit_predict(dataset)
    # dataset["Cluster"] = kmeans.labels_
    return model, kmeans


def perform_density_based_clustering(dataset, epsilon_val=0.5, minimum_samples_val=5):
    """Perform DBScan clustering

    Args:
        dataset (DataFrame): Dataframe with all our data.
        epsilon_val (float): Epsilon value to test.
        minimum_samples_val (int): Minimum samples value to test.

    Returns:
        model, predicted_vals
    """
    model = DBSCAN(eps=epsilon_val, min_samples=minimum_samples_val)

    predicted_vals = model.fit_predict(dataset)

    return model, predicted_vals


def get_best_params_for_dbscan(dataset, eps_options, min_samples_options):
    """Check and return the best number of clusters for DBScan clustering

    Args:
        dataset (DataFrame): Dataframe with all our data.
        eps_options (list): List of epsilon values to test.
        min_samples_options (list): List of minimum samples values to test.

    Returns:
        model, predicted_vals
    """
    best_score = float("-inf")
    for eps in eps_options:
        for min_samples in min_samples_options:
            model, pred = perform_density_based_clustering(dataset, eps, min_samples)
            try:
                if best_score < silhouette_score(dataset, pred):
                    # print("success -> eps:%f min_samp:%f"%(eps,min_samples))
                    best_score = silhouette_score(dataset, pred)
                    best_eps = eps
                    best_min_samples = min_samples
            except Exception as e:
                pass
                # print("fail ->  eps:%f min_samp:%f"%(eps,min_samples))

    return best_score, best_eps, best_min_samples


def Cluster_Graphs(name):
    """Create Graphs for the clustering results

    Args:
        name (str): Name of the DB

    Returns:
        [None] - creates graphs
    """
    """Columns to check correlation on, for each database, maybe add function to take high correlation columns"""
    columnsFULL = [
        ["Population Total", "GDP Total"],
        ["Population Total", "Life expectancy at birth"],
        ["Education Ranking", "GDP Total"],
        ["Total consumption ($)", "GDP Total"],
        ["Military Spendings ($)", "GDP Total"],
        ["Government expenditure (% of GDP)", "Education Ranking"],
    ]
    columnsSCRAP = [
        ["Cost of Living Index", "Affordability Index"],
    ]

    # Assign the correct database to the correct columns
    if name == "full":
        data = pd.read_csv(FULL_DB_PATH)
        columns = columnsFULL
    elif name == "scrape":
        data = pd.read_csv(SCRAP_DB_PATH)
        columns = columnsSCRAP

    # Main For loop
    for column in columns:
        ## KMeans clustering ##
        # Prepare the data to cluster
        data = data[data["Year"] == 2020]
        data1 = data[column].copy()

        # Get the best number of clusters for k-means
        score, num_clusters = get_best_num_of_clusters_for_k_means(
            data1.loc[:, data1.columns != "Continent"],
            [
                4,
                5,
                6,
                7,
                8,
                9,
                10,
            ],
            "k-means++",
            15,
            5,
        )

        # Perform k-means clustering
        model, datanew = perform_k_means(data1[column], num_clusters)
        # Add the cluster column to the dataframe
        data1["Cluster"] = datanew

        fig, axes = plt.subplots(1, 2, figsize=(20, 5))
        fig.suptitle("k_means")
        axes[0].set_title(
            "World Clusters -  num_clusters:"
            + str(num_clusters)
            + "- score:"
            + str(score)
        )
        axes[0].scatter(
            data1[column[0]], data1[column[1]], c=data1["Cluster"], s=50, cmap="plasma"
        )
        axes[0].set_xlabel(column[0])
        axes[0].set_ylabel(column[1])
        axes[1].set_title("World Continents")

        # Create the Continents graph
        for con in data["Continent"].unique():
            axes[1].scatter(
                data1[data["Continent"] == con][column[0]],
                data1[data["Continent"] == con][column[1]],
                label=con,
                cmap="plasma",
            )
        axes[1].legend()

        plt.show()

        ## DBscan clustering ##
        # Prepare the data to cluster
        data = data[data["Year"] == 2020]
        data1 = data[column].copy()

        try:
            # Get the best number of clusters for DBSCAN
            best_score, best_eps, best_min_samples = get_best_params_for_dbscan(
                data1.loc[:, data1.columns != "Continent"],
                [d for d in np.arange(0.1, 10, 0.1)],
                [2, 3, 4, 5, 6, 7, 8, 9, 10],
            )

            # Perform DBSCAN
            model, DBSCANData = perform_density_based_clustering(
                data1.loc[:, data1.columns != "Continent"], best_eps, best_min_samples
            )

            # Add the cluster column to the dataframe
            data1["Cluster"] = DBSCANData

            fig, axes = plt.subplots(1, 2, figsize=(20, 5))
            fig.suptitle("DBSCAN")
            axes[0].set_title(
                "World Clusters -  epsilon"
                + str(best_eps)
                + "- score:"
                + str(best_score)
            )
            axes[0].scatter(
                data1[column[0]],
                data1[column[1]],
                c=data1["Cluster"],
                s=50,
                cmap="plasma",
            )
            axes[0].set_xlabel(column[0])
            axes[0].set_ylabel(column[1])
            axes[1].set_title("World Continents")

            # Create the Continents graph
            for con in data["Continent"].unique():
                axes[1].scatter(
                    data1[data["Continent"] == con][column[0]],
                    data1[data["Continent"] == con][column[1]],
                    label=con,
                    cmap="plasma",
                )
            axes[1].legend()

            plt.show()
        except:
            pass


def PCA_Total_graph(data, num_components):
    """Convert the data to PCA

    Args:
        data (pandas.DataFrame): The data to convert
        num_components (int): Number of components to keep
    Returns:
        data (pandas.DataFrame): The data after the PCA
    """
    # Data Preparation
    data = data[data["Year"] == 2020]
    dataPCA = data.copy()
    features = list(data.columns)

    for column in ["Country", "Year"]:
        features.remove(column)

    # PCA-ing
    dataPCA = dataPCA.loc[:, features].values
    dataPCA = StandardScaler().fit_transform(dataPCA)
    pca = PCA(n_components=num_components)  # num_components-dimensional PCA
    principalComponents = pca.fit_transform(dataPCA)

    ## Plot the PCA(for testing purposes)
    # fig = plt.figure(figsize=(8, 8))
    # ax = fig.add_subplot(1, 1, 1)
    # ax.set_xlabel("Principal Component 1", fontsize=15)
    # ax.set_ylabel("Principal Component 2", fontsize=15)
    # ax.set_title("2 component PCA", fontsize=20)
    # plt.scatter(dataPCA[:,0], dataPCA[:,1],  cmap="plasma")
    # plt.show()

    data.insert(len(data.columns), "principal component 1", principalComponents[:, 0])
    if num_components == 2:
        data.insert(
            len(data.columns), "principal component 2", principalComponents[:, 1]
        )

    return data


def PCA_Cluster_Graph():
    """Perform Clustering on PCA data

    Args:
        None
    Returns:
        data (pandas.DataFrame): The data after the PCA
    """
    for data, name in zip([df, df_scrape, df_total], ("df", "df_scrape", "df_total")):
        data = PCA_Total_graph(data, 2)
        score, num_clusters = get_best_num_of_clusters_for_k_means(
            data[["principal component 1", "principal component 2"]],
            [
                4,
                5,
                6,
                7,
                8,
                9,
                10,
            ],
            "k-means++",
            15,
            5,
        )

        best_score, best_eps, best_min_samples = get_best_params_for_dbscan(
            data[["principal component 1", "principal component 2"]],
            [d for d in np.arange(0.05, 1, 0.01)],
            [2, 3, 4, 5, 6, 7, 8, 9, 10],
        )
        model, KmeansData = perform_k_means(
            data[["principal component 1", "principal component 2"]], num_clusters
        )
        model, DBSCANData = perform_density_based_clustering(
            data[["principal component 1", "principal component 2"]],
            best_eps,
            best_min_samples,
        )

        # Add the cluster column to the dataframe
        data.insert(len(data.columns), "kmean-cluster", KmeansData)
        data.insert(len(data.columns), "dbscan-cluster", DBSCANData)

        print("Now Printing the Graphs for " + name)
        a1, a2 = create_cluster_list(data)

        # for i, cluster in enumerate(data["kmean-cluster"].unique()):
        #     print(cluster)
        #     print(a1[i])
        # Kmean scatter plot
        ComparePlot(data, num_clusters, score, "kmean-cluster", name)

        # for i, cluster in enumerate(data["dbscan-cluster"].unique()):
        #     print(cluster)
        #     print(a2[i])
        # DBScan scatter plot
        ComparePlot(data, best_eps, best_score, "dbscan-cluster", name)

    # return data


def ComparePlot(data, num_clusters, score, label, name):
    """Function to compare 2 different labels for world clustering.

    Args:
        data (dataframe): Dataframe with all our data.
        num_clusters (int): Number of clusters used to cluster with.
        score (float): The score for each cluster.
        label (string): The target label used to cluster with.
        name (string): The name of the dataframe.

    Returns:
        None
    """
    fig, axes = plt.subplots(1, 2, figsize=(20, 5))
    fig.suptitle(name + "\n " + label, fontsize=20)
    if label == "kmean-cluster":
        axes[0].set_title("Clusters:" + str(num_clusters) + ", Score: " + str(score))
    else:
        axes[0].set_title("Eps:" + str(num_clusters) + ", Score:" + str(score))

    for cluster in data[label].unique():
        axes[0].scatter(
            data[data[label] == cluster]["principal component 1"],
            data[data[label] == cluster]["principal component 2"],
            label=cluster,
            # c=data[label],
            s=50,
            cmap="plasma",
        )
    axes[0].legend()

    axes[1].set_title("World Continents")
    for con in data["Continent"].unique():
        axes[1].scatter(
            data[data["Continent"] == con]["principal component 1"],
            data[data["Continent"] == con]["principal component 2"],
            label=dict[con],
            cmap="plasma",
        )
    axes[1].legend()

    plt.show()


# Send DataFrame here and max amount of neighbors to find best epsilon for DBscan
def best_epsilon(FULL_data, col, max_neighbors):
    """Find the best epsilon in giving data for the given column

    Args:
        FULL_data (DataFrame): Dataframe with all our data.
        col (string): The target label used to cluster with.
        max_neighbors (int): max value of neighbors to find epsilon for.
    """
    data = FULL_data.copy()
    # for col in REMOVE_COLUMN:
    #     data = data.drop(col)

    for n in range(2, max_neighbors + 1):
        neigh = NearestNeighbors(n_neighbors=n)
        nbrs = neigh.fit(data)
        distances, indices = nbrs.kneighbors(data)

        distances = np.sort(distances, axis=0)
        distances = distances[:, 1]
        plt.plot(distances)
        plt.title("n_neighbors :%d , %s" % (n, col))
        plt.show()


def find_best_epsilon(name):
    """Create Graphs for the clustering results

    Args:
        name (string): The name of the dataset.

    Returns:
        [None] - creates graphs
    """
    # Columns to check correlation on, for each database, maybe add function to take high correlation columns
    columnsFULL = [
        ["Population Total", "GDP Total"],
        ["Population Total", "Life expectancy at birth"],
        ["Education Ranking", "GDP Total"],
        ["Total consumption ($)", "GDP Total"],
        ["Military Spendings ($)", "GDP Total"],
        ["Government expenditure (% of GDP)", "Education Ranking"],
    ]
    columnsSCRAP = [
        ["Cost of Living Index", "Affordability Index"],
    ]

    # Assign the correct database to the correct columns
    if name == "full":
        data = pd.read_csv(FULL_DB_PATH)
        columns = columnsFULL
    elif name == "scrape":
        data = pd.read_csv(SCRAP_DB_PATH)
        columns = columnsSCRAP

    # Main For loop
    for column in columns:
        # Prepare the data to cluster
        data = data[data["Year"] == 2020]
        data1 = data[column].copy()

        best_epsilon(data1, column, 10)


def create_cluster_list(data):
    """Create a list of clusters for the given dataframe

    Args:
        data (DataFrame): Dataframe with all our data.

    Returns:
        arr1, arr2 (list): List of clusters for each model.
    """

    arr1 = []
    arr2 = []
    for cluster_num in data["kmean-cluster"].unique():
        arr1.append(data[data["kmean-cluster"] == cluster_num]["Country"].unique())

    for cluster_num in data["dbscan-cluster"].unique():
        arr2.append(data[data["dbscan-cluster"] == cluster_num]["Country"].unique())

    print("kmean-cluster")
    pie_plot_cluster_list(data, arr1, "kmean-cluster")
    print("dbscan-cluster")
    pie_plot_cluster_list(data, arr2, "dbscan-cluster")
    return arr1, arr2


def pie_plot_cluster_list(df, arr, label):
    """Create a pie plot for the given list of clusters

    Args:
            df (DataFrame): Dataframe with all our data.
            arr (list): List of clusters for each model.
            label (string): The label of the cluster.

    Returns:
            None - creates a pie plot
    """
    fig, ax = plt.subplots(2, 2, figsize=(20, 5))

    k = 0
    for i in range(2):
        for j in range(2):
            try:
                arr_tmp = [1 for c in arr[k]]
                ax[i][j].pie(
                    arr_tmp,
                    labels=arr[k],
                    shadow=True,
                    startangle=90,
                    autopct="%1.1f%%",
                )
                ax[i][j].set_title(df[label].unique()[k])
                k += 1
            except:
                break

    plt.show()


# TODO check what can we remove, delete old comments that are unneeded
# find_best_epsilon("full")
# find_best_epsilon("scrape") #?

# Cluster_Graphs("full")
# Cluster_Graphs("scrape")

# PCA_Cluster_Graph() #Main Function
