 
# Zusammenfassung

## Inhaltsangabe

## Tag 1

### Kommentare

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

### Variable & Typen

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

### Ausgabe

Um auf der Konsole (unter Windows CMD/CommandLine und unter Linux Terminal/Shell genannt) Text auszugeben wird der Befehl print() benötigt.

```python
name = "Max"
print("Hallo " + name + "!")
```

### Konvertierung

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

### Eingabe

Natürlich soll auch der Benutzer Eingaben machen können.

Bei der Funktion "input()", kann in der Klammer angegeben werden, was unmittelbar vor der Eingabe stehen soll.

```python
# Bei String-Eingaben:
name = input("Ihr Name: ")
alter = int(input("Ihr Alter: "))

# ...
```

### Verzweigung

Etwas häufiger werden Verzeigungen benötigt.
Bsp.: Wenn ich müde bin, dann gehe ich schlafen.

> Vergleichsoperatoren:
> <
> <=
> ==
> !=
> \>=
> \>

## Tag 2

## Tag 3

## Tag 4

## Tag 5

## Tag 6

## Tag 7

## Tag 8


