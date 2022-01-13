from sklearn.metrics import silhouette_score

from imports import *

FULL_DB_PATH = r"../CSV files/df_Full_DataBase.csv"
SCRAP_DB_PATH = r"../CSV files/df_scrape.csv"


data = pd.read_csv(FULL_DB_PATH)


def get_best_num_of_clusters_for_k_means(dataset, num_cluster_options, init_val, n_init_val, rand_state):
    best_score = float('-inf')
    for k in num_cluster_options:
        model, pred = perform_k_means(dataset, k, init_val, n_init_val, rand_state)
        if best_score < silhouette_score(dataset, pred):
            best_score = silhouette_score(dataset, pred)
            num_clusters = k

    return best_score, num_clusters

def perform_k_means(dataset, num_clusters, init_val, n_init_val, rand_state):
    model = KMeans(n_clusters=num_clusters, init=init_val, n_init=n_init_val, random_state=rand_state)
    predicted_vals = model.fit_predict(dataset)

    return model, predicted_vals



def Kmeans_clustering(data,num_clusters):

    model = KMeans(n_clusters=num_clusters, init="k-means++")
    kmeans = model.fit(data)
    data["Cluster"]=kmeans.labels_
    return data


columns = [["Population Total","GDP Total"], ["Population Total","Life expectancy at birth"], ["Education Ranking","GDP Total"],["Total consumption ($)","GDP Total"],["Military Spendings ($)","GDP Total"], ["Government expenditure (% of GDP)","Education Ranking"]]

for i in columns:
    data = data[data["Year"] == 2020]
    data1 = data[i].copy()

    score, num_clusters = get_best_num_of_clusters_for_k_means(data1.loc[:, data1.columns != "Continent"],
                                                               [ 4,5, 6, 7, 8 ,9 ,10, ], "k-means++", 15, 5)

    print(score,num_clusters)
    datanew = Kmeans_clustering(data1[i],num_clusters)
    # scatter plot
    plt.scatter(datanew[i[0]],
                datanew[i[1]],
                c=datanew["Cluster"],
                s=50,
                cmap='plasma')

    plt.xlabel(i[0])
    plt.ylabel(i[1])
    plt.show()

    # for continent in data["Continent"].unique():
    #     print(datanew[data["Continent"] == continent]["Cluster"])
    #     print(data[data["Continent"] == continent]["Country"].unique())
    #     plt.scatter(datanew[data["Continent"] == continent]["Cluster"],
    #                 data[data["Continent"] == continent]["Country"].unique(),
    #                 c=datanew[data["Continent"] == continent]["Cluster"], cmap='rainbow')
    #     plt.show()




