---


---

<ul>
<li><a href="http://www.cnblogs.com/">博客园</a></li>
<li><a href="http://www.cnblogs.com/dotnetcrazy/">首页</a></li>
<li><a href="https://i.cnblogs.com/EditPosts.aspx?opt=1">新随笔</a></li>
<li><a href="https://msg.cnblogs.com/send/%E9%B2%B2%E9%80%B8%E9%B9%8F">联系</a></li>
<li><a href="http://www.cnblogs.com/dotnetcrazy/rss">订阅</a></li>
<li><a href="https://i.cnblogs.com/">管理</a></li>
</ul>
<p>随笔 - 17 文章 - 0 评论 - 30</p>
<h1 id="python3-与-c-基础语法对比（就当python和c基础的普及吧）"><a href="https://www.cnblogs.com/dotnetcrazy/p/9102030.html">Python3 与 C# 基础语法对比（就当Python和C#基础的普及吧）</a></h1>
<p>VSCode设置python3的开发环境（linux下默认是python2）<a href="https://www.cnblogs.com/dotnetcrazy/p/9095793.html">https://www.cnblogs.com/dotnetcrazy/p/9095793.html</a></p>
<p><strong>欢迎提出更简单的语法~（文章中案例有两个福利哦，一个是养生，一个是人工智能[ 密码：fqif]）</strong></p>
<p>先说下感觉，python的编程有点<strong>JavaScript</strong>的感觉(比如：'和“有时候不区别)，又感觉像外国版的<strong>易语言</strong>，整个过程像读书一样，比如一个元素不在列表之中==&gt;  <strong>for</strong>  item  <strong>not in</strong>  lists。使用它做个大点的项目<strong>一定要先规定好编程风格</strong>，不然能让人崩溃的。先不深究，后面会继续深究。。。（Python2我就不讲了，官方推荐使用<strong>Python3</strong>）</p>
<p>0.命名规则</p>
<blockquote>
<p>Python官方是推荐使用_来间隔单词，但一般开发人员都是以各自主语言的命名来定义的，这个就各人爱好了，不过团队一定要统一。</p>
<p><strong>标示符</strong>由<strong>字母、下划线和数字组成，且数字不能开头</strong>（这个基本上都一样）<strong>注意</strong>：<strong>标识符是区分大小写的</strong></p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180529060042515-399043795.png" alt=""><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180529060129010-816355646.png" alt=""></p>
<p><strong>命名规则</strong>，总的原则就是见名知意，一般都是<strong>驼峰命名法</strong>，纯Python的话推荐用_连接单词</p>
<p>扩充：Python的<strong>关键词</strong>可以自己打印一下：</p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180529064319904-405690575.png" alt=""></p>
<p>[‘False’, ‘None’, ‘True’, ‘and’, ‘as’, ‘assert’, ‘break’, ‘class’, ‘continue’, ‘def’, ‘del’, ‘elif’, ‘else’, ‘except’, ‘finally’, ‘for’, ‘from’, ‘global’, ‘if’, ‘import’, ‘in’, ‘is’, ‘lambda’, ‘nonlocal’, ‘not’, ‘or’, ‘pass’, ‘raise’, ‘return’, ‘try’, ‘while’, ‘with’, ‘yield’]</p>
</blockquote>
<p>1.注释</p>
<blockquote>
<p>python：<strong>#注释一行</strong>，<strong>三个单引号或者三个双引号注释多行</strong>：<strong>’’‘<strong>XXX</strong>’’'<strong>或者</strong>""“<strong>XXXX</strong>”""</strong>（一般用#就够了，有点像shell脚本的感觉）</p>
<p>python输出就直接<strong>print</strong>即可，C是<strong>printf</strong>（不要搞混哦）</p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180528204912531-544194046.jpg" alt=""></p>
<p>C、Java、Net都是//注释一行，/**/注释多行</p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180528204408977-516180583.png" alt=""></p>
</blockquote>
<p>2.变量</p>
<blockquote>
<p>python定义变量比较牛逼，直接写变量名即可，句子后面<strong>不用加分号</strong>，eg：<strong>name="小明"</strong></p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180528205845946-1829179566.jpg" alt=""></p>
<p>netcore，可以用var来进行类型推断，eg：<strong>var name=“小明”;</strong></p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180528205235449-674598924.png" alt=""></p>
</blockquote>
<p>3.输入输出</p>
<blockquote>
<p><strong>换行输出，不换行输出：</strong>(<strong>\n</strong>使用这个就不说了，它们和C都是一样的)</p>
<p>python：<strong>print(“<a href="http://dnt.dkill.net/now">dnt.dkill.net/now</a>”,end=’’)  #默认end=’\n’ （’ 和 " 随意）</strong></p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180528223249683-720219817.png" alt=""></p>
<p>netcore: <strong>Console.Write Console.WriteLine</strong></p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180528223437421-1310985897.png" alt=""></p>
<hr>
<p>python输出多个<strong>重复字符</strong>，不需要自己手打N个*或者for循环输出多个<strong>重复字符</strong>，eg:*<em>print("x"<em>10)</em></em></p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180528210122036-1636038821.png" alt=""></p>
<p><img src="https://common.cnblogs.com/images/copycode.gif" alt="复制代码"></p>
<h1 id="c----字符--s----通过str-字符串转换来格式化--o----八进制整数--x----十六进制整数（小写字母）--x----十六进制整数（大写字母）--e----指数（小写e）--e----指数（大写“e”）--f----浮点实数--g----％f和％e-的简写--g----％f和％e的简写">%c    字符 # %s    通过str() 字符串转换来格式化 # %o    八进制整数 # %x    十六进制整数（小写字母） # %X    十六进制整数（大写字母） # %e    指数（小写’e’） # %E    指数（大写“E”） # %f    浮点实数 # %g    ％f和％e 的简写 # %G    ％f和％E的简写</h1>
<p><img src="https://common.cnblogs.com/images/copycode.gif" alt="复制代码"></p>
<p>下面来个输入输出的简单的案例吧：<strong>打印一张名片，Name:毒逆天，Gender：男</strong></p>
<p>Python：<strong>print(“Name:%s,Gender:%s”%(name,gender))</strong>【注意引号后面没有，哦】</p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180528212801772-1459012137.jpg" alt=""></p>
<p>NetCore：<strong>Console.WriteLine($“Name:{name}，Gender:{gender}”);</strong></p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180528212619290-2008780206.png" alt=""></p>
</blockquote>
<p>4.类型转换+算术运算符</p>
<blockquote>
<p>python：类型(值)，eg:<strong>int()，long()，float()，str()</strong>…等等（Python没有<strong>double</strong>类型哦~）【<strong>扩</strong>：转换成16进制：<strong>hex()</strong>、转换为8进制：<strong>oct()</strong>】</p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180528221534625-20095184.jpg" alt=""></p>
<p>netcore：该案例推荐使用 int.TryParse，我这边就用常用的<strong>Convert</strong>系列了【支持类型比较多】</p>
<p>Convert.ToInt64(),Convert.ToDouble()，Convert.ToString()</p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180528221622853-1590600585.jpg" alt=""></p>
<p>算术运算符编程语言基本上差不多，Python多了个  <strong>//  取商（%是取余）和 幂</strong>**，来个案例：</p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180529081921282-1874909883.png" alt=""></p>
<p>netcore（C#常用数学方法都在Match类中）</p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180529081950290-1639387865.png" alt=""></p>
<p>**+= -= *= /= %= <strong>= //=</strong>  这些就不用详说了吧？（举个例子：<strong>c += a 等效于 c = c + a</strong>）</p>
</blockquote>
<p>5.if else</p>
<blockquote>
<p>说Python像外国版的易语言，这边就可以看出来一点了，先说说Python的<strong>逻辑运算符</strong>==》<strong>与and  或or  非not</strong>，这个倒是跟C、C#、Java等大大不同，如果再结合Python命名规则就感觉在阅读文章一样</p>
<p>关系运算符和其他语言基本上差不多（<strong>==</strong>  !=  <strong>&lt;&gt;</strong>  <strong>&gt;</strong>  <strong>&lt;</strong>  <strong>&gt;=</strong>  <strong>&lt;=</strong>），就一点不一样：也可以用**&lt;&gt;**</p>
<p>来个if else基础语法：<strong>括号可加可不加，但是记得加：。不用大括号，但是if里面的代码注意缩进</strong></p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180529084030576-2013022763.png" alt=""></p>
<p>netcore：if或者else下面是单行代码可以不用写括号</p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180529084155612-1095775130.png" alt=""></p>
<p>再来个嵌套的：<strong>注意哦~else if 在python里面简写成了：elif</strong></p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180529084651600-2089053792.png" alt=""></p>
<p>netcore：单行代码可以不用写括号</p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180529084856202-656008625.png" alt=""></p>
</blockquote>
<p>6.while</p>
<blockquote>
<p>直接来个案例：</p>
<p>python里面没有++ 和 --，这点的确用的有点小不方便，<strong>扩展部分有相关说明</strong></p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180529090127015-1245308093.png" alt=""></p>
<p>netcore</p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180529085840340-1265270165.png" alt=""></p>
</blockquote>
<p>7.for</p>
<blockquote>
<p>python的<strong>for</strong>循环，类似于js里面的<strong>for in</strong>  以及C#里面的<strong>foreach</strong></p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180529094101943-1131766793.png" alt=""></p>
<p>netcore: <strong>foreach (var i in name)</strong></p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180529094226553-1539024857.png" alt=""></p>
</blockquote>
<hr>
<p>老规矩，来个扩展：switch（这个目前不用掌握，看看就好，后面会继续探讨的）</p>
<blockquote>
<p>Python没有 ++/-- <a href="https://blog.csdn.net/somehow1002/article/details/73744626">参考文章（点我）</a></p>
<p>python 中，变量是以内容为基准而不是像 c 中以变量名为基准，所以只要你的数字内容是5，不管你起什么名字，这个变量的 ID 是相同的，同时也就说明了 python 中一个变量可以以多个名称访问</p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180529092338794-1865165245.png" alt=""></p>
<p>如上例，a 和 b 都是 5，当你++改变了 a 时，b 也会跟着变，这当然不是我们希望的。so，正确的自增操作应该 a += 1，通过 id() 观察可知，id 值变化了，即 a 已经是新值的名称</p>
<hr>
<p><strong>for的扩展</strong>（一般不太用）官方参考：<a href="https://docs.python.org/3/reference/compound_stmts.html#the-for-statement">https://docs.python.org/3/reference/compound_stmts.html#the-for-statement</a></p>
<p><img src="https://images2018.cnblogs.com/blog/1127869/201805/1127869-20180531172814702-1628372100.png" alt=""></p>
<p>图片出处：<a href="https://www.cnblogs.com/dspace/p/6622799.html">https://www.cnblogs.com/dspace/p/6622799.html</a></p>
<hr>
<p><strong>Python 没有 switch / case 语句。为了实现它，我们可以使用字典映射：</strong></p>
<h1 id="官方的解释说，“用if...-elif...-elif...-else序列很容易来实现-switch--case-语句”。而且可以使用函数字典映射和类的调度方法。"><strong><a href="https://docs.python.org/3.6/faq/design.html#why-isn-t-there-a-switch-or-case-statement-in-python">官方的解释说，“用if… elif… elif… else序列很容易来实现 switch / case 语句”。而且可以使用函数字典映射和类的调度方法。</a></strong></h1>
<p><img src="https://common.cnblogs.com/images/copycode.gif" alt="复制代码"></p>
<p>def numbers_to_strings(argument):<br>
switcher = {<br>
0: “zero”, 1: “one”, 2: “two”,<br>
} return switcher.get(argument, “nothing”)</p>
<p><img src="https://common.cnblogs.com/images/copycode.gif" alt="复制代码"></p>
<p>这段代码类似于：</p>
<p><img src="https://common.cnblogs.com/images/copycode.gif" alt="复制代码"></p>
<p>function(argument){ switch(argument) { case 0: return “zero”; case 1: return “one”; case 2: return “two”; default: return “nothing”;<br>
};<br>
};</p>
<p><img src="https://common.cnblogs.com/images/copycode.gif" alt="复制代码"></p>
<p><strong>在 Python 中字典映射也可以包含函数或者 lambda 表达式</strong>：</p>
<p><img src="https://common.cnblogs.com/images/copycode.gif" alt="复制代码"></p>
<p>def zero(): return “zero”</p>
<p>def one(): return “one”</p>
<p>def numbers_to_functions_to_strings(argument):<br>
switcher = {<br>
0: zero, 1: one, 2: lambda: “two”,<br>
}<br>
func = switcher.get(argument, lambda: “nothing”) return func()</p>
<p><img src="https://common.cnblogs.com/images/copycode.gif" alt="复制代码"></p>
<p><strong>类的调度方法:</strong></p>
<p>如果在一个类中，不确定要使用哪种方法，可以用一个调度方法在运行的时候来确定。</p>
<p><img src="https://common.cnblogs.com/images/copycode.gif" alt="复制代码"></p>
<pre><code>class Switcher(object): def numbers_to_methods_to_strings(self, argument):
    method_name = 'number_' + str(argument)
    method = getattr(self, method_name, lambda: "nothing") return method() def number_0(self): return "zero"

def number_1(self): return "one"

def number_2(self): return "two"
</code></pre>
<p><img src="https://common.cnblogs.com/images/copycode.gif" alt="复制代码"></p>
<p><a href="https://docs.python.org/3.6/faq/design.html#why-isn-t-there-a-switch-or-case-statement-in-python">https://docs.python.org/3.6/faq/design.html#why-isn-t-there-a-switch-or-case-statement-in-python</a></p>
</blockquote>
<p>Python设计相关的为什么，可以参考官方文档：<a href="https://docs.python.org/3.6/faq/design.html">https://docs.python.org/3.6/faq/design.html</a></p>
<p>C#基础可以看：<a href="https://github.com/dunitian/LoTCodeBase/tree/master/NetCode/1.%E9%9D%A2%E5%90%91%E8%BF%87%E7%A8%8B">https://github.com/dunitian/LoTCodeBase/tree/master/NetCode/1.面向过程</a></p>
<blockquote>
<p>reference：<br>
<a href="https://www.cnblogs.com/dotnetcrazy/p/9102030.html">https://www.cnblogs.com/dotnetcrazy/p/9102030.html</a></p>
</blockquote>

