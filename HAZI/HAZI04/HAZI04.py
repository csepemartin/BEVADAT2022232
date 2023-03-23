# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
'''
FONTOS: Az első feladatáltal visszaadott DataFrame-et kell használni a további feladatokhoz. 
A függvényeken belül mindig készíts egy másolatot a bemenő df-ről, (new_df = df.copy() és ezzel dolgozz tovább.)
'''

# %%
'''
Készíts egy függvényt, ami egy string útvonalat vár paraméterként, és egy DataFrame ad visszatérési értékként.

Egy példa a bemenetre: 'test_data.csv'
Egy példa a kimenetre: df_data
return type: pandas.core.frame.DataFrame
függvény neve: csv_to_df
'''

# %%
def csv_to_df(string : str):
    return pd.read_csv(string)


# %%
'''
Készíts egy függvényt, ami egy DataFrame-et vár paraméterként, 
és átalakítja azoknak az oszlopoknak a nevét nagybetűsre amelyiknek neve nem tartalmaz 'e' betüt.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_capitalized
return type: pandas.core.frame.DataFrame
függvény neve: capitalize_columns
'''

# %%
def capitalize_columns(df_data):
    new_df=df_data.copy()
    return new_df.rename(lambda x : x.capitalize() if ('e' in x) else x, axis = 1)
    


# %%
'''
Készíts egy függvényt, ahol egy szám formájában vissza adjuk, hogy hány darab diáknak sikerült teljesíteni a matek vizsgát.
(legyen az átmenő ponthatár 50).

Egy példa a bemenetre: df_data
Egy példa a kimenetre: 5
return type: int
függvény neve: math_passed_count
'''

# %%
def math_passed_count(df_data):
    new_df=df_data.copy()
    passed = new_df[new_df['math score'] >= 50]
    return len(passed)
    

# %%
'''
Készíts egy függvényt, ahol Dataframe ként vissza adjuk azoknak a diákoknak az adatait (sorokat), akik végeztek előzetes gyakorló kurzust.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_did_pre_course
return type: pandas.core.frame.DataFrame
függvény neve: did_pre_course
'''

# %%
def did_pre_course(df_data):
    new_df=df_data.copy()
    return new_df[new_df['test preparation course'] == 'completed']

# %%
'''
Készíts egy függvényt, ahol a bemeneti Dataframet a diákok szülei végzettségi szintjei alapján csoportosításra kerül,
majd aggregációként vegyük, hogy átlagosan milyen pontszámot értek el a diákok a vizsgákon.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_average_scores
return type: pandas.core.frame.DataFrame
függvény neve: average_scores
'''

# %%
def average_scores(df_data):
    new_df=df_data.copy()
    keys = ['math score','reading score','writing score']
    return new_df.groupby('parental level of education')[keys].mean()

# %%
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'age' oszloppal, töltsük fel random 18-66 év közötti értékekkel.
A random.randint() függvényt használd, a random sorsolás legyen seedleve, ennek értéke legyen 42.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_age
return type: pandas.core.frame.DataFrame
függvény neve: add_age
'''

# %%
def add_age(df_data):
    new_df=df_data.copy()
    np.random.seed(42)
    new_df['age'] = np.random.randint(18,66,new_df.shape[0])
    return new_df

# %%
'''
Készíts egy függvényt, ami vissza adja a legjobb teljesítményt elérő női diák pontszámait.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: (99,99,99) #math score, reading score, writing score
return type: tuple
függvény neve: female_top_score
'''

# %%
def female_top_score(df_data):
    new_df = df_data.copy()
    new_df['highscore'] = (new_df['math score'] + new_df['reading score'] + new_df['writing score'])
    new_df = new_df[new_df['gender'] == 'female']
    new_df = new_df.query('highscore == highscore.max()')
    tpl = (new_df.iloc[0]['math score'],new_df.iloc[0]['reading score'],new_df.iloc[0]['writing score'])
    return tpl

# %%
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'grade' oszloppal. 
Számoljuk ki hogy a diákok hány százalékot ((math+reading+writing)/300) értek el a vizsgán, és osztályozzuk őket az alábbi szempontok szerint:

90-100%: A
80-90%: B
70-80%: C
60-70%: D
<60%: F

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_grade
return type: pandas.core.frame.DataFrame
függvény neve: add_grade
'''




# %%
def add_grade(df_data):
    new_df=df_data.copy()
    new_df['percantage'] = (new_df['math score'] + new_df['reading score'] + new_df['writing score'])/300
    new_df['grade'] = pd.cut(new_df['percantage'], bins=[0, 0.6, 0.7, 0.8, 0.9, 1.0], labels=['F', 'D', 'C', 'B', 'A'])
    del new_df['percantage']
    return new_df

# %%
'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlop diagrammot,
ami vizualizálja a nemek által elért átlagos matek pontszámot.

Oszlopdiagram címe legyen: 'Average Math Score by Gender'
Az x tengely címe legyen: 'Gender'
Az y tengely címe legyen: 'Math Score'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: math_bar_plot
'''

# %%
def math_bar_plot(df_data):
    new_df=df_data.copy()
    avg_score = new_df.groupby('gender')['math score'].mean()
    fig, ax =plt.subplots()
    ax.bar(avg_score.index,avg_score.values)
    ax.set_title('Average Math Score By Gender')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Math Score')
    return fig

# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan histogramot,
ami vizualizálja az elért írásbeli pontszámokat.

A histogram címe legyen: 'Distribution of Writing Scores'
Az x tengely címe legyen: 'Writing Score'
Az y tengely címe legyen: 'Number of Students'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: writing_hist
'''

# %%
def writing_hist(df_data):
    new_df=df_data.copy()
    fig, ax =plt.subplots()
    ax.hist(new_df['writing score'])
    ax.set_title('Distribution of Writing Scores')
    ax.set_xlabel('Writing Score')
    ax.set_ylabel('Number of Students')
    return fig
    

# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja a diákok etnikum csoportok szerinti eloszlását százalékosan.

Érdemes megszámolni a diákok számát, etnikum csoportonként,majd a százalékos kirajzolást az autopct='%1.1f%%' paraméterrel megadható.
Mindegyik kör szelethez tartozzon egy címke, ami a csoport nevét tartalmazza.
A diagram címe legyen: 'Proportion of Students by Race/Ethnicity'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: ethnicity_pie_chart
'''

# %%
def ethnicity_pie_chart(df_data):
    new_df=df_data.copy()
    proportion = new_df.pivot_table(index = ['race/ethnicity'], aggfunc ='size')
    fig, ax =plt.subplots()
    ax.pie(proportion.values,labels=proportion.index)
    ax.set_title('Proportion of Students by Race/Ethnicity')
    return fig
