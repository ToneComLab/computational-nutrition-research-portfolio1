"""Elite research portfolio — paths and 30 paper definitions."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"
DATA_PROC = ROOT / "data" / "processed"
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
PAPERS_MD = ROOT / "papers" / "markdown"
PAPERS_PDF = ROOT / "papers" / "pdf"
LOGS = ROOT / "logs"

for p in (DATA_RAW, DATA_PROC, RESULTS, FIGURES, PAPERS_MD, PAPERS_PDF, LOGS):
    p.mkdir(parents=True, exist_ok=True)

NHANES_BASE = "https://wwwn.cdc.gov/nchs/nhanes/"
NHANES_2017 = {
    "DR1TOT": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/DR1TOT_J.xpt",
    "DEMO": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/DEMO_J.xpt",
    "BMX": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/BMX_J.xpt",
    "BPX": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/BPX_J.xpt",
}
NHANES_2011 = {
    "DR1TOT": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2011/DataFiles/DR1TOT_G.xpt",
    "DEMO": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2011/DataFiles/DEMO_G.xpt",
    "BMX": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2011/DataFiles/BMX_G.xpt",
    "BPX": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2011/DataFiles/BPX_G.xpt",
}

USDA_FDC_API = "https://api.nal.usda.gov/fdc/v1/"
USDA_API_KEY = "DEMO_KEY"
PUBMED_EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
WHO_GHO_API = "https://ghoapi.azureedge.net/api/"
WB_API = "https://api.worldbank.org/v2/"
FAO_STAT = "https://www.fao.org/faostat/"
PUBMED_EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
OPEN_NUTRITION = "https://raw.githubusercontent.com/selva86/datasets/master/nutrition.csv"

FIG_DPI = 300

# 30 non-overlapping topics (titles for manuscripts)
PAPERS_META = [
    {"id": 1, "slug": "energy_density_satiety", "title": "Energy Density and Satiety-Proxy Constructs from 24-Hour Recall: A Cross-Sectional Energy–Volume Framework in NHANES Adults"},
    {"id": 2, "slug": "macro_gi_interaction", "title": "Macronutrient Ratio × Glycemic Load Interaction Surfaces and Cardiometabolic Proxies: NHANES-Based Inference"},
    {"id": 3, "slug": "na_k_ratio_cvd", "title": "Dietary Sodium-to-Potassium Ratio and Blood Pressure Phenotypes: Population Stratification with Confidence Intervals"},
    {"id": 4, "slug": "upf_metabolic", "title": "Ultra-Processed Food Proxies via Nutrient Signatures and Metabolic Syndrome Components: A Pattern-Recognition Study"},
    {"id": 5, "slug": "cost_nutrient_density", "title": "Food Cost Efficiency versus Nutrient Density: USDA FoodData Central Augmentation with Survey-Scale Trade-Offs"},
    {"id": 6, "slug": "micronutrient_deficiency_risk", "title": "Micronutrient Inadequacy Risk Scores from Recall-Derived Intakes: Threshold Models with Uncertainty Quantification"},
    {"id": 7, "slug": "fiber_diversity_digestive", "title": "Fiber Diversity Indices and Digestive-Health Proxies: Variance Decomposition in U.S. Adults"},
    {"id": 8, "slug": "sugar_inflammation_proxy", "title": "Sugar Intake and Inflammation-Adjacent Phenotypes: Cross-Sectional Association with Metabolic Load"},
    {"id": 9, "slug": "alcohol_lipid", "title": "Alcohol Consumption Patterns and Lipid-Linked Biomarker Proxies in National Survey Data"},
    {"id": 10, "slug": "protein_aging_proxy", "title": "Protein Intake and Aging-Biomarker Proxies: Effect Sizes with Multiple Testing Awareness"},
    {"id": 11, "slug": "diet_diversity_ses", "title": "Diet Diversity versus Socioeconomic Gradients: Income-Adjusted Modeling with NHANES"},
    {"id": 12, "slug": "global_calorie_obesity", "title": "Global Caloric Supply and Obesity Prevalence: Ecological Coupling with World Bank and WHO Indicators"},
    {"id": 13, "slug": "nutrition_inequality_index", "title": "Construction of a Nutrition Inequality Index from Harmonized Global Health Observatory Metrics"},
    {"id": 14, "slug": "food_access_health", "title": "Food Accessibility Proxies and Health Outcomes: Cross-Scale Correlation with Macro Indicators"},
    {"id": 15, "slug": "income_diet_quality", "title": "Income Elasticity of Dietary Quality: PIR-Stratified Nutrient Density Models"},
    {"id": 16, "slug": "nutrient_network", "title": "Nutrient Interaction Network Graphs from Pairwise and Partial Association Structures"},
    {"id": 17, "slug": "kmeans_dietary_patterns", "title": "K-Means Clustering of Standardized Intakes for Dietary Pattern Phenotyping"},
    {"id": 18, "slug": "pca_archetypes", "title": "PCA-Based Nutritional Archetypes with Interpretable Loading Vectors and Component Scores"},
    {"id": 19, "slug": "predict_hypertension_diet", "title": "Predictive Modeling of Hypertension Status from Dietary Composition: Logistic Regression with ROC Diagnostics"},
    {"id": 20, "slug": "ml_health_risk", "title": "Machine Learning Classification of Cardiometabolic Risk from Multivariate Nutrient Features"},
    {"id": 21, "slug": "temporal_sugar", "title": "Temporal Trend Analysis of Sugar Intake Across NHANES Cycles with Structural Break Tests"},
    {"id": 22, "slug": "shift_sodium", "title": "Shift Detection in Sodium Consumption: Two-Sample and Robust Rank-Based Contrasts"},
    {"id": 23, "slug": "longitudinal_diet_change", "title": "Longitudinal Diet Change Modeling with Repeated Cross-Sectional Cohort Contrasts"},
    {"id": 24, "slug": "time_series_nutrition", "title": "Time-Series Nutrition Transition Analysis with External Macro Series Alignment"},
    {"id": 25, "slug": "generational_diet", "title": "Generational Diet Pattern Differences Using Age-Stratified Survey Microdata"},
    {"id": 26, "slug": "bibliometric_functional_foods", "title": "Bibliometric Trends in Functional Foods: PubMed Corpus Mining with Regression Slopes"},
    {"id": 27, "slug": "topic_modeling_nutrition", "title": "Topic-Structured Survey of Nutrition Research Keywords via PubMed Frequency Dynamics"},
    {"id": 28, "slug": "citation_network_proxy", "title": "Citation-Network Proxy Analysis Using Publication Volume and Co-Term Occurrence Metrics"},
    {"id": 29, "slug": "dietary_guidelines_evolution", "title": "Evolution of Dietary Guideline Emphasis: Bibliometric Contrast of Nutrient-Focused Queries"},
    {"id": 30, "slug": "meta_bioactive", "title": "Meta-Analytic Framing of Bioactive Compound Research: Systematic PubMed Enumeration with Heterogeneity Discussion"},
]
