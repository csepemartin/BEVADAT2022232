from DecisionTreeClassifier import DecisionTreeClassifier
from NJCleaner import NJCleaner
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd


nj = NJCleaner('./2018_03.csv')
nj.prep_df()
data = nj.prep_df()
col_name = ['stop_sequence','from_id','to_id','status','line','type','day','part_of_the_day','delay']
data = pd.read_csv("./data/NJ.csv",skiprows=1, header=None, names=col_name)


X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values.reshape(-1,1)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=.2, random_state=41)

classifier = DecisionTreeClassifier(min_samples_split=100, max_depth=7)
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)
print(accuracy_score(Y_test, Y_pred))


#min_samples_split=2, max_depth=3 => accuracy=0.7839166666666667
#min_samples_split=2, max_depth=4 => accuracy=0.7849166666666667
#min_samples_split=1, max_depth=1 => accuracy=0.7773333333333333
#min_samples_split=2, max_depth=3 => accuracy=0.7839166666666667
#min_samples_split=2, max_depth=4 => accuracy=0.7849166666666667
#min_samples_split=3, max_depth=3 => accuracy=0.7839166666666667
#min_samples_split=3, max_depth=5 => accuracy=0.7885833333333333
#min_samples_split=3, max_depth=6 => accuracy=0.7885
#min_samples_split=3, max_depth=7 => accuracy=0.7934166666666667
#min_samples_split=5, max_depth=7 => accuracy=0.7934166666666667
#min_samples_split=10, max_depth=7 => 0.7935
#min_samples_split=20, max_depth=7 => 0.7936666666666666
#min_samples_split=100, max_depth=7 => 0.7940833333333334
#min_samples_split=1000, max_depth=7 => 0.7856666666666666



#A házi feladat első része az NJCleaner könnyedén ment.A másidok részhez már nehezebb volt megértenem hogyan is működik a DecisionTreeClassifier.
#A fitelést az órai példához hasonló min_sample_split és max_depth értékekkel kezdtem.
#Először a két érték csökkentésével próbálkoztam de nagyon kis értékeknél egyre pontatlanabb lett.
#Ezután elkezdtem növelni a két paramétert elöször kicsi majd egyre nagyobb mértékkel.A min_samples_split növelésével nőtt a pontosság is.
#Viszont túl nagy min_samples_split-nél elkezd csökkenni a pontosság.
#(100,7) értékekkel értem el a legnagyobb pontosságot.
