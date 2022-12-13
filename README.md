# Proyecto-Fisica Computacional
INTRODUCCIÓN

Las señales Electromiográficas (EMG) son fuente de información muy apropiada para el control de dispositivos virtuales como las prótesis de brazo y para analizar el comportamiento muscular ante diversas patologías. Las señales EMG superficiales (EMGs), son esencialmente un patrón unidimensional, por lo que cualquier técnica de procesamiento de señales para extracción de características y reconocimiento de patrones se puede aplicar a este tipo de señales. [1] 
Las señales EMGS son colectadas típicamente mediante electrodos bipolares de superficie, ubicados sobre la piel, estas han sido utilizadas para el control de prótesis de miembros superiores desde 1948 [2]

OBJETIVOS
Diseñar un ‘codigo’ capaz de modificar la señal del biopotencial muscular para la implementación en una prótesis de brazo.

  OBJETIVOS ESPECIFICOS 
  Obtención y lectura en Código del biopotencial muscular 
  Diseñar e Implementar un Código capaz de aplicar la transformada de Fourier 
  Lectura e Interpretación de la señal del biopotencial obtenida después de aplicarle el Código diseñado para su aplicación en protesis de brazo.


DESARROLLO

Las señales EMGS son generadas por la contracción muscular, por lo que su adquisición requiere de una correcta identificación de las regiones musculares comprometidas en la ejecución de los movimientos a clasificar. La adquisición de señales EMGS se realizo con un prototipo de un electromiografo, estas señales recogidas llevan un un procesamiento previo debido a su naturaleza, por lo que se hace necesario un previo de filtraje y amplificación antes de su análisis. 
En este caso nuestro prototipo del electro miógrafo realiza dos amplificaciones, una demodulación y un filtrado de frecuencias bajas, dándonos como resultado una señal aproximadamente de 5 volt limpia y con un mínimo ruido.
A esta señal obtenida con el electro miógrafo se le aplicara la transformada de Fourier con la finalidad de….




