from mteb.abstasks.clustering_legacy import AbsTaskClusteringLegacy
from mteb.abstasks.task_metadata import TaskMetadata


class SpanishWikiClusteringP2P(AbsTaskClusteringLegacy):
    metadata = TaskMetadata(
        name="SpanishWikiClusteringP2P",
        description=(
            "Clustering of Wikipedia article opening paragraphs in Spanish. "
            "Models must group 900 articles into 9 thematic categories without labels. "
            "Categories span geography, history, natural sciences, literature, organizations, "
            "language, natural phenomena, sports, and psychology."
        ),
        reference="https://huggingface.co/datasets/ClementeH/SpanishWikiClustering",
        dataset={
            "path": "ClementeH/SpanishWikiClustering",
            "revision": "1e18268d34f6ca5642399da61f180dc0faa3f401",
        },
        type="Clustering",
        category="t2c",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["spa-Latn"],
        main_score="v_measure",
        date=("2025-12-01", "2026-03-01"),
        domains=["Encyclopaedic", "Written"],
        task_subtypes=["Thematic clustering"],
        license="cc-by-sa-4.0",
        annotations_creators="derived",
        dialect=[],
        sample_creation="found",
        bibtex_citation="",
    )
