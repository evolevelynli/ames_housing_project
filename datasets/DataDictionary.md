# Codebook / Data Dictionary:

|SalePrice - the property's sale price in dollars. This is the target variable that you're trying to predict for this |challenge.

|Variable Name|Definition                                  |Data Type|Treatment|
|-------------|-----------------                           |-----------|-----|
|MSSubClass|The building class  |---|---|
|20  |1-STORY 1946 & NEWER ALL STYLES                      |Categorical||
|30  |1-STORY 1945 & OLDER                                 |Categorical||
|40  |1-STORY W/FINISHED ATTIC ALL AGES                    |Categorical||
|45  |1-1/2 STORY - UNFINISHED ALL AGES                    |Categorical||
|50  |1-1/2 STORY FINISHED ALL AGES                        |Categorical||
|60  |2-STORY 1946 & NEWER                                 |Categorical||
|70  |2-STORY 1945 & OLDER                                 |Categorical||
|75  |2-1/2 STORY ALL AGES                                 |Categorical||
|80  |SPLIT OR MULTI-LEVEL                                 |Categorical||
|85  |SPLIT FOYER                                          |Categorical||
|90  |DUPLEX - ALL STYLES AND AGES                         |Categorical||
|120 |1-STORY PUD (Planned Unit Development) - 1946 & NEWER|Categorical||
|150 |1-1/2 STORY PUD - ALL AGES                           |Categorical||
|160 |2-STORY PUD - 1946 & NEWER                           |Categorical||
|180 |PUD - MULTILEVEL - INCL SPLIT LEV/FOYER              |Categorical||
|190 |2 FAMILY CONVERSION - ALL STYLES AND AGES            |Categorical||



|Variable Name|Definition|Data Type|Treatment|
|------------------------------|---------|---------|
|MSZoning| Identifies the general zoning classification of the sale.|---|---|
|A |Agriculture                                            |Categorical|Dummy|
|C |Commercial                                             |Categorical|Dummy|
|FV |Floating Village Residential                          |Categorical|Dummy|
|I |Industrial                                             |Categorical|Dummy|
|RH |Residential High Density                              |Categorical|Dummy|
|RL |Residential Low Density                               |Categorical|Dummy|
|RP |Residential Low Density Park                          |Categorical|Dummy|
|RM |Residential Medium Density                            |Categorical|Dummy|


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|LotFrontage|Linear feet of street connected to property   |numerical|integer|
|LotArea|size in square feet                               |numerical|integer|

|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|Street| Type of road access to property|---|---|
|Grvl| Gravel                                              |Categorical|Dummy| 
|Pave| Paved


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|Alley|: Type of alley access to property                  |Categorical|Dummy|
|Grvl| Gravel                                              |Categorical|Dummy|
|Pave| Paved                                               |Categorical|Dummy|
|NA| No alley access                                       |Categorical|Dummy|


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|LotShape|General shape of property|---|-----|
|Reg| Regular                                              |Categorical|Dummy|
|IR1| Slightly irregular                                   |Categorical|Dummy|
|IR2| Moderately Irregular                                 |Categorical|Dummy|
|IR3| Irregular                                            |Categorical|Dummy|

|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|LandContour|Flatness of the property|---|---|                      
|Lvl| Near Flat/Level                                                  |Categorical|Dummy|
|Bnk| Banked - Quick and significant rise from street grade to building|Categorical|Dummy|
|HLS| Hillside - Significant slope from side to side                   |Categorical|Dummy|
|Low| Depression                                                       |Categorical|Dummy|


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|Utilities: Type of utilities available                    |Categorical|Dummy|
|AllPub| All public Utilities (E,G,W,& S)                  |Categorical|Dummy|
|NoSewr| Electricity, Gas, and Water (Septic Tank)         |Categorical|Dummy|
|NoSeWa| Electricity and Gas Only                          |Categorical|Dummy|
|ELO   | Electricity only                                  |Categorical|Dummy|


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|LotConfig|: Lot configuration|----|---------|
|Inside   | Inside lot                                     |Categorical|Dummy|
|Corner   | Corner lot                                     |Categorical|Dummy|
|CulDSac  | Cul-de-sac                                     |Categorical|Dummy|
|FR2      | Frontage on 2 sides of property                |Categorical|Dummy|
|FR3      | Frontage on 3 sides of property                |Categorical|Dummy|


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|LandSlope:| Slope of property                             |Categorical|Dummy|
|Gtl       | Gentle slope                                  |Categorical|Dummy|
|Mod       | Moderate Slope                                |Categorical|Dummy|
|Sev       | Severe Slope                                  |Categorical|Dummy|


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|Neighborhood:| Physical locations within Ames city limits|---|---|
|Blmngtn| Bloomington Heights |Categorical|Dummy|
|Blueste| Bluestem                                         |Categorical|Dummy|
|BrDale | Briardale                                        |Categorical|Dummy|
|BrkSide| Brookside                                        |Categorical|Dummy|
|ClearCr| Clear Creek                                      |Categorical|Dummy|
|CollgCr| College Creek                                    |Categorical|Dummy|
|Crawfor| Crawford                                         |Categorical|Dummy|
|Edwards| Edwards                                          |Categorical|Dummy|
|Gilbert| Gilbert                                          |Categorical|Dummy|
|IDOTRR | Iowa DOT and Rail Road                           |Categorical|Dummy|
|MeadowV| Meadow Village                                   |Categorical|Dummy|
|Mitchel| Mitchell                                         |Categorical|Dummy|
|Names  | North Ames                                       |Categorical|Dummy|
|NoRidge| Northridge                                       |Categorical|Dummy|
|NPkVill| Northpark Villa                                  |Categorical|Dummy|
|NridgHt| Northridge Heights                               |Categorical|Dummy|
|NWAmes | Northwest Ames                                   |Categorical|Dummy|
|OldTown| Old Town                                         |Categorical|Dummy|
|SWISU  | South & West of Iowa State University            |Categorical|Dummy|
|Sawyer | Sawyer                                           |Categorical|Dummy|
|SawyerW| Sawyer West                                      |Categorical|Dummy|
|Somerst| Somerset                                         |Categorical|Dummy|
|StoneBr| Stone Brook                                      |Categorical|Dummy|
|Timber | Timberland                                       |Categorical|Dummy|
|Veenker| Veenker                                          |Categorical|Dummy|



|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|Condition1|: Proximity to main road or railroad|---|---|
|Artery    | Adjacent to arterial street                         |Categorical|Dummy|
|Feedr     | Adjacent to feeder street                           |Categorical|Dummy|
|Norm      | Normal                                              |Categorical|Dummy|
|RRNn      | Within 200' of North-South Railroad                 |Categorical|Dummy|
|RRAn      | Adjacent to North-South Railroad                    |Categorical|Dummy|
|PosN      | Near positive off-site feature--park, greenbelt, etc|Categorical|Dummy|
|PosA      | Adjacent to postive off-site feature                |Categorical|Dummy|
|RRNe      | Within 200' of East-West Railroad                   |Categorical|Dummy|
|RRAe      | Adjacent to East-West Railroad                      |Categorical|Dummy|




|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|Condition2:| Proximity to main road or railroad (if a second is present)|---|---|
|Artery| Adjacent to arterial street                          |Categorical|Dummy|
|Feedr | Adjacent to feeder street                            |Categorical|Dummy|
|Norm  | Normal                                               |Categorical|Dummy|
|RRNn  | Within 200' of North-South Railroad                  |Categorical|Dummy|
|RRAn  | Adjacent to North-South Railroad                     |Categorical|Dummy|
|PosN  | Near positive off-site feature--park, greenbelt, etc.|Categorical|Dummy|
|PosA  | Adjacent to postive off-site feature                 |Categorical|Dummy|
|RRNe  | Within 200' of East-West Railroad                    |Categorical|Dummy|
|RRAe  | Adjacent to East-West Railroad                       |Categorical|Dummy|




|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|BldgType:| Type of dwelling|---|---|
|1Fam     | Single-family Detached                                        |Categorical|Dummy|
|2FmCon   | Two-family Conversion; originally built as one-family dwelling|Categorical|Dummy|
|Duplx    | Duplex                                                        |Categorical|Dummy|
|TwnhsE   | Townhouse End Unit                                            |Categorical|Dummy|
|TwnhsI   | Townhouse Inside Unit                                         |Categorical|Dummy|




|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|HouseStyle:| Style of dwelling|Categorical|Dummy|
|1Story| One story|Categorical|Dummy|
|1.5Fin| One and one-half story: 2nd level finished|Categorical|Dummy|
|1.5Unf| One and one-half story: 2nd level unfinished|Categorical|Dummy|
|2Story| Two story|Categorical|Dummy|
|2.5Fin| Two and one-half story: 2nd level finished|Categorical|Dummy|
|2.5Unf| Two and one-half story: 2nd level unfinished|Categorical|Dummy|
|SFoyer| Split Foyer|Categorical|Dummy|
|SLvl| Split Level|Categorical|Dummy|




|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|OverallQual:| Overall material and finish quality
|10 | Very Excellent 
|9  | Excellent
|8  | Very Good
|7  | Good
|6  | Above Average
|5  | Average
|4  | Below Average
|3  | Fair
|2  | Poor
|1  | Very Poor


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|OverallCond:| Overall condition rating
|10| Very Excellent
|9| Excellent
|8| Very Good
|7| Good
|6| Above Average
|5| Average
|4| Below Average
|3| Fair
|2| Poor
|1| Very Poor

|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|YearBuilt:| Original construction date|Categoraical|Extract the year and build dummy variables|




|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|YearRemodAdd:| Remodel date (same as construction date if no remodeling or additions)|Categoraical|Extract the year and build dummy variables|





|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|RoofStyle:| Type of roof |Categorical||
|Flat| Flat               |Categorical||
|Gable| Gable             |Categorical||
|Gambrel| Gabrel (Barn)   |Categorical||
|Hip| Hip                 |Categorical||
|Mansard| Mansard         |Categorical||
|Shed| Shed               |Categorical||


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|RoofMatl:| Roof material             |Categorical|Dummy|
|ClyTile| Clay or Tile                |Categorical|Dummy|
|CompShg| Standard (Composite) Shingle|Categorical|Dummy|
|Membran| Membrane                    |Categorical|Dummy|
|Meta|l Metal                         |Categorical|Dummy|
|Roll| Roll                           |Categorical|Dummy|
|Tar&Grv| Gravel & Tar                |Categorical|Dummy|
|WdShake| Wood Shakes                 |Categorical|Dummy|
|WdShngl| Wood Shingles               |Categorical|Dummy|



|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|Exterior1st:| Exterior covering on house |---|---|
|AsbShng| Asbestos Shingles       |Categorical|Dummy|
|AsphShn| Asphalt Shingles        |Categorical|Dummy|
|BrkComm| Brick Common            |Categorical|Dummy|
|BrkFace| Brick Face              |Categorical|Dummy|
|CBlock | Cinder Block            |Categorical|Dummy|
|CemntBd| Cement Board            |Categorical|Dummy|
|HdBoard| Hard Board              |Categorical|Dummy|
|ImStucc| Imitation Stucco        |Categorical|Dummy|
|MetalSd| Metal Siding            |Categorical|Dummy|
|Other  | Other                   |Categorical|Dummy|
|Plywood| Plywood                 |Categorical|Dummy|
|PreCast| PreCast                 |Categorical|Dummy|
|Stone  | Stone                   |Categorical|Dummy|
|Stucco | Stucco                  |Categorical|Dummy|
|VinylSd| Vinyl Siding            |Categorical|Dummy|
|Wd Sdng| Wood Siding             |Categorical|Dummy|
|WdShing| Wood Shingles           |Categorical|Dummy|


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|Exterior2nd:| Exterior covering on house (if more than one material)
|AsbShng| Asbestos Shingles
|AsphShn| Asphalt Shingles
|BrkComm| Brick Common
|BrkFace| Brick Face
|CBlock | Cinder Block
|CemntBd| Cement Board
|HdBoard| Hard Board
|ImStucc| Imitation Stucco
|MetalSd| Metal Siding
|Other  | Other
|Plywood| Plywood
|PreCast| PreCast
|Stone  | Stone
|Stucco | Stucco
|VinylSd| Vinyl Siding
|Wd Sdng| Wood Siding
|WdShing| Wood Shingles


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
|MasVnrType:| Masonry veneer type
|BrkCmn| Brick Common
|BrkFace| Brick Face
|CBlock| Cinder Block
|None| None
|Stone| Stone



|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
MasVnrArea: Masonry veneer area in square feet



|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
ExterQual: Exterior material quality
Ex Excellent
Gd Good
TA Average/Typical
Fa Fair
Po Poor




|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
ExterCond: Present condition of the material on the exterior
Ex Excellent
Gd Good
TA Average/Typical
Fa Fair
Po Poor



|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
Foundation: Type of foundation
BrkTil Brick & Tile
CBlock Cinder Block
PConc Poured Contrete
Slab Slab
Stone Stone
Wood Wood




|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
BsmtQual: Height of the basement
Ex Excellent (100+ inches)
Gd Good (90-99 inches)
TA Typical (80-89 inches)
Fa Fair (70-79 inches)
Po Poor (<70 inches)
NA No Basement




|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
BsmtCond: General condition of the basement
Ex Excellent
Gd Good
TA Typical - slight dampness allowed
Fa Fair - dampness or some cracking or settling
Po Poor - Severe cracking, settling, or wetness
NA No Basement




|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
BsmtExposure: Walkout or garden level basement walls
Gd Good Exposure
Av Average Exposure (split levels or foyers typically score average or above)
Mn Mimimum Exposure
No No Exposure
NA No Basement




|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
BsmtFinType1: Quality of basement finished area
GLQ Good Living Quarters
ALQ Average Living Quarters
BLQ Below Average Living Quarters
Rec Average Rec Room
LwQ Low Quality
Unf Unfinshed
NA No Basement



|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
BsmtFinSF1: Type 1 finished square feet




|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
BsmtFinType2: Quality of second finished area (if present)
GLQ Good Living Quarters
ALQ Average Living Quarters
BLQ Below Average Living Quarters
Rec Average Rec Room
LwQ Low Quality
Unf Unfinshed
NA No Basement

|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
BsmtFinSF2: Type 2 finished square feet



|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
BsmtUnfSF: Unfinished square feet of basement area
TotalBsmtSF: Total square feet of basement area
Heating: Type of heating
Floor Floor Furnace
GasA Gas forced warm air furnace
GasW Gas hot water or steam heat
Grav Gravity furnace
OthW Hot water or steam heat other than gas
Wall Wall furnace



|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
HeatingQC: Heating quality and condition
Ex Excellent
Gd Good
TA Average/Typical
Fa Fair
Po Poor

|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
CentralAir: Central air conditioning
N No
Y Yes


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
Electrical: Electrical system
SBrkr Standard Circuit Breakers & Romex
FuseA Fuse Box over 60 AMP and all Romex wiring (Average)
FuseF 60 AMP Fuse Box and mostly Romex wiring (Fair)
FuseP 60 AMP Fuse Box and mostly knob & tube wiring (poor)
Mix Mixed




|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
1stFlrSF: First Floor square feet
2ndFlrSF: Second floor square feet
LowQualFinSF: Low quality finished square feet (all floors)
GrLivArea: Above grade (ground) living area square feet
BsmtFullBath: Basement full bathrooms
BsmtHalfBath: Basement half bathrooms
FullBath: Full bathrooms above grade
HalfBath: Half baths above grade
Bedroom: Number of bedrooms above basement level
Kitchen: Number of kitchens


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
KitchenQual: Kitchen quality
Ex Excellent
Gd Good
TA Typical/Average
Fa Fair
Po Poor

|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
TotRmsAbvGrd: Total rooms above grade (does not include bathrooms)


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
Functional: Home functionality rating
Typ Typical Functionality
Min1 Minor Deductions 1
Min2 Minor Deductions 2
Mod Moderate Deductions
Maj1 Major Deductions 1
Maj2 Major Deductions 2
Sev Severely Damaged
Sal Salvage only


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
Fireplaces: Number of fireplaces



|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
FireplaceQu: Fireplace quality
Ex Excellent - Exceptional Masonry Fireplace
Gd Good - Masonry Fireplace in main level
TA Average - Prefabricated Fireplace in main living area or Masonry Fireplace in basement
Fa Fair - Prefabricated Fireplace in basement
Po Poor - Ben Franklin Stove
NA No Fireplace



|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
GarageType: Garage location
2Types More than one type of garage
Attchd Attached to home
Basment Basement Garage
BuiltIn Built-In (Garage part of house - typically has room above garage)
CarPort Car Port
Detchd Detached from home
NA No Garage


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
GarageYrBlt: Year garage was built



|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
GarageFinish: Interior finish of the garage
Fin Finished
RFn Rough Finished
Unf Unfinished
NA No Garage


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
GarageCars: Size of garage in car capacity
GarageArea: Size of garage in square feet



|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
GarageQual: Garage quality
Ex Excellent
Gd Good
TA Typical/Average
Fa Fair
Po Poor
NA No Garage



|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
GarageCond: Garage condition
Ex Excellent
Gd Good
TA Typical/Average
Fa Fair
Po Poor
NA No Garage



|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
PavedDrive: Paved driveway
Y Paved
P Partial Pavement
N Dirt/Gravel


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
WoodDeckSF: Wood deck area in square feet
OpenPorchSF: Open porch area in square feet
EnclosedPorch: Enclosed porch area in square feet
3SsnPorch: Three season porch area in square feet
ScreenPorch: Screen porch area in square feet
PoolArea: Pool area in square feet


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
PoolQC: Pool quality
Ex Excellent
Gd Good
TA Average/Typical
Fa Fair
NA No Pool


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
Fence: Fence quality
GdPrv Good Privacy
MnPrv Minimum Privacy
GdWo Good Wood
MnWw Minimum Wood/Wire
NA No Fence



|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
MiscFeature: Miscellaneous feature not covered in other categories
Elev Elevator
Gar2 2nd Garage (if not described in garage section)
Othr Other
Shed Shed (over 100 SF)
TenC Tennis Court
NA None


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
MiscVal: $Value of miscellaneous feature

|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
MoSold: Month Sold


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
YrSold: Year Sold


|Variable Name|Definition|Data Type|Treatment|
|-------------|----------|---------|---------|
SaleType: Type of sale
WD Warranty Deed - Conventional
CWD Warranty Deed - Cash
VWD Warranty Deed - VA Loan
New Home just constructed and sold
COD Court Officer Deed/Estate
Con Contract 15% Down payment regular terms
ConLw Contract Low Down payment and low interest
ConLI Contract Low Interest
ConLD Contract Low Down
Oth Other
