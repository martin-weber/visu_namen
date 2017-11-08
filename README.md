# Visualisierung der aktuellen Zürcher Wohnbevölkerung

Dieses Projekt wurde im Rahmen der Projektarbeit im Modul Visualisierung des CAS Data Science Applications an der [ZHAW](http://www.zhaw.ch) erstellt.
Das Frontend wurde mit D3.JS und Angular-Material aufgebaut.
Für das Backend wird eine Flask Applikation mit SQLite-Datenbank verwendet.
Weitere Infos sind in der [Präsentation](https://github.com/martin-weber/visu_namen/blob/master/Pr%C3%A4sentation_mwe.pdf) zu finden.

![Barcharts](/images/barchart.png)
![Linecharts](/images/linechart.png)

Die Daten stammen von:
https://data.stadt-zuerich.ch/dataset/bev-bestand-vornamen-jahrgang-geschlecht

## Setup

```
cd static
npm install
python3 visu_namen.py
```