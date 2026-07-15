import networkx as nx
import matplotlib.pyplot as plt


class ConceptMap:

    def __init__(self):

        self.graph = nx.Graph()

    def build_graph(self, concepts):

        self.graph.clear()

        if not concepts:
            return

        main_concept = concepts[0]

        self.graph.add_node(main_concept)

        for concept in concepts[1:]:

            self.graph.add_edge(
                main_concept,
                concept
            )

    def get_figure(self):

        figure = plt.figure(
            figsize=(8, 6)
        )

        position = nx.spring_layout(
            self.graph,
            seed=42
        )

        nx.draw(

            self.graph,

            position,

            with_labels=True,

            node_size=3200,

            node_color="skyblue",

            edge_color="gray",

            font_size=10,

            font_weight="bold"

        )

        plt.title(
            "Research Concept Map",
            fontsize=15,
            fontweight="bold"
        )

        return figure


if __name__ == "__main__":

    concepts = [

        "Reinforcement Learning",

        "Machine Learning Technique",

        "Agent",

        "Environment",

        "Rewards"

    ]

    graph = ConceptMap()

    graph.build_graph(concepts)

    figure = graph.get_figure()

    plt.show()