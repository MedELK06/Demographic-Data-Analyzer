import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read dataset, skip initial spaces after commas
    df = pd.read_csv(
        "adult.data.csv",
        header=None,
        names=[
            'age', 'workclass', 'fnlwgt', 'education', 'education-num',
            'marital-status', 'occupation', 'relationship', 'race', 'sex',
            'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
        ],
        skipinitialspace=True
    )

    # 1. How many people of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage of people with Bachelors
    percentage_bachelors = round(100 * (df['education'] == 'Bachelors').mean(), 1)

    # 4-5. Percentage with/without advanced education earning >50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education
    higher_education_rich = round(100 * df[higher_education]['salary'].eq('>50K').mean(), 1)
    lower_education_rich = round(100 * df[lower_education]['salary'].eq('>50K').mean(), 1)

    # 6. Minimum hours per week
    # 6. Minimum hours per week
    min_work_hours = int(df['hours-per-week'].min())


    # 7. Percentage of rich among those who work minimum hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(100 * num_min_workers['salary'].eq('>50K').mean(), 1)

    # 8. Country with highest percentage of >50K earners
    country_counts = df['native-country'].value_counts()
    country_rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    highest_earning_country_percentage = round(100 * (country_rich_counts / country_counts).max(), 1)
    highest_earning_country = (country_rich_counts / country_counts).idxmax()

    # 9. Top occupation in India among >50K
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # PRINT RESULTS
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education earning >50K: {higher_education_rich}%")
        print(f"Percentage without higher education earning >50K: {lower_education_rich}%")
        print("Minimum work hours per week:", min_work_hours)
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich in country:", highest_earning_country_percentage)
        print("Top occupation in India among rich:", top_IN_occupation)

    # RETURN RESULTS
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
