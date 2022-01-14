from imports import *

FULL_DB_PATH = r"../CSV files/df_Full_DataBase.csv"
SCRAP_DB_PATH = r"../CSV files/df_scrape.csv"


def get_best_num_of_clusters_for_k_means(
    dataset, num_cluster_options, init_val, n_init_val, rand_state
):
    best_score = float("-inf")
    for k in num_cluster_options:
        model, pred = perform_k_means(dataset, k, init_val, n_init_val, rand_state)
        if best_score < silhouette_score(dataset, pred):
            best_score = silhouette_score(dataset, pred)
            num_clusters = k

    return best_score, num_clusters


def perform_k_means(dataset, num_clusters, init_val, n_init_val, rand_state):
    model = KMeans(
        n_clusters=num_clusters,
        init=init_val,
        n_init=n_init_val,
        random_state=rand_state,
    )
    predicted_vals = model.fit_predict(dataset)

    return model, predicted_vals


def Kmeans_clustering(data, num_clusters):

    model = KMeans(n_clusters=num_clusters, init="k-means++")
    kmeans = model.fit(data)
    data["Cluster"] = kmeans.labels_
    return data


def Cluster_Graphs(name):

    if name == "full":
        data = pd.read_csv(FULL_DB_PATH)
        columns = [
            ["Population Total", "GDP Total"],
            ["Population Total", "Life expectancy at birth"],
            ["Education Ranking", "GDP Total"],
            ["Total consumption ($)", "GDP Total"],
            ["Military Spendings ($)", "GDP Total"],
            ["Government expenditure (% of GDP)", "Education Ranking"],
        ]

        for i in columns:
            data = data[data["Year"] == 2020]
            data1 = data[i].copy()

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

            datanew = Kmeans_clustering(data1[i], num_clusters)

            fig, axes = plt.subplots(1, 2, figsize=(20, 5))
            axes[0].set_title("World Clusters")
            axes[0].scatter(
                datanew[i[0]], datanew[i[1]], c=datanew["Cluster"], s=50, cmap="plasma"
            )
            axes[0].set_xlabel(i[0])
            axes[0].set_ylabel(i[1])
            axes[1].set_title("World Continents")
            for con in data["Continent"].unique():
                axes[1].scatter(
                    datanew[data["Continent"] == con][i[0]],
                    datanew[data["Continent"] == con][i[1]],
                    label=con,
                    cmap="plasma",
                )
            axes[1].legend()
            plt.show()

    elif name == "scrape":
        data = pd.read_csv(SCRAP_DB_PATH)
        columns = [
            ["Cost of Living Index", "Affordability Index"],
        ]

        for i in columns:
            data = data[data["Year"] == 2020]
            data1 = data[i].copy()

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

            datanew = Kmeans_clustering(data1[i], num_clusters)

            fig, axes = plt.subplots(1, 2, figsize=(20, 5))
            axes[0].set_title("World Clusters")
            axes[0].scatter(
                datanew[i[0]], datanew[i[1]], c=datanew["Cluster"], s=50, cmap="plasma"
            )
            axes[0].set_xlabel(i[0])
            axes[0].set_ylabel(i[1])
            axes[1].set_title("World Continents")
            for con in data["Continent"].unique():
                axes[1].scatter(
                    datanew[data["Continent"] == con][i[0]],
                    datanew[data["Continent"] == con][i[1]],
                    label=con,
                    cmap="plasma",
                )
            axes[1].legend()
            plt.show()


def PCA_Total_graph(data):
    data = data[data["Year"] == 2020]
    dataPCA = data.copy()
    features = list(data.columns)
    features.remove("Continent")
    features.remove("Country")
    features.remove("Year")

    dataPCA = dataPCA.loc[:, features].values
    dataPCA = StandardScaler().fit_transform(dataPCA)
    pca = PCA(n_components=2)  # 2-dimensional PCA
    principalComponents = pca.fit_transform(dataPCA)
    # principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel("Principal Component 1", fontsize=15)
    ax.set_ylabel("Principal Component 2", fontsize=15)
    ax.set_title("2 component PCA", fontsize=20)
    # plt.scatter(dataPCA[:,0], dataPCA[:,1],  cmap="plasma")
    # plt.show()
    data["principal component 1"] = principalComponents[:, 0]
    data["principal component 2"] = principalComponents[:, 1]

    # Show complete graph
    # for continent in data["Continent"].unique():
    #     i=0
    #     countries = data[data["Continent"] == continent]["Country"].unique()
    #     #color map in size of len(countries)
    #     colors = cm.tab20(np.linspace(0, 1, len(countries)))
    #     # print(countries)
    #     for country in countries:
    #         plt.scatter(data[(data["Continent"] == continent) &  (data["Country"]==country)]["principal component 1"],
    #                 data[(data["Continent"] == continent) & (data["Country"]==country)]["principal component 2"],
    #                  )
    #         i+=1
    #     plt.title(continent)
    #     plt.legend(data[data["Continent"] == continent]["Country"].unique(), loc="best", fontsize="small")
    #     plt.show()
    return data


# Cluster_Graphs("full")
# Cluster_Graphs("scrape")

FULL_data = pd.read_csv(FULL_DB_PATH)
SCRAP_data = pd.read_csv(SCRAP_DB_PATH)

FULL_data = PCA_Total_graph(FULL_data)
SCRAP_data = PCA_Total_graph(SCRAP_data)


def PCA_Cluster_Graph(data):
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
    datanew = Kmeans_clustering(
        data[["principal component 1", "principal component 2"]], num_clusters
    )

    data["Cluster"] = datanew["Cluster"]

    # World scatter plot
    # plt.scatter(datanew["principal component 1"], datanew["principal component 2"], c=datanew["Cluster"], s=50, cmap="plasma")
    # plt.title("World")
    # plt.xlabel("principal component 1")
    # plt.ylabel("principal component 2")
    # plt.show()

    # Same scatter plot but with colors for continents
    # for con in data["Continent"].unique():
    #     plt.scatter(datanew[data["Continent"]==con]["principal component 1"], datanew[data["Continent"]==con]["principal component 2"],label=con, cmap="plasma")
    # plt.title("World")
    # plt.xlabel("principal component 1")
    # plt.ylabel("principal component 2")
    # plt.legend()
    # plt.show()

    fig, axes = plt.subplots(1, 2, figsize=(20, 5))
    axes[0].set_title("World Clusters")
    axes[0].scatter(
        datanew["principal component 1"],
        datanew["principal component 2"],
        c=datanew["Cluster"],
        s=50,
        cmap="plasma",
    )
    axes[1].set_title("World Continents")
    for con in data["Continent"].unique():
        axes[1].scatter(
            datanew[data["Continent"] == con]["principal component 1"],
            datanew[data["Continent"] == con]["principal component 2"],
            label=con,
            cmap="plasma",
        )
    axes[1].legend()
    # plt.show()

    # for continent in data["Continent"].unique():
    #     countries= data[data["Continent"] == continent]["Country"].unique()
    #     for i in datanew[data["Continent"] == continent]["Cluster"].unique():
    #         plt.scatter(datanew[(data["Continent"] == continent) & (datanew["Cluster"]==i)]["principal component 1"],
    #                 datanew[(data["Continent"] == continent) & (datanew["Cluster"]==i)]["principal component 2"],
    #                  cmap='rainbow', label=i)
    #     plt.title(continent)
    #     plt.legend()
    #     plt.show()
    return data


FULL_data = PCA_Cluster_Graph(FULL_data)
SCRAP_data = PCA_Cluster_Graph(SCRAP_data)

for data in [SCRAP_data]:
    item = []
    for clu in data["Cluster"].unique():
        item.append(data[data["Cluster"] == clu]["Country"].unique())
    dp = pd.DataFrame(item)

print(dp.transpose())
dp.to_csv("cluster_data.csv")
