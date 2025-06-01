clear


capture cd "data"
use all_demographic.dta



* Generate dummy variables for all categorical variables
* Age group dummies
gen age_15_24 = 0
replace age_15_24 = 1 if age == "15 to 24"
gen age_25_34 = 0
replace age_25_34 = 1 if age == "25 to 34"
gen age_35_44 = 0
replace age_35_44 = 1 if age == "35 to 44"
gen age_45_54 = 0
replace age_45_54 = 1 if age == "45 to 54"
gen age_55_64 = 0
replace age_55_64 = 1 if age == "55 to 64"
gen age_over_65 = 0
replace age_over_65 = 1 if age == "Over 65"

gen age_below_25  = 0
replace age_below_25 = 1 if age_15_24 == 1
gen age_above_55 = 0
replace age_above_55 = 1 if age_55_64 == 1 | age_over_65 ==1

* Gender dummies
gen gender_female = 0
replace gender_female = 1 if gender == "Female"
gen gender_male = 0
replace gender_male = 1 if gender == "Male"

* Education dummies
gen education_bachelor = 0
replace education_bachelor = 1 if education == "Bachelor"
gen education_below_secondary = 0
replace education_below_secondary = 1 if education == "Below lower secondary"
gen education_graduate = 0
replace education_graduate = 1 if education == "Graduate"
gen education_lower_secondary = 0
replace education_lower_secondary = 1 if education == "Lower secondary"
gen education_short_cycle_tertiary = 0
replace education_short_cycle_tertiary = 1 if education == "Short-cycle tertiary"
gen education_upper_secondary = 0
replace education_upper_secondary = 1 if education == "Upper secondary"


gen below_secondary = 0
replace below_secondary = 1 if education_below_secondary == 1 | education_lower_secondary == 1 | education_upper_secondary == 1




* Marital status dummies
gen marital_divorced = 0
replace marital_divorced = 1 if maritalstatus == "Divorced"
gen marital_married = 0
replace marital_married = 1 if maritalstatus == "Married"
gen marital_never_married = 0
replace marital_never_married = 1 if maritalstatus == "Never married"
gen marital_widowed = 0
replace marital_widowed = 1 if maritalstatus == "Widowed"

* Location dummies
gen location_rural = 0
replace location_rural = 1 if location == "Rural"
gen location_urban = 0
replace location_urban = 1 if location == "Urban"

* Sexual orientation dummies
gen sexual_asexual = 0
replace sexual_asexual = 1 if sexualorientation == "Asexual"
gen sexual_bisexual = 0
replace sexual_bisexual = 1 if sexualorientation == "Bisexual"
gen sexual_heterosexual = 0
replace sexual_heterosexual = 1 if sexualorientation == "Heterosexual"
gen sexual_homosexual = 0
replace sexual_homosexual = 1 if sexualorientation == "Homosexual"

gen sexual_minority = 0 
replace sexual_minority = 1 if sexual_heterosexual == 0

* Disability dummies
gen disability_able_bodied = 0
replace disability_able_bodied = 1 if disability == "able-bodied"
gen disability_physical = 0
replace disability_physical = 1 if disability == "physically-disabled"

* Race dummies
gen race_african = 0
replace race_african = 1 if race == "African"
gen race_asian = 0
replace race_asian = 1 if race == "Asian"
gen race_caucasian = 0
replace race_caucasian = 1 if race == "Caucasian"
gen race_hispanic = 0
replace race_hispanic = 1 if race == "Hispanic"
* Religion dummies
gen religion_atheist = 0
replace religion_atheist = 1 if religion == "Atheist"
gen religion_christian = 0
replace religion_christian = 1 if religion == "Christian"
gen religion_jewish = 0
replace religion_jewish = 1 if religion == "Jewish"
gen religion_religious_other = 0
replace religion_religious_other = 1 if religion == "Religious"


* Political affiliation dummies
gen political_obama_supporter = 0
replace political_obama_supporter = 1 if politicalaffiliation == "Barack Obama Supporter"
gen political_trump_supporter = 0
replace political_trump_supporter = 1 if politicalaffiliation == "Donald Trump Supporter"
gen political_democrat = 0
replace political_democrat = 1 if politicalaffiliation == "lifelong Democrat"
gen political_republican = 0
replace political_republican = 1 if politicalaffiliation == "lifelong Republican"

global independent_vars age_15_24 age_35_44 age_45_54 age_55_64 age_over_65 gender_female education_bachelor education_below_secondary education_graduate education_lower_secondary education_upper_secondary marital_divorced marital_never_married marital_widowed location_rural sexual_asexual  sexual_bisexual sexual_homosexual disability_physical race_african race_asian race_hispanic religion_atheist religion_jewish religion_religious_other political_obama_supporter political_trump_supporter  political_republican


global independent_vars_new age_below_25 age_above_55 gender_female education_graduate below_secondary marital_divorced marital_married marital_widowed location_rural sexual_asexual sexual_bisexual sexual_homosexual disability_physical race_african race_asian race_hispanic religion_atheist religion_christian religion_jewish political_obama_supporter political_trump_supporter political_republican

tab model



encode model, gen(model_id) 
label list model_id 

local model_names GPT4o Qwen32B THUDM GlmDeepSeek deepseek_reasoner GoogleGemma InternLM MetaLlama405B MetaLlama8B GPTo1

levelsof model_id, local(models) 
local i = 1 

foreach m of local models { 
    local model_name : word `i' of `model_names' 
    reg tau $independent_vars_new if model_id == `m' 
    est store `model_name' 
    local i = `i' + 1 

	


esttab * using "regression_results.csv", replace ///
    cells(b se p) 
	
esttab * using "regression_results_plot.csv", replace ///
   cells(b se p)


	








