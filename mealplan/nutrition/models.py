from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel


class Nutrition(BaseModel):
    """
    All values are per 100g of ingredient
    """
    ingredient = models.OneToOneField(
        'ingredients.Ingredient',
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='nutrition',
    )

    # Nutrients

    nitrogen = models.FloatField(                                  # 1002 G
        _('Nitrogen'), null=True, blank=True)
    protein = models.FloatField(                                   # 1003 G
        _('Protein'), null=True, blank=True)
    total_lipid_fat = models.FloatField(                           # 1004 G
        _('Total lipid (fat)'), null=True, blank=True)
    carbohydrate_by_difference = models.FloatField(                # 1005 G
        _('Carbohydrate, by difference'), null=True, blank=True)
    ash = models.FloatField(                                       # 1007 G
        _('Ash'), null=True, blank=True)
    energy = models.FloatField(                                    # 1008 KCAL
        _('Energy'), null=True, blank=True)
    starch = models.FloatField(                                    # 1009 G
        _('Starch'), null=True, blank=True)
    sucrose = models.FloatField(                                   # 1010 G
        _('Sucrose'), null=True, blank=True)
    glucose_dextrose = models.FloatField(                          # 1011 G
        _('Glucose (dextrose)'), null=True, blank=True)
    fructose = models.FloatField(                                  # 1012 G
        _('Fructose'), null=True, blank=True)
    lactose = models.FloatField(                                   # 1013 G
        _('Lactose'), null=True, blank=True)
    maltose = models.FloatField(                                   # 1014 G
        _('Maltose'), null=True, blank=True)
    alcohol_ethyl = models.FloatField(                             # 1018 G
        _('Alcohol, ethyl'), null=True, blank=True)
    specific_gravity = models.FloatField(                          # 1024 SP_GR
        _('Specific Gravity'), null=True, blank=True)
    acetic_acid = models.FloatField(                               # 1026 MG
        _('Acetic acid'), null=True, blank=True)
    lactic_acid = models.FloatField(                               # 1038 MG
        _('Lactic acid'), null=True, blank=True)
    carbohydrate_by_summation = models.FloatField(                 # 1050 G
        _('Carbohydrate, by summation'), null=True, blank=True)
    water = models.FloatField(                                     # 1051 G
        _('Water'), null=True, blank=True)
    sorbitol = models.FloatField(                                  # 1056 G
        _('Sorbitol'), null=True, blank=True)
    caffeine = models.FloatField(                                  # 1057 MG
        _('Caffeine'), null=True, blank=True)
    theobromine = models.FloatField(                               # 1058 MG
        _('Theobromine'), null=True, blank=True)
    energy = models.FloatField(                                    # 1062 kJ
        _('Energy'), null=True, blank=True)
    sugars_total_nlea = models.FloatField(                         # 1063 G
        _('Sugars, Total NLEA'), null=True, blank=True)
    carbohydrate_other = models.FloatField(                        # 1072 G
        _('Carbohydrate, other'), null=True, blank=True)
    galactose = models.FloatField(                                 # 1075 G
        _('Galactose'), null=True, blank=True)
    xylitol = models.FloatField(                                   # 1078 G
        _('Xylitol'), null=True, blank=True)
    fiber_total_dietary = models.FloatField(                       # 1079 G
        _('Fiber, total dietary'), null=True, blank=True)
    ribose = models.FloatField(                                    # 1081 G
        _('Ribose'), null=True, blank=True)
    fiber_soluble = models.FloatField(                             # 1082 G
        _('Fiber, soluble'), null=True, blank=True)
    fiber_insoluble = models.FloatField(                           # 1084 G
        _('Fiber, insoluble'), null=True, blank=True)
    total_fat_nlea = models.FloatField(                            # 1085 G
        _('Total fat (NLEA)'), null=True, blank=True)
    total_sugar_alcohols = models.FloatField(                      # 1086 G
        _('Total sugar alcohols'), null=True, blank=True)
    calcium_ca = models.FloatField(                                # 1087 MG
        _('Calcium, Ca'), null=True, blank=True)
    chlorine_cl = models.FloatField(                               # 1088 MG
        _('Chlorine, Cl'), null=True, blank=True)
    iron_fe = models.FloatField(                                   # 1089 MG
        _('Iron, Fe'), null=True, blank=True)
    magnesium_mg = models.FloatField(                              # 1090 MG
        _('Magnesium, Mg'), null=True, blank=True)
    phosphorus_p = models.FloatField(                              # 1091 MG
        _('Phosphorus, P'), null=True, blank=True)
    potassium_k = models.FloatField(                               # 1092 MG
        _('Potassium, K'), null=True, blank=True)
    sodium_na = models.FloatField(                                 # 1093 MG
        _('Sodium, Na'), null=True, blank=True)
    sulfur_s = models.FloatField(                                  # 1094 MG
        _('Sulfur, S'), null=True, blank=True)
    zinc_zn = models.FloatField(                                   # 1095 MG
        _('Zinc, Zn'), null=True, blank=True)
    chromium_cr = models.FloatField(                               # 1096 UG
        _('Chromium, Cr'), null=True, blank=True)
    cobalt_co = models.FloatField(                                 # 1097 UG
        _('Cobalt, Co'), null=True, blank=True)
    copper_cu = models.FloatField(                                 # 1098 MG
        _('Copper, Cu'), null=True, blank=True)
    fluoride_f = models.FloatField(                                # 1099 UG
        _('Fluoride, F'), null=True, blank=True)
    iodine_i = models.FloatField(                                  # 1100 UG
        _('Iodine, I'), null=True, blank=True)
    manganese_mn = models.FloatField(                              # 1101 MG
        _('Manganese, Mn'), null=True, blank=True)
    molybdenum_mo = models.FloatField(                             # 1102 UG
        _('Molybdenum, Mo'), null=True, blank=True)
    selenium_se = models.FloatField(                               # 1103 UG
        _('Selenium, Se'), null=True, blank=True)
    vitamin_a_iu = models.FloatField(                              # 1104 IU
        _('Vitamin A, IU'), null=True, blank=True)
    retinol = models.FloatField(                                   # 1105 UG
        _('Retinol'), null=True, blank=True)
    vitamin_a_rae = models.FloatField(                             # 1106 UG
        _('Vitamin A, RAE'), null=True, blank=True)
    carotene_beta = models.FloatField(                             # 1107 UG
        _('Carotene, beta'), null=True, blank=True)
    carotene_alpha = models.FloatField(                            # 1108 UG
        _('Carotene, alpha'), null=True, blank=True)
    vitamin_e_alpha_tocopherol = models.FloatField(                # 1109 MG
        _('Vitamin E (alpha-tocopherol)'), null=True, blank=True)
    vitamin_d = models.FloatField(                                 # 1110 IU
        _('Vitamin D'), null=True, blank=True)
    vitamin_d2_ergocalciferol = models.FloatField(                 # 1111 UG
        _('Vitamin D2 (ergocalciferol)'), null=True, blank=True)
    vitamin_d3_cholecalciferol = models.FloatField(                # 1112 UG
        _('Vitamin D3 (cholecalciferol)'), null=True, blank=True)
    acid_25_hydroxycholecalciferol = models.FloatField(            # 1113 UG
        _('25-hydroxycholecalciferol'), null=True, blank=True)
    vitamin_d_d2_d3 = models.FloatField(                           # 1114 UG
        _('Vitamin D (D2 + D3)'), null=True, blank=True)
    phytoene = models.FloatField(                                  # 1116 UG
        _('Phytoene'), null=True, blank=True)
    phytofluene = models.FloatField(                               # 1117 UG
        _('Phytofluene'), null=True, blank=True)
    zeaxanthin = models.FloatField(                                # 1119 UG
        _('Zeaxanthin'), null=True, blank=True)
    cryptoxanthin_beta = models.FloatField(                        # 1120 UG
        _('Cryptoxanthin, beta'), null=True, blank=True)
    lutein = models.FloatField(                                    # 1121 UG
        _('Lutein'), null=True, blank=True)
    lycopene = models.FloatField(                                  # 1122 UG
        _('Lycopene'), null=True, blank=True)
    lutein_zeaxanthin = models.FloatField(                         # 1123 UG
        _('Lutein + zeaxanthin'), null=True, blank=True)
    vitamin_e_label_entry_primarily = models.FloatField(           # 1124 IU
        _('Vitamin E (label entry primarily)'), null=True, blank=True)
    tocopherol_beta = models.FloatField(                           # 1125 MG
        _('Tocopherol, beta'), null=True, blank=True)
    tocopherol_gamma = models.FloatField(                          # 1126 MG
        _('Tocopherol, gamma'), null=True, blank=True)
    tocopherol_delta = models.FloatField(                          # 1127 MG
        _('Tocopherol, delta'), null=True, blank=True)
    tocotrienol_alpha = models.FloatField(                         # 1128 MG
        _('Tocotrienol, alpha'), null=True, blank=True)
    tocotrienol_beta = models.FloatField(                          # 1129 MG
        _('Tocotrienol, beta'), null=True, blank=True)
    tocotrienol_gamma = models.FloatField(                         # 1130 MG
        _('Tocotrienol, gamma'), null=True, blank=True)
    tocotrienol_delta = models.FloatField(                         # 1131 MG
        _('Tocotrienol, delta'), null=True, blank=True)
    boron_b = models.FloatField(                                   # 1137 UG
        _('Boron, B'), null=True, blank=True)
    nickel_ni = models.FloatField(                                 # 1146 UG
        _('Nickel, Ni'), null=True, blank=True)
    vitamin_e = models.FloatField(                                 # 1158 MG_ATE
        _('Vitamin E'), null=True, blank=True)
    cis_beta_carotene = models.FloatField(                         # 1159 UG
        _('cis-beta-Carotene'), null=True, blank=True)
    cis_lycopene = models.FloatField(                              # 1160 UG
        _('cis-Lycopene'), null=True, blank=True)
    cis_lutein_zeaxanthin = models.FloatField(                     # 1161 UG
        _('cis-Lutein/Zeaxanthin'), null=True, blank=True)
    vitamin_c_total_ascorbic_acid = models.FloatField(             # 1162 MG
        _('Vitamin C, total ascorbic acid'), null=True, blank=True)
    thiamin = models.FloatField(                                   # 1165 MG
        _('Thiamin'), null=True, blank=True)
    riboflavin = models.FloatField(                                # 1166 MG
        _('Riboflavin'), null=True, blank=True)
    niacin = models.FloatField(                                    # 1167 MG
        _('Niacin'), null=True, blank=True)
    pantothenic_acid = models.FloatField(                          # 1170 MG
        _('Pantothenic acid'), null=True, blank=True)
    vitamin_b_6 = models.FloatField(                               # 1175 MG
        _('Vitamin B-6'), null=True, blank=True)
    biotin = models.FloatField(                                    # 1176 UG
        _('Biotin'), null=True, blank=True)
    folate_total = models.FloatField(                              # 1177 UG
        _('Folate, total'), null=True, blank=True)
    vitamin_b_12 = models.FloatField(                              # 1178 UG
        _('Vitamin B-12'), null=True, blank=True)
    choline_total = models.FloatField(                             # 1180 MG
        _('Choline, total'), null=True, blank=True)
    inositol = models.FloatField(                                  # 1181 MG
        _('Inositol'), null=True, blank=True)
    menaquinone_4 = models.FloatField(                             # 1183 UG
        _('Menaquinone-4'), null=True, blank=True)
    dihydrophylloquinone = models.FloatField(                      # 1184 UG
        _('Dihydrophylloquinone'), null=True, blank=True)
    vitamin_k_phylloquinone = models.FloatField(                   # 1185 UG
        _('Vitamin K (phylloquinone)'), null=True, blank=True)
    folic_acid = models.FloatField(                                # 1186 UG
        _('Folic acid'), null=True, blank=True)
    folate_food = models.FloatField(                               # 1187 UG
        _('Folate, food'), null=True, blank=True)
    acid_5_methyl_tetrahydrofolate_5_mthf = models.FloatField(     # 1188 UG
        _('5-methyl tetrahydrofolate (5-MTHF)'), null=True, blank=True)
    folate_dfe = models.FloatField(                                # 1190 UG
        _('Folate, DFE'), null=True, blank=True)
    acid_10_formyl_folic_acid_10hcofa = models.FloatField(         # 1191 UG
        _('10-Formyl folic acid (10HCOFA)'), null=True, blank=True)
    acid_5_formyltetrahydrofolic_acid_5_hcoh4 = models.FloatField(  # 1192 UG
        _('5-Formyltetrahydrofolic acid (5-HCOH4'), null=True, blank=True)
    choline_free = models.FloatField(                              # 1194 MG
        _('Choline, free'), null=True, blank=True)
    choline_from_phosphocholine = models.FloatField(               # 1195 MG
        _('Choline, from phosphocholine'), null=True, blank=True)
    choline_from_phosphotidyl_choline = models.FloatField(         # 1196 MG
        _('Choline, from phosphotidyl choline'), null=True, blank=True)
    choline_from_glycerophosphocholine = models.FloatField(        # 1197 MG
        _('Choline, from glycerophosphocholine'), null=True, blank=True)
    betaine = models.FloatField(                                   # 1198 MG
        _('Betaine'), null=True, blank=True)
    choline_from_sphingomyelin = models.FloatField(                # 1199 MG
        _('Choline, from sphingomyelin'), null=True, blank=True)
    tryptophan = models.FloatField(                                # 1210 G
        _('Tryptophan'), null=True, blank=True)
    threonine = models.FloatField(                                 # 1211 G
        _('Threonine'), null=True, blank=True)
    isoleucine = models.FloatField(                                # 1212 G
        _('Isoleucine'), null=True, blank=True)
    leucine = models.FloatField(                                   # 1213 G
        _('Leucine'), null=True, blank=True)
    lysine = models.FloatField(                                    # 1214 G
        _('Lysine'), null=True, blank=True)
    methionine = models.FloatField(                                # 1215 G
        _('Methionine'), null=True, blank=True)
    cystine = models.FloatField(                                   # 1216 G
        _('Cystine'), null=True, blank=True)
    phenylalanine = models.FloatField(                             # 1217 G
        _('Phenylalanine'), null=True, blank=True)
    tyrosine = models.FloatField(                                  # 1218 G
        _('Tyrosine'), null=True, blank=True)
    valine = models.FloatField(                                    # 1219 G
        _('Valine'), null=True, blank=True)
    arginine = models.FloatField(                                  # 1220 G
        _('Arginine'), null=True, blank=True)
    histidine = models.FloatField(                                 # 1221 G
        _('Histidine'), null=True, blank=True)
    alanine = models.FloatField(                                   # 1222 G
        _('Alanine'), null=True, blank=True)
    aspartic_acid = models.FloatField(                             # 1223 G
        _('Aspartic acid'), null=True, blank=True)
    glutamic_acid = models.FloatField(                             # 1224 G
        _('Glutamic acid'), null=True, blank=True)
    glycine = models.FloatField(                                   # 1225 G
        _('Glycine'), null=True, blank=True)
    proline = models.FloatField(                                   # 1226 G
        _('Proline'), null=True, blank=True)
    serine = models.FloatField(                                    # 1227 G
        _('Serine'), null=True, blank=True)
    hydroxyproline = models.FloatField(                            # 1228 G
        _('Hydroxyproline'), null=True, blank=True)
    cysteine = models.FloatField(                                  # 1232 G
        _('Cysteine'), null=True, blank=True)
    glutamine = models.FloatField(                                 # 1233 G
        _('Glutamine'), null=True, blank=True)
    taurine = models.FloatField(                                   # 1234 G
        _('Taurine'), null=True, blank=True)
    sugars_added = models.FloatField(                              # 1235 G
        _('Sugars, added'), null=True, blank=True)
    vitamin_e_added = models.FloatField(                           # 1242 MG
        _('Vitamin E, added'), null=True, blank=True)
    vitamin_b_12_added = models.FloatField(                        # 1246 UG
        _('Vitamin B-12, added'), null=True, blank=True)
    cholesterol = models.FloatField(                               # 1253 MG
        _('Cholesterol'), null=True, blank=True)
    fatty_acids_total_trans = models.FloatField(                   # 1257 G
        _('Fatty acids, total trans'), null=True, blank=True)
    fatty_acids_total_saturated = models.FloatField(               # 1258 G
        _('Fatty acids, total saturated'), null=True, blank=True)
    acid_4_0 = models.FloatField(                                  # 1259 G
        _('4:0'), null=True, blank=True)
    acid_6_0 = models.FloatField(                                  # 1260 G
        _('6:0'), null=True, blank=True)
    acid_8_0 = models.FloatField(                                  # 1261 G
        _('8:0'), null=True, blank=True)
    acid_10_0 = models.FloatField(                                 # 1262 G
        _('10:0'), null=True, blank=True)
    acid_12_0 = models.FloatField(                                 # 1263 G
        _('12:0'), null=True, blank=True)
    acid_14_0 = models.FloatField(                                 # 1264 G
        _('14:0'), null=True, blank=True)
    acid_16_0 = models.FloatField(                                 # 1265 G
        _('16:0'), null=True, blank=True)
    acid_18_0 = models.FloatField(                                 # 1266 G
        _('18:0'), null=True, blank=True)
    acid_20_0 = models.FloatField(                                 # 1267 G
        _('20:0'), null=True, blank=True)
    acid_18_1 = models.FloatField(                                 # 1268 G
        _('18:1'), null=True, blank=True)
    acid_18_2 = models.FloatField(                                 # 1269 G
        _('18:2'), null=True, blank=True)
    acid_18_3 = models.FloatField(                                 # 1270 G
        _('18:3'), null=True, blank=True)
    acid_20_4 = models.FloatField(                                 # 1271 G
        _('20:4'), null=True, blank=True)
    acid_22_6_n_3_dha = models.FloatField(                         # 1272 G
        _('22:6 n-3 (DHA)'), null=True, blank=True)
    acid_22_0 = models.FloatField(                                 # 1273 G
        _('22:0'), null=True, blank=True)
    acid_14_1 = models.FloatField(                                 # 1274 G
        _('14:1'), null=True, blank=True)
    acid_16_1 = models.FloatField(                                 # 1275 G
        _('16:1'), null=True, blank=True)
    acid_18_4 = models.FloatField(                                 # 1276 G
        _('18:4'), null=True, blank=True)
    acid_20_1 = models.FloatField(                                 # 1277 G
        _('20:1'), null=True, blank=True)
    acid_20_5_n_3_epa = models.FloatField(                         # 1278 G
        _('20:5 n-3 (EPA)'), null=True, blank=True)
    acid_22_1 = models.FloatField(                                 # 1279 G
        _('22:1'), null=True, blank=True)
    acid_22_5_n_3_dpa = models.FloatField(                         # 1280 G
        _('22:5 n-3 (DPA)'), null=True, blank=True)
    acid_14_1_t = models.FloatField(                               # 1281 G
        _('14:1 t'), null=True, blank=True)
    phytosterols = models.FloatField(                              # 1283 MG
        _('Phytosterols'), null=True, blank=True)
    stigmasterol = models.FloatField(                              # 1285 MG
        _('Stigmasterol'), null=True, blank=True)
    campesterol = models.FloatField(                               # 1286 MG
        _('Campesterol'), null=True, blank=True)
    beta_sitosterol = models.FloatField(                           # 1288 MG
        _('Beta-sitosterol'), null=True, blank=True)
    fatty_acids_total_monounsaturated = models.FloatField(         # 1292 G
        _('Fatty acids, total monounsaturated'), null=True, blank=True)
    fatty_acids_total_polyunsaturated = models.FloatField(         # 1293 G
        _('Fatty acids, total polyunsaturated'), null=True, blank=True)
    acid_15_0 = models.FloatField(                                 # 1299 G
        _('15:0'), null=True, blank=True)
    acid_17_0 = models.FloatField(                                 # 1300 G
        _('17:0'), null=True, blank=True)
    acid_24_0 = models.FloatField(                                 # 1301 G
        _('24:0'), null=True, blank=True)
    acid_16_1_t = models.FloatField(                               # 1303 G
        _('16:1 t'), null=True, blank=True)
    acid_18_1_t = models.FloatField(                               # 1304 G
        _('18:1 t'), null=True, blank=True)
    acid_22_1_t = models.FloatField(                               # 1305 G
        _('22:1 t'), null=True, blank=True)
    acid_18_2_t_not_further_defined = models.FloatField(           # 1306 G
        _('18:2 t not further defined'), null=True, blank=True)
    acid_18_2_i = models.FloatField(                               # 1307 G
        _('18:2 i'), null=True, blank=True)
    acid_18_2_tt = models.FloatField(                              # 1310 G
        _('18:2 t,t'), null=True, blank=True)
    acid_18_2_clas = models.FloatField(                            # 1311 G
        _('18:2 CLAs'), null=True, blank=True)
    acid_24_1_c = models.FloatField(                               # 1312 G
        _('24:1 c'), null=True, blank=True)
    acid_20_2_n_6_cc = models.FloatField(                          # 1313 G
        _('20:2 n-6 c,c'), null=True, blank=True)
    acid_16_1_c = models.FloatField(                               # 1314 G
        _('16:1 c'), null=True, blank=True)
    acid_18_1_c = models.FloatField(                               # 1315 G
        _('18:1 c'), null=True, blank=True)
    acid_18_2_n_6_cc = models.FloatField(                          # 1316 G
        _('18:2 n-6 c,c'), null=True, blank=True)
    acid_22_1_c = models.FloatField(                               # 1317 G
        _('22:1 c'), null=True, blank=True)
    acid_18_3_n_6_ccc = models.FloatField(                         # 1321 G
        _('18:3 n-6 c,c,c'), null=True, blank=True)
    acid_17_1 = models.FloatField(                                 # 1323 G
        _('17:1'), null=True, blank=True)
    acid_20_3 = models.FloatField(                                 # 1325 G
        _('20:3'), null=True, blank=True)
    fatty_acids_total_trans_monoenoic = models.FloatField(         # 1329 G
        _('Fatty acids, total trans-monoenoic'), null=True, blank=True)
    fatty_acids_total_trans_dienoic = models.FloatField(           # 1330 G
        _('Fatty acids, total trans-dienoic'), null=True, blank=True)
    fatty_acids_total_trans_polyenoic = models.FloatField(         # 1331 G
        _('Fatty acids, total trans-polyenoic'), null=True, blank=True)
    acid_13_0 = models.FloatField(                                 # 1332 G
        _('13:0'), null=True, blank=True)
    acid_15_1 = models.FloatField(                                 # 1333 G
        _('15:1'), null=True, blank=True)
    acid_22_2 = models.FloatField(                                 # 1334 G
        _('22:2'), null=True, blank=True)
    acid_11_0 = models.FloatField(                                 # 1335 G
        _('11:0'), null=True, blank=True)
    epigallocatechin_3_gallate = models.FloatField(                # 1368 MG
        _('Epigallocatechin-3-gallate'), null=True, blank=True)
    inulin = models.FloatField(                                    # 1403 G
        _('Inulin'), null=True, blank=True)
    acid_18_3_n_3_ccc_ala = models.FloatField(                     # 1404 G
        _('18:3 n-3 c,c,c (ALA)'), null=True, blank=True)
    acid_20_3_n_3 = models.FloatField(                             # 1405 G
        _('20:3 n-3'), null=True, blank=True)
    acid_20_3_n_6 = models.FloatField(                             # 1406 G
        _('20:3 n-6'), null=True, blank=True)
    acid_20_4_n_6 = models.FloatField(                             # 1408 G
        _('20:4 n-6'), null=True, blank=True)
    acid_18_3i = models.FloatField(                                # 1409 G
        _('18:3i'), null=True, blank=True)
    acid_21_5 = models.FloatField(                                 # 1410 G
        _('21:5'), null=True, blank=True)
    acid_22_4 = models.FloatField(                                 # 1411 G
        _('22:4'), null=True, blank=True)
    acid_18_1_11_t_18_1t_n_7 = models.FloatField(                  # 1412 G
        _('18:1-11 t (18:1t n-7)'), null=True, blank=True)
    acid_20_3_n_9 = models.FloatField(                             # 1414 G
        _('20:3 n-9'), null=True, blank=True)
    sugars_total_including_nlea = models.FloatField(               # 2000 G
        _('Sugars, total including NLEA'), null=True, blank=True)
    acid_5_0 = models.FloatField(                                  # 2003 G
        _('5:0'), null=True, blank=True)
    acid_7_0 = models.FloatField(                                  # 2004 G
        _('7:0'), null=True, blank=True)
    acid_9_0 = models.FloatField(                                  # 2005 G
        _('9:0'), null=True, blank=True)
    acid_21_0 = models.FloatField(                                 # 2006 G
        _('21:0'), null=True, blank=True)
    acid_23_0 = models.FloatField(                                 # 2007 G
        _('23:0'), null=True, blank=True)
    acid_12_1 = models.FloatField(                                 # 2008 G
        _('12:1'), null=True, blank=True)
    acid_14_1_c = models.FloatField(                               # 2009 G
        _('14:1 c'), null=True, blank=True)
    acid_17_1_c = models.FloatField(                               # 2010 G
        _('17:1 c'), null=True, blank=True)
    acid_20_1_c = models.FloatField(                               # 2012 G
        _('20:1 c'), null=True, blank=True)
    acid_20_1_t = models.FloatField(                               # 2013 G
        _('20:1 t'), null=True, blank=True)
    acid_22_1_n_9 = models.FloatField(                             # 2014 G
        _('22:1 n-9'), null=True, blank=True)
    acid_22_1_n_11 = models.FloatField(                            # 2015 G
        _('22:1 n-11'), null=True, blank=True)
    acid_18_2_c = models.FloatField(                               # 2016 G
        _('18:2 c'), null=True, blank=True)
    acid_18_3_c = models.FloatField(                               # 2018 G
        _('18:3 c'), null=True, blank=True)
    acid_18_3_t = models.FloatField(                               # 2019 G
        _('18:3 t'), null=True, blank=True)
    acid_20_3_c = models.FloatField(                               # 2020 G
        _('20:3 c'), null=True, blank=True)
    acid_22_3 = models.FloatField(                                 # 2021 G
        _('22:3'), null=True, blank=True)
    acid_20_4_c = models.FloatField(                               # 2022 G
        _('20:4 c'), null=True, blank=True)
    acid_20_5_c = models.FloatField(                               # 2023 G
        _('20:5 c'), null=True, blank=True)
    acid_22_5_c = models.FloatField(                               # 2024 G
        _('22:5 c'), null=True, blank=True)
    acid_22_6_c = models.FloatField(                               # 2025 G
        _('22:6 c'), null=True, blank=True)
    acid_20_2_c = models.FloatField(                               # 2026 G
        _('20:2 c'), null=True, blank=True)
    trans_beta_carotene = models.FloatField(                       # 2028 UG
        _('trans-beta-Carotene'), null=True, blank=True)
    trans_lycopene = models.FloatField(                            # 2029 UG
        _('trans-Lycopene'), null=True, blank=True)
    cryptoxanthin_alpha = models.FloatField(                       # 2032 UG
        _('Cryptoxanthin, alpha'), null=True, blank=True)

    class Meta():
        verbose_name = _('Nutrition')
        verbose_name_plural = _('Nutrition')

    # TODO: implement mathematical operations
    """
    def __add__(self, other):
        if type(other) is not type(self):
            # Needed for sum() to work
            if type(other) is int or type(other) is float:
                return self
            else:
                raise TypeError("Nutrition can be added "
                                "only with other Nutritions")

        # Create a new value dict with added values
        # Don't add ingredient and id -> would throw an error
        tot_vals = {}
        for f in self._meta.get_fields():
            try:
                added = f.value_from_object(self) + f.value_from_object(other)
            except TypeError as e:
                # Fields can be None, pick whichever isn't None
                if f.value_from_object(other) is None:
                    added = f.value_from_object(self)
                else:
                    added = f.value_from_object(other)
            tot_vals[f.name] = added

        # Make sure ID and Ingredient aren't added
        tot_vals["id"] = 0
        tot_vals["ingredient"] = None

        # Create a new Nutrition from the added values
        tot = Nutrition(**tot_vals)
        return tot

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        try:
            other = float(other)
        except ValueError:
            raise TypeError("Nutrition can only be multiplied a number")

        # Create a new value dict with added values
        # Don't multiply ingredient and id -> would throw an error
        tot_vals = {}
        for f in self._meta.get_fields():
            try:
                multiplied = f.value_from_object(self) * other
            except TypeError:
                # It's ok if it's None
                multiplied = None
            tot_vals[f.name] = multiplied

        # Make sure ID and Ingredient aren't multiplied
        tot_vals["id"] = 0
        tot_vals["ingredient"] = None

        # Create a new Nutrition from the multiplied values
        tot = Nutrition(**tot_vals)
        return tot

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        try:
            other = float(other)
        except ValueError:
            raise TypeError("Nutrition can only be divided a number")

        return self.__mul__(1.0 / other)
    """
