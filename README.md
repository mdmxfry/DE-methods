# Variant 19 (Sukach Maxim, BS17-03)

#### Содержание:
1. [Уравнение](#eq)
2. [Решение](#solution)
2. [Метод Эйлера](#euler)
3. [Усовершенствованный метод Эйлера](#imp_euler)
4. [Классический метод Рунге-Кутты](#runge_kutta)
5. [Сравнение методов для заданной задачи](#comparing)
6. [Заключение](#conclusion)
7. [Запуск](#launch)
8. [Ссылки](#links)

## <a name="eq"></a>Уравнение
№19:

<img src="https://latex.codecogs.com/gif.latex?\frac{dy}{dx}&space;=&space;2y^{1/2}&space;&plus;&space;2y">

## <a name="solution"></a>Решение
<img src="https://latex.codecogs.com/gif.latex?\newline\frac{dy}{dx}&space;=&space;2y^{1/2}&plus;2y&space;\newline&space;\newline&space;\frac{dy}{2(y^{1/2}&plus;y)}=dx&space;\newline&space;\newline&space;\int&space;\frac{dy}{2(y^{1/2}&plus;y)}=\int&space;dx&space;\newline&space;\newline&space;\ln&space;(\sqrt&space;y&space;&plus;&space;1)&space;=&space;x&space;&plus;&space;C_{1}&space;\newline&space;\newline&space;\sqrt&space;y&space;&plus;&space;1&space;=&space;e^{x&space;&plus;&space;C_{1}}&space;\newline&space;\newline&space;y&space;=&space;(e^{x&plus;C_{1}}&space;-&space;1)^{2}" title="\frac{dy}{dx} = 2y^{1/2}+2y \newline \newline \frac{dy}{2(y^{1/2}+y)}=dx \newline \newline \int \frac{dy}{2(y^{1/2}+y)}=\int dx \newline \newline \ln (\sqrt y + 1) = x + C_{1} \newline \newline \sqrt y + 1 = e^{x + C_{1}} \newline \newline y = (e^{x+C_{1}} - 1)^{2}">

Найдем <img src="https://latex.codecogs.com/gif.latex?C_{1}">

<img src="https://latex.codecogs.com/gif.latex?\newline&space;x_{0}&space;=&space;0,&space;y_{0}&space;=&space;1&space;\newline&space;\newline&space;1=(e^{C_{1}}-1)^{2}&space;\newline&space;\newline&space;e^{2C_{1}}=2e^{C_{1}}&space;\newline&space;\newline&space;e^{C_{1}}&space;=&space;2&space;\newline&space;\newline&space;C_{1}&space;=&space;ln(2)&space;\approx&space;0.693">

В итоге, наше решение принимает вид:

<img src="https://latex.codecogs.com/gif.latex?y&space;=&space;(e^{x&plus;0.693}&space;-&space;1)^{2}">


## <a name="euler"></a>Метод Эйлера

Метод Эйлера дает возможность приближенно выразить функцию теоретически с любой наперед заданной точностью. Суть метода Эйлера в пошаговом вычислении значений решения y=y(x) дифференциального уравнения вида y’=f(x,y) с начальным условием (x0;y0).
Метод Эйлера является методом 1-го порядка точности и называется методом ломаных. 

Для вычисления используются следующие формулы:

<img src="https://latex.codecogs.com/gif.latex?\left\{\begin{matrix}&space;&x_{n&plus;1}=x_{n}&space;&plus;&space;h&space;\\&space;&y_{n&plus;1}=y_{n}&space;&plus;&space;hf(x_{i},&space;y_{i})&space;\end{matrix}\right.">
<figure>
<img src="https://user-images.githubusercontent.com/32166900/47929321-bb831680-ded9-11e8-8e51-9da92a83bd00.png">
<figcaption><i>Метод Эйлера и точное решение при x0 = 0, xf = 9, y0 = 1, h = 0.1 </i></figcaption>
</figure>

## <a name="imp_euler"></a>Усовершенствованный метод Эйлера

Суть усовершенствованного метода Эйлера в пошаговом вычислении значений решения y=y(x) дифференциального уравнения вида y’=f(x,y) с начальным условием (x0;y0).
Усовершенствованный метод Эйлера является методом 2-го порядка точности и называется модифицированным методом Эйлера.

Разница между данным методом и методом Эйлера минимальна и заключается в использовании следующих формул:

<img src="https://latex.codecogs.com/gif.latex?\left\{\begin{matrix}&space;&x_{n&plus;1}=x_{n}&space;&plus;&space;h&space;\\&space;&y_{n&plus;1}=y_{n}&space;&plus;&space;\Delta&space;y&space;\\&space;&\Delta&space;y&space;=&space;hf(x_{n}&space;&plus;&space;\frac{h}{2},&space;y_{n}&space;&plus;&space;\frac{h}{2}f(x_{i},y_{i})))&space;\end{matrix}\right.">

<figure>
<img src="https://user-images.githubusercontent.com/32166900/47929373-da81a880-ded9-11e8-81c8-48b6f645d1e5.png">
<figcaption><i> Усовершенствованный Метод Эйлера и точное решение при <br> x0 = 0, xf = 9, y0 = 1, h = 0.1 </i></figcaption>
</figure>

## <a name="runge_kutta"></a>Классический метод Рунге-Кутты
Суть метода Рунге-Кутты в пошаговом вычислении значений решения y=y(x) дифференциального уравнения вида y’=f(x,y) с начальным условием (x0;y0).
Классический метод Рунге-Кутты является методом 4-го порядка точности и называется методом Рунге-Кутты 4-го порядка точности.

Ну и как обычно, формулы:

<img src="https://latex.codecogs.com/gif.latex?\left\{\begin{matrix}&space;&x_{n&plus;1}=x_{n}&space;&plus;&space;h&space;\\&space;&y_{n&plus;1}=y_{n}&space;&plus;&space;\Delta&space;y&space;\\&space;&\Delta&space;y&space;=&space;\frac{k_{1}&plus;2k_{2}&plus;2k_{3}&plus;k_{4}}{6}&space;\\&space;&k_{1}&space;=&space;hf(x_{n},&space;y_{n})&space;\\&space;&k_{2}&space;=&space;hf(x_{n}&space;&plus;&space;\frac{h}{2},&space;y_{n}&space;&plus;&space;\frac{k_{2}}{2})\\&space;&k_{3}&space;=&space;hf(x_{n}&space;&plus;&space;\frac{h}{2},&space;y_{n}&space;&plus;&space;\frac{k_{2}}{2})&space;\\&space;&k_{4}&space;=&space;hf(x_{n}&space;&plus;&space;h,&space;y_{n}&space;&plus;&space;k_{3})&space;\end{matrix}\right.">

<figure>
<img src="https://user-images.githubusercontent.com/32166900/47929419-000eb200-deda-11e8-874f-21ce7db5c8fa.png">
<figcaption><i> Классический метод Рунге-Кутты и точное решение при x0 = 0, xf = 9, y0 = 1, h = 0.1 </i></figcaption>
</figure>

## <a name="comparing"></a>Сравнение методов для заданной задачи

## <a name="conclusion"></a>Заключение

## <a name="launch"></a>Запуск

### <a name="links"></a>Ссылки
