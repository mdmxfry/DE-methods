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

В Python:
	
	def next_y(xi, yi):
	    return yi + self.h * self.f(xi, yi)
	
	ys = []
	xs = np.arange(x0 + h, xf + h, h)  # вектор всех значений x
	for x in xs:
        ys.append(y)
        y = next_y(x, y) # В результате ys будет содержать все значения метода Эйлера
    

<figure>
<img src="https://user-images.githubusercontent.com/32166900/47929321-bb831680-ded9-11e8-8e51-9da92a83bd00.png">
<figcaption><i>Метод Эйлера и точное решение при x0 = 0, xf = 9, y0 = 1, h = 0.1 </i></figcaption>
</figure>

<figure>
<img src="https://user-images.githubusercontent.com/32166900/47952091-4ff18580-df7b-11e8-843a-9d60171847df.png">
<figcaption><i>Метод Эйлера и точное решение при x0 = 0, xf = 3, y0 = 1, h = 0.1 </i></figcaption>
</figure>

<figure>
<img src="https://user-images.githubusercontent.com/32166900/47952099-6b5c9080-df7b-11e8-9614-8146f7702cdc.png">
<figcaption><i>Метод Эйлера и точное решение при x0 = 0, xf = 1, y0 = 1, h = 0.1 </i></figcaption>
</figure>

## <a name="imp_euler"></a>Усовершенствованный метод Эйлера

Суть усовершенствованного метода Эйлера в пошаговом вычислении значений решения y=y(x) дифференциального уравнения вида y’=f(x,y) с начальным условием (x0;y0).
Усовершенствованный метод Эйлера является методом 2-го порядка точности и называется модифицированным методом Эйлера.

Разница между данным методом и методом Эйлера минимальна и заключается в использовании следующих формул:

<img src="https://latex.codecogs.com/gif.latex?\left\{\begin{matrix}&space;&x_{n&plus;1}=x_{n}&space;&plus;&space;h&space;\\&space;&y_{n&plus;1}=y_{n}&space;&plus;&space;\Delta&space;y&space;\\&space;&\Delta&space;y&space;=&space;hf(x_{n}&space;&plus;&space;\frac{h}{2},&space;y_{n}&space;&plus;&space;\frac{h}{2}f(x_{i},y_{i})))&space;\end{matrix}\right.">

В Python:
	
	# Заменяем next_y функцию на эту:
		
	def next_y(xi, yi):
       h2 = h / 2
       delta_y = h * f(xi + h2, yi + h2 * f(xi, yi))
       return yi + delta_y

<figure>
<img src="https://user-images.githubusercontent.com/32166900/47929373-da81a880-ded9-11e8-81c8-48b6f645d1e5.png">
<figcaption><i> Усовершенствованный Метод Эйлера и точное решение при <br> x0 = 0, xf = 9, y0 = 1, h = 0.1 </i></figcaption>
</figure>

<figure>
<img src="https://user-images.githubusercontent.com/32166900/47952104-8e874000-df7b-11e8-9425-1839e796b5d5.png">
<figcaption><i> Усовершенствованный Метод Эйлера и точное решение при <br> x0 = 0, xf = 3, y0 = 1, h = 0.1 </i></figcaption>
</figure>

<figure>
<img src="https://user-images.githubusercontent.com/32166900/47952103-89c28c00-df7b-11e8-9554-4712eb13d2c1.png">
<figcaption><i> Усовершенствованный Метод Эйлера и точное решение при <br> x0 = 0, xf = 1, y0 = 1, h = 0.1 </i></figcaption>
</figure>

## <a name="runge_kutta"></a>Классический метод Рунге-Кутты
Суть метода Рунге-Кутты в пошаговом вычислении значений решения y=y(x) дифференциального уравнения вида y’=f(x,y) с начальным условием (x0;y0).
Классический метод Рунге-Кутты является методом 4-го порядка точности и называется методом Рунге-Кутты 4-го порядка точности.

Ну и как обычно, формулы:

<img src="https://latex.codecogs.com/gif.latex?\left\{\begin{matrix}&space;&x_{n&plus;1}=x_{n}&space;&plus;&space;h&space;\\&space;&y_{n&plus;1}=y_{n}&space;&plus;&space;\Delta&space;y&space;\\&space;&\Delta&space;y&space;=&space;\frac{k_{1}&plus;2k_{2}&plus;2k_{3}&plus;k_{4}}{6}&space;\\&space;&k_{1}&space;=&space;hf(x_{n},&space;y_{n})&space;\\&space;&k_{2}&space;=&space;hf(x_{n}&space;&plus;&space;\frac{h}{2},&space;y_{n}&space;&plus;&space;\frac{k_{2}}{2})\\&space;&k_{3}&space;=&space;hf(x_{n}&space;&plus;&space;\frac{h}{2},&space;y_{n}&space;&plus;&space;\frac{k_{2}}{2})&space;\\&space;&k_{4}&space;=&space;hf(x_{n}&space;&plus;&space;h,&space;y_{n}&space;&plus;&space;k_{3})&space;\end{matrix}\right.">

В Python:
	
	# Заменяем next_y функцию на эту:
		
	def next_y(xi, yi):
        h2 = h / 2
        k1 = f(xi, yi)
        k2 = f(xi + h2, yi + h2 * k1)
        k3 = f(xi + h2, yi + h2 * k2)
        k4 = f(xi + h, yi + h * k3)
        return yi + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)


<figure>
<img src="https://user-images.githubusercontent.com/32166900/47929419-000eb200-deda-11e8-874f-21ce7db5c8fa.png">
<figcaption><i> Классический метод Рунге-Кутты и точное решение при x0 = 0, xf = 9, y0 = 1, h = 0.1 </i></figcaption>
</figure>

<figure>
<img src="https://user-images.githubusercontent.com/32166900/47952120-b4ace000-df7b-11e8-903b-d563aa766b78.png">
<figcaption><i> Классический метод Рунге-Кутты и точное решение при x0 = 0, xf = 3, y0 = 1, h = 0.1 </i></figcaption>
</figure>

<figure>
<img src="https://user-images.githubusercontent.com/32166900/47952119-b4ace000-df7b-11e8-815a-5f5c2702541c.png">
<figcaption><i> Классический метод Рунге-Кутты и точное решение при x0 = 0, xf = 1, y0 = 1, h = 0.1 </i></figcaption>
</figure>

## <a name="comparing"></a>Сравнение методов для заданной задачи
<figure>
<img src="https://user-images.githubusercontent.com/32166900/47951678-0b62eb80-df75-11e8-9635-fdbf4ec200dc.png">
<figcaption>Размер ошибки всех методов на промежутке [0, 9] с шагом 0.1</figcaption>
</figure>

<figure>
<img src="https://user-images.githubusercontent.com/32166900/47951701-701e4600-df75-11e8-83bd-d66cfe0c8b67.png">
<figcaption>Размер ошибки всех методов на промежутке [0, 3] с шагом 0.1</figcaption>
</figure>

<figure>
<img src="https://user-images.githubusercontent.com/32166900/47951712-90e69b80-df75-11e8-9706-5e3e747cfb79.png">
<figcaption>Размер ошибки всех методов на промежутке [0, 1] с шагом 0.1</figcaption>
</figure>

## <a name="conclusion"></a>Заключение

Очевидно что, классический метод Рунге-Кутты справляется с задачей аппроксимации в случае данного уравнения намного лучше чем Метод Эйлера и Усовершенствованный метод Эйлера. 

### График глобальной средней ошибки

<figure>
<img src="https://user-images.githubusercontent.com/32166900/47970404-e3b77480-e095-11e8-904a-d446bd110c68.png">
<figcaption>
Глобальная ошибка в зависимости от размера шага H на промежтке [1, 9]
</figcaption>
</figure>


## <a name="launch"></a>Запуск

1. Установить Python3
2. Все пакеты необходимые для работы находятся в **requirements.txt**

   	matplotlib<br>
  	numpy

3. Запустить run.py в корневой директории проекта.

Все настройки находятся в run.py в виде констант (строки 12-16). configparser очень не хотелось подключать. После запуска скрипт покажет 6 графиков (в диком разрешении, там ничего не видно толком) и сохранит их нормальные версии (dpi=300) в папке **results**. 

### <a name="links"></a>Ссылки
Latex Редактор: <a href="https://www.codecogs.com/latex/eqneditor.php">https://www.codecogs.com/latex/eqneditor.php</a><br>
Метод Эйлера: <a href="https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_%D0%AD%D0%B9%D0%BB%D0%B5%D1%80%D0%B0">Wikipedia</a>
<br>
Усовершенствованный метод Эйлера: <a href="http://mathprofi.ru/metody_eilera_i_runge_kutty.html">Mathprofi</a> (кык)
<br>
Метод Рунге — Кутты: <a href="https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_%D0%A0%D1%83%D0%BD%D0%B3%D0%B5_%E2%80%94_%D0%9A%D1%83%D1%82%D1%82%D1%8B">Wikipedia</a>
