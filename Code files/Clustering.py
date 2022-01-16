from imports import *


FULL_DB_PATH = r"../CSV files/df_Full_DataBase.csv"
SCRAP_DB_PATH = r"../CSV files/df_scrape.csv"
REMOVE_COLUMN = ["Continent", "Country", "Year"]


def get_best_num_of_clusters_for_k_means(
    dataset, num_cluster_options, init_val="k-means++", n_init_val=10, rand_state=None
):
    """Check and return the best number of clusters for k-means clustering

    Args:
        dataset,
        num_cluster_options,
        init_val,
        n_init_val,
        rand_state - Tony please fill

    Returns:
        score, number of clusters
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
        dataset,
        num_cluster_options,
        init_val,
        n_init_val,
        rand_state - Tony please fill

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
        dataset,
        epsilon_val,
        minimum_samples_val,

    Returns:
        model, predicted_vals
    """
    model = DBSCAN(eps=epsilon_val, min_samples=minimum_samples_val)

    predicted_vals = model.fit_predict(dataset)

    return model, predicted_vals


def get_best_params_for_dbscan(dataset, eps_options, min_samples_options):
    """Check and return the best number of clusters for DBScan clustering

    Args:
        dataset,
        eps_options,
        min_samples_options,

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
        name - name of the database

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

    """Assign the correct database to the correct columns"""
    if name == "full":
        data = pd.read_csv(FULL_DB_PATH)
        columns = columnsFULL
    elif name == "scrape":
        data = pd.read_csv(SCRAP_DB_PATH)
        columns = columnsSCRAP

    """Main For loop """
    for column in columns:

        # Prepate the data to cluster
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

        # dbscan

        # Prepate the data to cluster
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


def PCA_Total_graph(data):
    """Convert the data to PCA

    Args:
        data

    Returns:
        data - dataframe with PCA
    """
    # Data Preparation
    data = data[data["Year"] == 2020]
    dataPCA = data.copy()
    features = list(data.columns)

    for column in REMOVE_COLUMN:
        features.remove(column)

    # PCA-ing
    dataPCA = dataPCA.loc[:, features].values
    dataPCA = StandardScaler().fit_transform(dataPCA)
    pca = PCA(n_components=2)  # 2-dimensional PCA
    principalComponents = pca.fit_transform(dataPCA)

    # Plot the PCA(for testing purposes)
    # fig = plt.figure(figsize=(8, 8))
    # ax = fig.add_subplot(1, 1, 1)
    # ax.set_xlabel("Principal Component 1", fontsize=15)
    # ax.set_ylabel("Principal Component 2", fontsize=15)
    # ax.set_title("2 component PCA", fontsize=20)
    # plt.scatter(dataPCA[:,0], dataPCA[:,1],  cmap="plasma")
    # plt.show()

    data["principal component 1"] = principalComponents[:, 0]
    data["principal component 2"] = principalComponents[:, 1]

    return data


def PCA_Cluster_Graph(data):
    """Perform Clutsering on PCA data

    Args:
        data -

    Returns:
        data - dataframe with PCA
    """
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

    data["kmean-cluster"] = KmeansData
    data["dbscan-cluster"] = DBSCANData

    # Kmean scatter plot
    ComparePlot(data, num_clusters, score, "kmean-cluster")

    # DBScan scatter plot
    ComparePlot(data, best_eps, best_score, "dbscan-cluster")

    return data


def ComparePlot(data, num_clusters, score, label):

    fig, axes = plt.subplots(1, 2, figsize=(20, 5))
    fig.suptitle(label)
    axes[0].set_title("World Clusters -" + str(num_clusters) + " - " + str(score))
    axes[0].scatter(
        data["principal component 1"],
        data["principal component 2"],
        c=data[label],
        s=50,
        cmap="plasma",
    )
    axes[1].set_title("World Continents")
    for con in data["Continent"].unique():
        axes[1].scatter(
            data[data["Continent"] == con]["principal component 1"],
            data[data["Continent"] == con]["principal component 2"],
            label=con,
            cmap="plasma",
        )
    axes[1].legend()

    plt.show()


# send DataFrame here and max amount of neighbors to find best epsilon for DBscan
def best_epsilon(FULL_data, max_neighbors):
    data = FULL_data.copy()
    data = data.drop(columns=REMOVE_COLUMN)

    for n in range(2, max_neighbors + 1):
        neigh = NearestNeighbors(n_neighbors=n)
        nbrs = neigh.fit(data)
        distances, indices = nbrs.kneighbors(data)

        distances = np.sort(distances, axis=0)
        distances = distances[:, 1]
        plt.plot(distances)
        plt.title("n_neighbors :%d " % n)
        plt.show()


Cluster_Graphs("full")
Cluster_Graphs("scrape")


FULL_data = pd.read_csv(FULL_DB_PATH)
SCRAP_data = pd.read_csv(SCRAP_DB_PATH)

FULL_data = PCA_Total_graph(FULL_data)
SCRAP_data = PCA_Total_graph(SCRAP_data)


FULL_data = PCA_Cluster_Graph(FULL_data)
SCRAP_data = PCA_Cluster_Graph(SCRAP_data)


for data in [SCRAP_data]:
    item = []
    for clu in data["kmean-cluster"].unique():
        item.append(data[data["kmean-cluster"] == clu]["Country"].unique())
    dp = pd.DataFrame(item)

print(dp.transpose())
dp.to_csv("cluster_data.csv")
