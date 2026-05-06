# tp2-tda

## Lineamientos básicos.

- El trabajo se realizará en grupos de cuato o cinco personas.
- Un integrante del grupo deberá entregar el informe en formato pdf y los programas realizandos en nombre del grupo en el aula virtual de la materia.
- El código fuente debe incluirse dentro de arhivo “.zip”. El .zip no debe contener carpetas en su interior, si no, solo 2 archivos (“tp1_1.py” y “tp1_2.py”)
- El lenguaje de implementación a utilizar es Python. No está permitido utilizar librerías externas.
- Deben seguir el formato especificado a modo de plantilla en el siguiente repositorio https://github.com/TDA-Podberezski/tps/tree/main/2026-1c-tp2. Deben descargar los archivos e implementar su algoritmo dentro de la función “main” de cada módulo python.
- Se proporciona un archivo tests.py básico para comprobar que su función cumple con el formato adecuado. Opcionalmente pueden agregar tests adicionales para ayudar a comprobar que su algoritmo funciona correctamente
- El informe debe presentar carátula con el nombre del grupo, datos de los integrantes, fecha y número de entrega. Debe incluir número de hoja en cada página. No debe superar las 25 páginas + carátula + índice + referencias.
- Debe entregar en el informe las fuentes consultadas en una sección de referencias.
- En caso de re-entrega, entregar luego del informe original un apartado con las correcciones realizadas.

## Parte 1: La separación del dojo.

Un dojo dedicado a la enseñanza de Karate tiene “n” miembros. Dos de ellos, los profesores principales, no tienen una buena relación. Tanto así que se rumorea que probablemente terminen cerrando el dojo y cada uno armará el suyo propio. Cada uno de los miembros restantes deberá seleccionar si siguen con uno o con el otro. El dueño del establecimiento desea decidir a quién a quién de los dos le otorgará el lugar. No tiene preferencias, solo le gustaría que sea el que finalice con más integrantes. Para eso encargó a un investigador que averigüe cuáles son las relaciones entre miembros. Como resultado tiene un listado que dice cuántas veces se relacionaron pares de miembros durante el último mes. Cree que relaciones fuertes de grupos pueden hacer que estos se mantengan unidos en la división. En base a esta información desean estimar cuál de los dos profesores terminará con más seguidores.

**Se pide:**

1. Realizar una reducción polinomial del problema planteado a uno de redes de flujo.
2. Resolver el problema utilizando redes de flujo.
3. Realizar análisis de complejidad temporal y espacial.
4. Realice un ejemplo paso a paso de resolución. Utilice redes de flujo gráficas.
5. Analice: su propuesta realmente predecirá la división real? En base a esta, ¿puede una misma instancia tener diferentes soluciones? ¿Qué implicación tiene seleccionar una u otra?
6. Programar la solución.

### Formato de entrega del código

Generar un archivo tp2_1.py que contenga una función main que reciba: s_1 un entero positivo entre 1 y n representando a uno de los profesores principales s_2 un entero positivo entre 1 y n representando al otro de los profesores principales Una lista de a lo sumo n^2 tuplas, [(a, b, i)], con a, b siendo miembros del dojo a, b = (1, …, n) a != b, e “i” un entero positivo siendo la cantidad de veces se relacionaron a y b entre sí.

Y que retorna una tupla con dos conjuntos: Los miembros que se estima que seguirán con el profesor s_1 Los miembros que se estima que seguirán con el profesor s_2.

**Ejemplo de ejecución:** Para una entrada: s1 = 1 s2 = 4 relaciones = [(1, 2, 10), (1, 3, 1), (2, 3, 1), (2, 4, 1), (3, 4, 3)]

Una estimación posible sería ({1, 2}, {3, 4})

## Parte 2: El despacho de los productos.

Una empresa logística debe enviar “n” productos. Cada producto “i” tiene un tamaño “si“ y valor de envío “vi”. Dispone de “k” contenedores idénticos, cada uno con capacidad “C”. Un producto debe asignarse a lo sumo a un contenedor (puede decidir no enviarlo). La suma de los tamaños de los productos dentro de un mismo contenedor no puede superar su capacidad. El despacho de un contenedor con espacio vacío es penalizado económicamente mediante un factor “a” (valor por unidad de espacio no utilizado). Nos solicitan maximizar el valor total enviado (ganancia por los productos enviados menos la penalización de los espacios libres en los contenedores utilizados). La penalización se aplica únicamente sobre los contenedores que contienen al menos un producto. Nos sugieren que utilicemos la técnica más eficiente que conocen, Branch & Bound.

**Se pide:**

1. Explique brevemente su solución propuesta. Defina la función costo y límite. Explica cuando poda una rama.
2. Dar el pseudocódigo y estructuras de datos a utilizar.
3. Realice el análisis de complejidad temporal y espacial de la solución.
4. Brinde un ejemplo simple paso a paso del funcionamiento de la solución.
5. Programe la solución.

### Formato de entrega del código.

Generar un archivo tp2_2.py que contenga una función main que reciba: Un listado de n tuplas [(s_1, v_1) …, (s_n, v_n)], representando s_i el tamaño de cada producto, y v_i su valor; Un entero positivo “k” de la cantidad de contenedores disponibles Un número positivo “C”, la capacidad de cada contenedor El factor “a” de penalización por no llenar un contenedor Y que retorne una tupla con dos miembros: Un número G representando la ganancia máxima posible de obtener Una lista de conjuntos [l_1, …, l_k], siendo l_i una lista con elementos {l_i1, … l_im}, cada l_ij representando el índice del producto en la lista “n” a incluir en el contenedor “i” que genera esa ganancia máxima G.

**Ejemplo de ejecución:** Para una entrada: n = [(2, 10), (5, 10), (7, 20)], k = 2, c = 8, a = 5

Una respuesta posible sería (30, [{0, 1}, {2}])

Otra respuesta posible sería (30, [{2}, {0, 1}])

## Parte 3: Los centros de atención.

Una empresa de servicios planea instalar centros de atención para cubrir distintas zonas de la ciudad. Se dispone de:

- Un conjunto de posibles ubicaciones para centros F.
- Un conjunto de zonas Z que deben ser atendidas.

Cada centro j ∈ F tiene un costo fijo de instalación cj. Cada zona i ∈ Z puede ser atendida únicamente por ciertos centros (por restricciones geográficas y logísticas). Esta información se provee como, para cada zona, el subconjunto de centros que pueden atenderla. Cada zona debe ser atendida por un centro. No deben quedar zonas sin atender. El objetivo es seleccionar qué centros instalar y asignar cada zona a un centro instalado, minimizando el costo total de instalación.

**Se pide:**

1. Demostrar que el problema es NP-Hard mediante una reducción polinomial utilizando Set Cover (considerar que set cover es un problema de decisión al momento de realizar la reducción).
2. Que debería modificar en el enunciado para convertirlo en un problema de decisión?
3. Demostrar que la versión de decisión pertenece a NP.
4. Demuestre que la versión de decisión pertenece a NP-Completo.
5. Una persona afirma tener un método eficiente (polinomial) para obtener la solución al problema de optimización cualquiera sea la instancia. Utilizando el concepto de transitividad y la definición de NP-C explique qué ocurriría si se demuestra que la afirmación es correcta.
6. Un tercer problema al que llamaremos X se puede reducir polinomialmente al problema de decisión de “los centros de atención”, ¿qué podemos decir acerca de su complejidad?
