def cleaner():
    """ Python hat Schwierigkeiten Umlaute zu verarbeiten. Diese werden ersetzt durch "e", "ue" und "ae". Weiterhin werden aus darstellungsgründen \n und \r durch ein Leerzeichen ersetzt. Bei re.compile werden die 2 Leerzeichen vor und nach dem String durch ein Leerzeichen ersetzt."""
def gettheduckingstring(tostring):
    """ Die Strings sind verschieden codiert. Entweder in UTF-8 oder binary values. Bei UTF-8 braucht es keine decodierung. Mit dieser Funktion wird der String so decodiert, \n dass mit ihm weiter gearbeitet werden kann."""
def lister(tolist,whichitem=0):
    """ Es wird eine Liste erstellt, aus den jeweiligen ersten Elementen, einer Liste bestehend aus Listen.""" 
def getcont(text,price=False):
    """ Hier werden aus der Strings die jeweiligen Zahlenwerte entnommen. Präfixe wie kg, PS oder CHF werden nicht berücksichtigt. Weiterhin wird auch überprüft ob ein Preis vorhanden ist. \n Auktionen beinhalten keinen Preis. Somit werden diese Autionen herausgefiltert."""
def getverb(toverb):
    """Der Verbrauch ist im Gegensatz zu den anderen numerischen Werten komplizierter dargestellt. Die Darstellung sieht folgendermassen aus: 'zahl/zahl/zahl(st/land/tot)'. \n Der String wird bei "\" getrennt. Davon wird dann der 3. Wert genommen. Dieser sieht folgendermassen aus: 'zahl(st'. Danach folgt ein Split bei der Klammer. \n Am Schluss wird der 1. Wert, der totale Verbrauch, genommen. """
class run():
    """Hier werden alle Attribute gesucht und herausgelesen aus den Strings. Dabei wird immer überprüft wie der String codiert ist. Falls nötig wird decodiert. \n Beim "ricardo_scraping_1.py" wird das Decodieren nicht benötigt."""
def createdb():
    """Hier wird die Datenbank erstellt. Da mehrere Durchgänge nötig sind, wird mit c.execute("drop table cars") die alten Daten gelöscht. So gibt es keine mehrfaches Aufkommen der selben Datei. \n Mit "CREATE TABLE CARS" wird eine DB mit den darunter aufgeführten Begriffen erstellt. """ 
def showcount():
    """ Zeigt an wie viele Elemente heruntergeladen worden sind."""
def getbrand(artname):
    """ Hier werden die Marken beschaffen. Dabei werden die Marken mit der "filter"-Liste abgeglichen. Nur die Marken welche sich in der "Filter"-Liste befinden werden aus den Strings entnommen."""
def getmodel(car, artname):
    """ Mit dieser Funktion wird die Marke aus den Strings geholt."""
def computeCost(X,y,theta):
    """Cost function wird berechnet."""
def gradientDescent(X,y,theta,iters,alpha):
    """Das gradienten Verfahren wird definiert."""
