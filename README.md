# Ratio Similarity

Teniendo dos conjuntos de datos cargados en gvSIG:
- mpol: una capa cargada en una Vista
- m1: una tabla

Se busca conseguir la unión entre ambas tablas pero eligiendo la selección según la proximidad de un valor.

Esta formula se utilizará en la Calculadora de campos y se aplicará sobre una columna nueva. Se ejecutará sobre la capa 'mpol'.

1. Accedeer a un store desde las expresiones:

<pre>
FEATURES('m1')
</pre>

2. Para realizar la unión se buscará la similitud entre dos valores para realizar el enlace, quedandose con el más parecido.

Se utilizará la función RATIOSIM(A, B). Este calcula la similitud entre dos numeros o entre dos string. Cuanto más parecidos los valores, mayor será la similitud.

Devuelve un valor entre 0 y 1.

Ejemplo:
<pre>
RATIOSIM( 100, 99 ) -> 0.99
RATIOSIM( 99, 100 ) -> 0.99
RATIOSIM( 1578, 1301 ) -> 0.824461..
RATIOSIM( 'aaa', 'aab' ) -> 0.82
RATIOSIM( 'aaa', 'abc' ) -> 0.56
</pre>

3. La comparación se puede realizar comparando diferentes campos. Para ello se puede utilizar la función SUMPRODUCT() que realizará una suma entre dos listas multiplandola por otra lista con los valores de peso.

Ejemplo:

<pre>
SUMPRODUCT(
  LIST(
     99,
     70,
     55),
  LIST(
    0.7,
    0.2,
    0.1)
)
--> 88.8
</pre>

4. Para seleccionar la entidad más parecido utilizaremos la función MAX().

En esta funcion recorreremos un store y iremos calculando el valor según una expresión de cada uno. La función calcula el feature que cumple el máximo según ese valor. Devuelve o el mismo valor calculado, o si hay una según expresión establecida el resultado de ejecutar esa expresión sobre el feature

Ejemplo:

<pre>
MAX(FEATURES('m1'),'k',
  'SUMPRODUCT(
     LIST(
       RATIOSIM(k.get(''SAREA''), AREA),
       RATIOSIM(k.get(''SAREA''), AREA),
       RATIOSIM(k.get(''SAREA''), AREA)
     ),
     LIST(
         0.5,
         0.3,
         0.2
       )
   )'
, 'k.get(''CAMPO1'')'
)
</pre>

