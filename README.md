 
# Zusammenfassung

## Vorwort

Der Quellcode ist während dem Kurs "Python" von SmartNinja entstanden.<br/>
Kursstart: 16.04.2020.<br/>
SmartNinja [Webseite](https://www.smartninja.org/)<br/>
Die Pythondateien sind in den Ordnern "_uebung" und "_unterricht" aufgeteilt.

## Inhaltsangabe
[Kommentare | einzeilige u. mehrzeilige](#Kommentare)<br/>
[Variable | Deklaration und Initalisierung](#Variable)<br/>
[Ausgabe | print()](#Ausgabe)<br/>
[Konvertierung | int(), str(), ...](#Konvertierung)<br/>
[Eingabe | input()](#Eingabe)<br/>
[Verzweigung | if, elif, else](#Verzweigung)<br/>

## Tag 1 - 16.06.2020

### <a name="Kommentare"></a>Kommentare

Kommentare sind für die Entwickler, um sich Notizen zum Code zu machen. Diese werden vom Interpreter (beim ausführen) ignoriert.
Zum Testen wird auch manchmal eine Codezeile oder ein ganzer Block auskommentiert. Der Vorteil ist, dass der Code an Ort und Stelle stehen bleiben kann und nicht ausgeschnitten werden muss, sondern nur auskommentiert wird.

Einzeilige Kommentare:
```python
# Das ist ein Kommentar
...
x = 2 # Hier wird eine Variable angelegt und zugewiesen
```

Mehrzeilige Kommentare:
```python
"""
Hier steht ein
etwas längerer
Text
"""
```

### <a name="Variable"></a>Variable & Typen

Folgende Typen gibt es:
| Englisch | Deutsch | Beispiel |
|---|---|---|
| Integer | Ganze Zahl | 3 |
| Float | Kommazahl | 10.2 |
| String | Zeichenkette | "Ich liebe meine 4 kinder und den Burschen" |
| Boolean | Wahrheitswert | True oder False |
| List | Liste | ["Hy", 2, 2.4, False, 4]

Deklarieren und Initalisieren:
```python
x = 3	# x  -> deklarieren/anlegen
	# =3 -> initalisieren/zuweisen

vorname = "Markus"

maennlich = True

gewicht = 78.3
```

### <a name="Ausgabe"></a>Ausgabe

Um auf der Konsole (unter Windows CMD/CommandLine und unter Linux Terminal/Shell genannt) Text auszugeben wird der Befehl print() benötigt.

```python
name = "Max"
print("Hallo " + name + "!")
```

### <a name="Konvertierung"></a>Konvertierung

Um einen Typ von einer Variable (Wert) zu ändern ist es nötig diesen zu Konvertieren.

```python
x = 3
x_als_text = str(x)
x_als_float = float(x)

text = 123
zahl = int(123)

# In der Ausgabe eine Berechnung und somit auch eine Konvertierung in einem String:
zahl_1 = 5
zahl_2 = 3
print(zahl_1 + " + " + zahl_2 + " = " + str(zahl_1 + zahl_2))
# Ausgabe: 5 + 3 = 8
```

### <a name="Eingabe"></a>Eingabe

Natürlich soll auch der Benutzer Eingaben machen können.

Bei der Funktion "input()", kann in der Klammer angegeben werden, was unmittelbar vor der Eingabe stehen soll.

```python
# Bei String-Eingaben:
name = input("Ihr Name: ")

# Bei Int-Eingabe:
alter = int(input("Ihr Alter: "))

# ...
```

### <a name="Verzweigung"></a>Verzweigung

Etwas häufiger werden Verzeigungen benötigt.
Bsp.: Wenn ich müde bin, dann gehe ich schlafen.

Vergleichsoperatoren:
| Schreibweise | gesprochen |
|---|---|
| < | kleiner |
| <= | kleiner gleich |
| == | gleich |
| != | ungleich |
| >= | größer gleich |
| > | größer |

Boolsche Operatoren:
| Schreibweise | gesprochen |
|---|---|
| and | und |
| or | oder |
| is | gleiches Objekt |
| is not | ungleiches Objekt |
| not | nicht |
 
```python
secret = 1234
eingabe = int(input("Raten Sie eine Zahl: "))

if eingabe < secret :
  print("Ihre Eingabe war zu klein")
elif eingabe == secret :
  print("Perfekt! Erraten.")
else:
  print("Ihre Eingabe war zu groß")

hunger = True
bin_daheim = False

if hunger == True and bin_daheim == True:
  print("Gehe bitte zum Kühlschrenk")
elif hunger == True and bin_daheim == False:
  print("Hole dir was vom Supermarkt")
else:
  print("Kein Handlungsbedarf")
```

## Tag 2

## Tag 3

## Tag 4

## Tag 5

## Tag 6

## Tag 7

## Tag 8


