HTML--超文本标记语言 (Hyper Text Markup Language)
        定义
                HTML 不是一种编程语言，而是一种标记语言 (markup language)
                标记语言是一套标记标签 (markup tag)
                HTML 使用标记标签来描述网页
        HTML 标签(HTML tag)
                规则
                            由尖括号包围的关键词，比如 <html>
                            成对出现，比如 <b> 和 </b>
                            标签对中的第一个标签是开始标签，第二个标签是结束标签，开始和结束标签也被称为开放标签和闭合标签  
                            小写标签
                标签 
                            HTML 标题(Heading) -- <h1> to <h6> -- 浏览器会自动地在标题或块级元素的前后添加空行
                            HTML 段落(Paragraph) -- <p> 
                            HTML 头部元素(Head)  -- 所有头部元素的容器 -- 可包含脚本，指示浏览器在何处可以找到样式表，提供元信息，等等
                                        HTML 头部元素 -- 以下标签都可以添加到 head 部分：<title>、<base>、<link>、<meta>、<script> 以及 <style>
                                                    标签  描述
                                                    <head>  文档信息
                                                    <title> 文档标题，浏览器工具栏中的标题，收藏夹显示的标题，搜索引擎结果中的页面标题，必须
                                                    <base>  定义页面上所有链接的默认地址或默认目标
                                                    <link>  定义文档与外部资源之间的关系-- 最常用于连接样式表 -- <link rel="stylesheet" type="text/css" href="mystyle.css" />
                                                    <meta>  提供关于 HTML 文档的元数据 -- 描述文档 -- 定义文档关键词 -- 元数据不会显示在页面上，机器可读
                                                                        典型的情况是，meta 元素被用于规定页面的描述、关键词、文档的作者、最后修改时间以及其他元数据。
                                                                        <meta> 标签始终位于 head 元素中。
                                                                        元数据可用于浏览器（如何显示内容或重新加载页面），搜索引擎（关键词），或其他 web 服务。    
                                                                        针对搜索引擎的关键词
                                                                        一些搜索引擎会利用 meta 元素的 name 和 content 属性来索引页面
                                                                                    下面的 meta 元素定义页面的描述：
                                                                                    <meta name="description" content="Free Web tutorials on HTML, CSS, XML" />
                                                                                    下面的 meta 元素定义页面的关键词：
                                                                                    <meta name="keywords" content="HTML, CSS, XML" />
                                                                                    下面的 meta 元素定义页面的作者：
                                                                                    <meta name="author" content="UIkit中文网">
                                                                                    下面的 meta 元素定义页面的？？：
                                                                                    <meta name="viewport" content="width=device-width, initial-scale=1">
                                                                                    下面的 meta 元素定义页面的？？：
                                                                                    <meta charset="utf-8">
                                                                                    name 和 content 属性的作用是描述页面的内容。                                                                                                        
                                                    <script>    定义客户端脚本
                                                    <style> 定义客户端脚本 -- 规定 HTML 元素在浏览器中呈现的样式                            
                            HTML 主体(Body) -- <body>  HTML 文档的主体
                            HTML 链接(URL) --  <a> <a href="链接地址">link</a> -- 超链接可以是字，词，图像，或其他 HTML 元素 -- 点击这些内容来跳转到新文档或当前文档中的某个部分
                                        通过使用 href 属性 - 创建指向另一个文档的链接
                                                    href 属性规定链接的目标。
                                                    开始标签和结束标签之间的文字被作为超级链接来显示。
                                                    使用 Target 属性，你可以定义被链接的文档在何处显示
                                                    实例
                                                    <a href="http://www.w3school.com.cn/" target="_blank">Visit W3School!</a>                                      
                                        通过使用 name 属性 - 创建文档内的书签
                                                    命名锚的语法：
                                                    <a name="label">锚（显示在页面上的文本）</a>        
                                                    提示：锚的名称可以是任何你喜欢的名字。
                                                    提示：您可以使用 id 属性来替代 name 属性，命名锚同样有效。                                
                                                    name 属性规定锚（anchor）的名称。
                                                    您可以使用 name 属性创建 HTML 页面中的书签。
                                                    书签不会以任何特殊方式显示，它对读者是不可见的。
                                                    当使用命名锚（named anchors）时，我们可以创建直接跳至该命名锚（比如页面中某个小节）的链接，这样使用者就无需不停地滚动页面来寻找他们需要的信息了。                                        
                            HTML 图像(Image) -- <img> <img src="图片地址" width="104" height="142" /> --图像名称和尺寸以属性的形式提供
                                        替换文本属性（Alt）
                                        alt 属性用来为图像定义一串预备的可替换的文本。替换文本属性的值是用户定义的。
                                        <img src="boat.gif" alt="Big Boat">     
                                                               在浏览器无法载入图像时，替换文本属性告诉读者她们失去的信息。此时，浏览器将显示这个替代性的文本而不是图像。为页面上的图像
                                                               都加上替换文本属性是个好习惯，这样有助于更好的显示信息，并且对于那些使用纯文本浏览器的人来说是非常有用的。
                            HTML 水平线(Horizontal Line) -- <hr />  在 HTML 页面中创建水平线
                            HTML 注释(Comments) -- <!-- comment --> -- 提高其可读性 使代码更易理解 浏览器会忽略注释 不会显示它们
                            HTML 空行(Break) -- <br />
                            HTML 短引用(Quotation) -- <q> -- 短的行内引用 -- 浏览器会为 <q> 元素包围引号
                            HTML 长引用(Quotation) -- <blockquote> -- 定义被引用的节 -- 浏览器会对 <blockquote> 元素进行缩进处理
                            HTML 缩略词(Abbreviation) -- <abbr> 缩写或首字母缩略语 -- <abbr title="World">W</abbr>
                            HTML 定义() -- <dfn> 项目或缩写的定义 -- title="World">W</dfn> or <dfn><abbr title="World">W</abbr> 缩略词会以斜体显示
                            HTML 联系信息(Address) -- <address> -- 定义文档或文章的联系信息（作者/拥有者） -- 以斜体显示 -- 元素前后添加折行
                            HTML <cite> -- 定义著作的标题 -- 斜体显示
                            HTML <bdo> --  双向重写 -- 覆盖当前文本方向，以相反方向显示
                            <style> 定义样式定义。
                            <link>  定义资源引用。
                            <div>   定义文档中的节或区域（块级）。
                            <span>  定义文档中的行内的小块或区域。
                            <font>  规定文本的字体、字体尺寸、字体颜色。不赞成使用。请使用样式。
                            <basefont>  定义基准字体。不赞成使用。请使用样式。
                            <center>    对文本进行水平居中。不赞成使用。请使用样式。
                            HTML 超链接(链接) -- <a> 标签--超链接可以是一个字，一个词，或者一组词，也可以是一幅图像 -- 点击这些内容来跳转到新的文档或者当前文档中的某个部分
                            HTML 表格(table) -- <table> 标签 -- 表格由 <table> 标签来定义
                                        表格标签
                                                    表格  描述
                                                    <table> 定义表格
                                                    <caption>   定义表格标题。
                                                    <th>    定义表格的表头。
                                                    <tr>    定义表格的行。
                                                    <td>    定义表格单元。
                                                    <thead> 定义表格的页眉。
                                                    <tbody> 定义表格的主体。
                                                    <tfoot> 定义表格的页脚。
                                                    <col>   定义用于表格列的属性。
                                                    <colgroup>  定义表格列的组。                                        
                                        每个表格均有若干行(由 <tr> 标签定义) -- table row
                                        每行被分割为若干单元格(由 <td> 标签定义) -- 字母 td 指表格数据(table data) -- 即数据单元格的内容 -- 数据单元格可以包含文本、图片、列表、段落、表单、水平线、表格等等
                                        表格和边框属性 -- 如果不定义边框属性，表格将不显示边框。有时这很有用，但是大多数时候，我们希望显示边框。
                                        使用边框属性来显示一个带有边框的表格 -- <table border="1">
                                        表格的表头(用 <th> 标签进行定义)
                                        表格中的空单元格() -- 空单元格中添加一个空格占位符 -- <td>&nbsp;</td>
                            HTML 列表() -- HTML 支持有序、无序和定义列表
                                        列表标签
                                                    标签  描述
                                                    <ol>    定义有序列表。
                                                    <ul>    定义无序列表。
                                                    <li>    定义列表项。
                                                    <dl>    定义定义列表。
                                                    <dt>    定义定义项目。
                                                    <dd>    定义定义的描述。                                        
                                        无序列表 -- 是一个项目的列表，此列项目使用粗体圆点（典型的小黑圆圈）进行标记 
                                                    无序列表始于 <ul> 标签。每个列表项始于 <li>
                                                    列表项内部可以使用段落、换行符、图片、链接以及其他列表等等。
                                        有序列表 -- 有序列表也是一列项目，列表项目使用数字进行标记
                                                    有序列表始于 <ol> 标签。每个列表项始于 <li> 标签
                                                    列表项内部可以使用段落、换行符、图片、链接以及其他列表等等
                                        定义列表 -- 自定义列表不仅仅是一列项目，而是项目及其注释的组合
                                                    自定义列表以 <dl> 标签开始。每个自定义列表项以 <dt> 开始。每个自定义列表项的定义以 <dd> 开始
                                                    定义列表的列表项内部可以使用段落、换行符、图片、链接以及其他列表等等
                            HTML <div> 和 <span> -- 可以通过 <div> 和 <span> 将 HTML 元素组合起来
                            
                                        HTML <div> 元素 -- 组合其他 HTML 元素的容器
                                                    HTML <div> 元素是块级元素，它是可用于组合其他 HTML 元素的容器
                                                    <div> 元素没有特定的含义。除此之外，由于它属于块级元素，浏览器会在其前后显示折行。
                                                    如果与 CSS 一同使用，<div> 元素可用于对大的内容块设置样式属性。
                                                    <div> 元素的另一个常见的用途是文档布局。它取代了使用表格定义布局的老式方法。使用 <table> 元素进行文档布局不是表格的正确用法。
                                                    <table> 元素的作用是显示表格化的数据。
                                        HTML <span> 元素 -- 文本的容器
                                                    HTML <span> 元素是内联元素，可用作文本的容器。
                                                    <span> 元素也没有特定的含义。
                                                    当与 CSS 一同使用时，<span> 元素可用于为部分文本设置样式属性。
                                        HTML 分组标签
                                                    标签  描述
                                                    <div>   定义文档中的分区或节（division/section）。
                                                    <span>  定义 span，用来组合文档中的行内元素。                                                    
                            HTML 块元素(block level element) -- 块级元素在浏览器显示时，通常会以新行来开始（和结束） -- 例子：<div>，<h1>, <p>, <ul>, <table>
                            HTML 内联元素(inline element) -- 内联元素在显示时通常不会以新行开始 -- 例子：<b>, <td>, <a>, <img>
                            HTML script元素() -- <script> 标签用于定义客户端脚本，比如 JavaScript
                                        script 元素既可包含脚本语句，也可通过 src 属性指向外部脚本文件
                                        必需的 type 属性规定脚本的 MIME 类型，默认是 type="text/javascript"
                                        JavaScript 最常用于图片操作、表单验证以及内容动态更新
                            <noscript> 标签 -- <noscript> 标签提供无法使用脚本时的替代内容，比方在浏览器禁用脚本时，或浏览器不支持客户端脚本时。
                            HTML 字符实体
                                            HTML 中有用的字符实体
                                            注释：实体名称对大小写敏感！
                                            显示结果    描述  实体名称    实体编号
                                                空格  &nbsp;  &#160;
                                            <   小于号 &lt;    &#60;
                                            >   大于号 &gt;    &#62;
                                            &   和号  &amp;   &#38;
                                            "   引号  &quot;  &#34;
                                            '   撇号  &apos; (IE不支持)  &#39;
                                            ￠   分（cent） &cent;  &#162;
                                            £   镑（pound）    &pound; &#163;
                                            ¥   元（yen）  &yen;   &#165;
                                            €   欧元（euro）    &euro;  &#8364;
                                            §   小节  &sect;  &#167;
                                            ©   版权（copyright）   &copy;  &#169;
                                            ®   注册商标    &reg;   &#174;
                                            ™   商标  &trade; &#8482;
                                            ×   乘号  &times; &#215;
                                            ÷   除号  &divide;    &#247;                            
                            
                            注释 <!--...--> 用于在源代码中插入注释。注释不会显示在浏览器中
                            声明 <!DOCTYPE html> 声明不是 HTML 标签，指示 web 浏览器使用那个 HTML 版本进行编写 
                            超链接 <a> 最重要的属性是 href 属性，它指示链接的目标 -- 支持 HTML 中的全局属性-事件属性
                                    如果不使用 href 属性，则不可以使用如下属性：href, download, hreflang, media, rel, target 以及 type 属性
                                    在 HTML5 中，<a> 标签始终是超链接，但是如果未设置 href 属性，则只是超链接的占位符
                                    属性
                                                属性                    值                            描述

                                                download           filename                   规定被下载的超链接目标。                                         
                                                href                    URL                         规定链接指向的页面的 URL。                                          
                                                hreflang             language_code         规定被链接文档的语言。
                                                media                media_query             规定被链接文档是为何种媒介/设备优化的
                                                name                 section_name           HTML5 中不支持。规定锚的名称。                                            
                                                rel                      text                          规定当前文档与被链接文档之间的关系。
                                                target               •   _blank                   规定在何处打开链接文档。
                                                                        •   _parent
                                                                        •   _self
                                                                        •   _top
                                                                        •   framename                                                                                                 
                                                type                 MIME type                 规定被链接文档的的 MIME 类型。
                            缩写 <abbr> <abbr title="People's Republic of China">PRC</abbr> -- 为浏览器、拼写检查和搜索引擎提供有用的信息  -- 全局属性，事件属性        
                                    
                                    可以在 <abbr> 标签中使用全局的 title 属性，这样就能够在鼠标指针移动到 <abbr> 元素上时显示出简称/缩写的完整版本         
                            联系信息 <address> 定义文档或文章的作者/拥有者的联系信息 -- 不应该用于描述通讯地址，除非它是联系信息的一部分 -- 全局属性，事件属性
                                        如果 <address> 元素位于 <body> 元素内，则它表示文档联系信息。
                                        如果 <address> 元素位于 <article> 元素内，则它表示文章的联系信息。
                                        <address> 元素中的文本通常呈现为斜体。大多数浏览器会在 address 元素前后添加折行
                                        <address> 元素通常连同其他信息被包含在 <footer> 元素中

                                        <address>
                                        Written by <a href="mailto:webmaster@example.com">Donald Duck</a>.<br> 
                                        Visit us at:<br>
                                        Example.com<br>
                                        Box 564, Disneyland<br>
                                        USA
                                        </address>
                            <area> 标签定义图像映射中的区域（注：图像映射指得是带有可点击区域的图像） -- 全局属性，事件属性
                                    area 元素总是嵌套在 <map> 标签中
                                    <img> 标签中的 usemap 属性与 map 元素 name 属性相关联，创建图像与映射之间的联系
                                    
                                    <img src="planets.jpg" border="0" usemap="#planetmap" alt="Planets" />
                                    <map name="planetmap" id="planetmap">
                                      <area shape="circle" coords="180,139,14" href ="venus.html" alt="Venus" />
                                      <area shape="circle" coords="129,161,10" href ="mercur.html" alt="Mercury" />
                                      <area shape="rect" coords="0,0,110,260" href ="sun.html" alt="Sun" />
                                    </map>

                                    <img> 中的 usemap 属性可引用 <map> 中的 id 或 name 属性（由浏览器决定），所以我们需要同时向 <map> 添加 id 和 name 两个属性
                                    必需的属性
                                            属性           值                     描述
                                            alt             text                   定义此区域的替换文本。
                                            
                                    可选的属性
                                            属性           值                     描述

                                            coords       坐标值               定义可点击区域（对鼠标敏感的区域）的坐标。                                      
                                            href           URL                   定义此区域的目标 URL。                                       
                                            nohref       nohref               从图像映射排除某个区域。
                                            shape           •   default        定义区域的形状。
                                                                •   rect
                                                                •   circ
                                                                •   poly    
                                            target           •   _blank         规定在何处打开 href 属性指定的目标 URL。
                                                                •   _parent
                                                                •   _self
                                                                •   _top    
                            <article> 标签规定独立的自包含内容 -- 全局属性，事件属性
                                        <article> 元素的潜在来源：
                                        •   论坛帖子
                                        •   报纸文章
                                        •   博客条目
                                        •   用户评论
                            侧栏 <aside> 标签定义其所处内容之外的内容 -- aside 的内容应该与附近的内容相关 -- 可用作文章的侧栏 -- 全局属性，事件属性
                            音频 <audio> <audio src="someaudio.wav">test </audio> 定义声音，比如音乐或其他音频流 -- 可以在开始标签和结束标签之间放置文本内容 -- 全局属性，事件属性
                                        属性                值                 描述
                                        autoplay         autoplay       如果出现该属性，则音频在就绪后马上播放。
                                        controls          controls        如果出现该属性，则向用户显示控件，比如播放按钮。
                                        loop                loop             如果出现该属性，则每当音频结束时重新开始播放。
                                        muted            muted          规定视频输出应该被静音。
                                        preload          preload         如果出现该属性，则音频在页面加载时进行加载，并预备播放。如果使用 "autoplay"，则忽略该属性。
                                        src                 url                要播放的音频的 URL。
                            粗体文本 <b> -- 全局属性
                                    根据 HTML5 规范，在没有其他合适标签更合适时，才应该把 <b> 标签作为最后的选项。HTML5 规范声明：应该
                                    使用 <h1> - <h6> 来表示标题
                                    使用 <em> 标签来表示强调的文本
                                    使用 <strong> 标签来表示重要文本
                                    使用 <mark> 标签来表示标注的/突出显示的文本。
                                    提示：您也能够使用 CSS "font-weight" 属性来设置粗体文本
                            <base> 标签为页面上的所有链接规定默认地址或默认目标      
                                    通常情况下，浏览器会从当前文档的 URL 中提取相应的元素来填写相对 URL 中的空白。
                                    使用 <base> 标签可以改变这一点。浏览器随后将不再使用当前文档的 URL，而使用指定的基本 URL 来解析所有的相对 URL。
                                    这其中包括 <a>、<img>、<link>、<form> 标签中的 URL
                                        <head>
                                        <base href="http://www.w3school.com.cn/i/" />
                                        <base target="_blank" />
                                        </head>

                                        <body>
                                        <img src="eg_smile.gif" />
                                        <a href="http://www.w3school.com.cn">W3School</a>
                                        </body>
                                        必需的属性
                                                属性                值                   描述
                                                href                URL                规定页面中所有相对链接的基准 URL。
                                        可选的属性
                                                属性               值                    描述
                                                target               •   _blank      在何处打开页面中所有的链接。
                                                                        •   _parent
                                                                        •   _self
                                                                        •   _top
                                                                        •   framename   
                            <bdi> 标签允许设置一段文本，使其脱离其父元素的文本方向设置 -- 全局属性，事件属性
                                        <ul>
                                        <li>Username <bdi>Bill</bdi>:80 points</li>
                                        <li>Username <bdo dir="rtl">Here is <bdi>Steve</bdi> some text</bdo></li>
                                        </ul>

                                        属性     值                描述
                                        dir        •   ltr           可选。规定 <bdi> 元素内的文本的文本方向。默认值：auto。
                                                    •   rtl
                                                    •   auto    
                            <bdo> 标签可覆盖默认的文本方向 <bdo dir="rtl">Here is some text</bdo>  -- 全局属性，事件属性                   
                                                    可选的属性
                                                    属性      值             描述
                                                    dir         •   ltr        定义文字的方向
                                                                 •   rtl 
                            <big> 标签呈现大号字体效果
                                        浏览器显示包含在 <big> 标签内的文字时，其字体比周围的文字要大一号。但是，如果文字已经是最大号字体，这个 <big> 标签将不起任何作用。
                                        更妙的是，可以嵌套 <big> 标签来放大文本。每一个 <big> 标签都可以使字体大一号，直到上限 7 号文本，正如字体模型所定义的那样。
                                        但是使用 <big> 标签的时候还是要小心，因为浏览器总是很宽大地试图去理解各种标签，对于那些不支持 <big> 标签的浏览器来说，它经常将其认为是粗体字标签。
                            <blockquote> 标签 标记长的引用(块引用)  -- 全局属性，事件属性  
                                    <blockquote> 与 </blockquote> 之间的所有文本都会从常规文本中分离出来，
                                    经常会在左、右两边进行缩进（增加外边距），而且有时会使用斜体。也就是说，块引用拥有它们自己的空间。                        
                            <body> 标签定义文档的主体 -- 包含文档的所有内容（比如文本、超链接、图像、表格和列表等等。）-- -- 全局属性，事件属性 
                            <br/> 可插入一个简单的换行符 -- 全局属性，事件属性 
                                        如果您希望文本流在内联表格或图像的下一行继续输出，请使用 clear 属性，
                                        该属性有三个可选的值：left、right 或者 all，每个值都代表一个边界或两边的边界。
                            <button> 标签定义一个按钮 -- 全局属性，事件属性 
                                        在 button 元素内部，可以放置内容，比如文本或图像。这是该元素与使用 input 元素创建的按钮之间的不同之处。
                                        <button> 控件 与 <input type="button"> 相比，提供了更为强大的功能和更丰富的内容。<button> 与 </button> 标签之间的所有内容
                                        都是按钮的内容，其中包括任何可接受的正文内容，比如文本或多媒体内容。例如，我们可以在按钮中包括一个图像和相关的文本，用它们在按钮中创建一个
                                        吸引人的标记图像。唯一禁止使用的元素是图像映射，因为它对鼠标和键盘敏感的动作会干扰表单按钮的行为。
                                        请始终为按钮规定 type 属性。Internet Explorer 的默认类型是 "button"，而其他浏览器中（包括 W3C 规范）的默认值是 "submit"。
                                        属性
                                                属性                  值                         描述
                                                autofocus         autofocus             规定当页面加载时按钮应当自动地获得焦点。
                                                disabled            disabled                规定应该禁用该按钮。
                                                form                 form_name           规定按钮属于一个或多个表单。
                                                formaction        url                        覆盖 form 元素的 action 属性。 注释：该属性与 type="submit" 配合使用。
                                                formenctype     见注释                   覆盖 form 元素的 enctype 属性。注释：该属性与 type="submit" 配合使用。
                                                                                                        formenctype 属性可能的值：
                                                                                                        •   application/x-www-form-urlencoded
                                                                                                        •   multipart/form-data
                                                                                                        •   text/plain
                                                formmethod     •   get                   覆盖 form 元素的 method 属性。注释：该属性与 type="submit" 配合使用。
                                                                         •   post 
                                                formnovalidate  formnovalidate     覆盖 form 元素的 novalidate 属性。 注释：该属性与 type="submit" 配合使用。
                                                formtarget        •   _blank              覆盖 form 元素的 target 属性。注释：该属性与 type="submit" 配合使用。
                                                                        •   _self
                                                                        •   _parent
                                                                        •   _top
                                                                        •   framename   
                                                name               button_name         规定按钮的名称。
                                                type                 •   button
                                                                        •   reset                 规定按钮的类型。
                                                                        •   submit  
                                                value                text                       规定按钮的初始值。可由脚本进行修改。
                            <canvas> 标签定义图形，比如图表和其他图像 -- 只是图形容器，必须使用脚本来绘制图形 -- 全局属性，事件属性
                                            属性          值             描述
                                            height      pixels        设置 canvas 的高度。
                                            width       pixels        设置 canvas 的宽度。
                                            
                                            <canvas id="myCanvas"></canvas>

                                            <script type="text/javascript">

                                            var canvas=document.getElementById('myCanvas');
                                            var ctx=canvas.getContext('2d');
                                            ctx.fillStyle='#FF0000';
                                            ctx.fillRect(0,0,80,100);

                                            </script>
                            <caption> 元素定义表格标题。标签必须紧随 table 标签之后。只能对每个表格定义一个标题。通常这个标题会被居中于表格之上。 -- 全局属性，事件属性
                            <center> 标签 对其所包括的文本进行水平居中 --请使用 CSS 样式来居中文本 -- 标准属性，事件属性 
                            <cite> 标签表示它所包含的文本对某个参考文献的引用，比如书籍或者杂志的标题 - 引用的文本将以斜体显示
                                    用 <cite> 标签把指向其他文档的引用分离出来，尤其是分离那些传统媒体中的文档，如书籍、杂志、期刊，等等。如果引用的这些文档
                                    有联机版本，还应该把引用包括在一个 <a> 标签中，从而把一个超链接指向该联机版本。
                                    <cite> 标签还有一个隐藏的功能：它可以使你或者其他人从文档中自动摘录参考书目。我们可以很容易地想象一个浏览器，它能够自动整理
                                    引用表格，并把它们作为脚注或者独立的文档来显示。<cite> 标签的语义已经远远超过了改变它所包含的文本外观的作用；它使浏览器能够
                                    以各种实用的方式来向用户表达文档的内容。
                            <em> 把文本定义为强调的内容。
                            <strong> 把文本定义为语气更强的强调的内容。
                            <dfn> 定义一个定义项目。
                            <code> 定义计算机代码文本。
                            <samp> 定义样本文本。
                            <kbd> 定义键盘文本。它表示文本是从键盘上键入的。它经常用在与计算机相关的文档或手册中。
                            <var> 定义变量。您可以将此标签与 <pre> 及 <code> 标签配合使用。
                            <col> 标签为表格中一个或多个列定义属性值 -- 只能在 table 或 colgroup 元素中使用 <col> 标签
                                        提示：请为 <col> 标签添加 class 属性。这样就可以使用 CSS 来负责对齐方式、宽度和颜色等等。
                                        提示：如果您希望在 colgroup 内部为每个列规定不同的属性值时，请使用此元素。如果没有 col 元素，列会从 colgroup 那里继承所有的属性值。
                                        注释：col 元素是仅包含属性的空元素。如需创建列，您就必须在 tr 元素内部规定 td 元素。
                                        可选的属性
                                                    属性  值   描述
                                                    align
                                                    •   right
                                                    •   left
                                                    •   center
                                                    •   justify
                                                    •   char    规定与 col 元素相关的内容的水平对齐方式。
                                                    char
                                                    character   规定根据哪个字符来对齐与 col 元素相关的内容。
                                                    charoff
                                                    number  规定第一个对齐字符的偏移量。
                                                    span
                                                    number  规定 col 元素应该横跨的列数。
                                                    valign
                                                    •   top
                                                    •   middle
                                                    •   bottom
                                                    •   baseline    定义与 col 元素相关的内容的垂直对齐方式。
                                                    width
                                                    •   pixels
                                                    •   %
                                                    •   relative_length 规定 col 元素的宽度。
                属性
                            标准属性 id, class, title, style, dir, lang, xml:lang
                            全局属性
                            事件属性 onclick, ondblclick, onmousedown, onmouseup, onmouseover, onmousemove, onmouseout, onkeypress, onkeydown, onkeyup 
  
        HTML 文档() = 网页(HTML 标签 + 纯文本)
                HTML 文档描述网页
                HTML 文档包含 HTML 标签和纯文本
                HTML 文档也被称为网页
        HTML 元素(Element) -- 从 开始标签(start tag) 到 结束标签(end tag) 的所有代码 -- 可嵌套
                    语法
                            HTML 元素以开始标签起始
                            HTML 元素以结束标签终止
                            元素的内容是开始标签与结束标签之间的内容
                            某些 HTML 元素具有空内容（empty content）
                            空元素在开始标签中进行关闭（以开始标签的结束而结束）
                            大多数 HTML 元素可拥有属性                    
                    空元素 -- 在开始标签中关闭 -- 如 <br />
                    块级元素 -- HTML 会自动地在块级元素前后添加一个额外的空行，比如段落、标题元素前后
                    HTML5 语义元素
                                        header  定义文档或节的页眉
                                        nav 定义导航链接的容器
                                        section 定义文档中的节
                                        article 定义独立的自包含文章
                                        aside   定义内容之外的内容（比如侧栏）
                                        footer  定义文档或节的页脚
                                        details 定义额外的细节
                                        summary 定义 details 元素的标题
        HTML 属性(Property) -- HTML 标签可以拥有属性 -- 属性提供了有关 HTML 元素的更多的信息
                    以 名称/值 对 的形式出现，比如：name="value"
                    在 HTML 元素的 开始标签中 规定
                    样式属性(style)
                                背景颜色-- style="background-color:yellow"
                                字体、颜色和尺寸 -- style="font-family:arial;color:red;font-size:20px;"
                                文本对齐 -- style="text-align:center"
                                控制元素显示或消失 -- style = "visibility:visible/hidden"
        HTML 文本格式化()
                    文本格式化标签
                                标签  描述
                                <b> 定义粗体文本。
                                <big>   定义大号字。
                                <em>    定义着重文字。
                                <i> 定义斜体字。
                                <small> 定义小号字。
                                <strong>    定义加重语气。
                                <sub>   定义下标字。
                                <sup>   定义上标字。
                                <ins>   定义插入字。
                                <del>   定义删除字。    
                    计算机输出标签
                                标签  描述
                                <code>  定义计算机代码。-- 支持固定的字母尺寸和间距 -- 不保留多余的空格和折行 -- 如需解决该问题，您必须在 pre 元素中包围代码
                                <kbd>   定义键盘码。 -- 支持固定的字母尺寸和间距
                                <samp>  定义计算机代码样本。 -- 支持固定的字母尺寸和间距
                                <tt>    定义打字机代码。
                                <var>   定义变量。
                                <pre>   定义预格式文本。
                    引用、引用和术语定义
                                标签  描述
                                <abbr>  定义缩写。
                                <acronym>   定义首字母缩写。
                                <address>   定义地址。
                                <bdo>   定义文字方向。
                                <blockquote>    定义长的引用。
                                <q> 定义短的引用语。
                                <cite>  定义引用、引证。
                                <dfn>   定义一个定义项目。
        HTML 样式() -- 对文档进行格式化
                    外部样式表 -- 多页面，理想的选择，通过更改一个文件来改变整个站点的外观
                                <head>
                                <link rel="stylesheet" type="text/css" href="mystyle.css">
                                </head>
                    内部样式表 -- 单个文件需要特别样式
                                    <head>
                                    <style type="text/css">
                                    body {background-color: red}
                                    p {margin-left: 20px}
                                    </style>
                                    </head>
                    内联样式 -- 特殊的样式需要应用到个别元素，在相关的标签中使用样式属性
                                <p style="color: red; margin-left: 20px">
                                This is a paragraph
                                </p>
        HTML 布局()
                    使用 <div> 元素的 HTML 布局 -- 能够轻松地通过 CSS 对其进行定位
                    使用 HTML5 的网站布局 -- TML5 提供的新语义元素定义了网页的不同部分 -- 使用 <header>, <nav>, <section>, 以及 <footer> 来创建多列布局
                    使用表格的 HTML 布局 -- 使用 <table> 元素能够取得布局效果，因为能够通过 CSS 设置表格元素的样式
        HTML 响应式 Web 设计
                    Responsive Web Design
                                RWD 指的是响应式 Web 设计（Responsive Web Design）
                                RWD 能够以可变尺寸传递网页
                                RWD 对于平板和移动设备是必需的        
                    创建响应式设计的一个方法，是自己来创建它
                    另一个创建响应式设计的方法，是使用现成的 CSS 框架 -- 使用 Bootstrap
                                另一个创建响应式设计的方法，是使用现成的 CSS 框架。
                                Bootstrap 是最流行的开发响应式 web 的 HTML, CSS, 和 JS 框架。
                                Bootstrap 帮助您开发在任何尺寸都外观出众的站点：显示器、笔记本电脑、平板电脑或手机                    
        HTML 框架() -- 通过使用框架，你可以在同一个浏览器窗口中显示不止一个页面 -- 每份HTML文档称为一个框架，并且每个框架都独立于其他的框架
                    框架结构标签 -- <frameset>
                                框架结构标签（<frameset>）定义如何将窗口分割为框架
                                每个 frameset 定义了一系列行或列
                                rows/columns 的值规定了每行或每列占据屏幕的面积
                                编者注：frameset 标签也被某些文章和书籍译为框架集。   
                    框架标签 -- <Frame> -- Frame 标签定义了放置在每个框架中的 HTML 文档
                    重要提示：不能将 <body></body> 标签与 <frameset></frameset> 标签同时使用！不过，假如你添加包含一段文本的 <noframes> 标签，
                                就必须将这段文字嵌套于 <body></body> 标签内
                    HTML Iframe  iframe 用于在网页内显示网页 -- 语法 -- <iframe src="URL"></iframe> -- URL 指向隔离页面的位置 -- 定义内联的子窗口（框架）
                                height 和 width 属性用于规定 iframe 的高度和宽度 -- 属性值的默认单位是像素，但也可以用百分比来设定（比如 "80%"）
                                实例 <iframe src="demo_iframe.htm" width="200" height="200"></iframe>
                                frameborder 属性规定是否显示 iframe 周围的边框 -- 设置属性值为 "0" 就可以移除边框
                                <iframe src="demo_iframe.htm" frameborder="0"></iframe>
        HTML 脚本() -- JavaScript 使 HTML 页面具有更强的动态和交互性
        HTML 统一资源定位器() -- URL - Uniform Resource Locator -- 网址 -- 可以由单词组成 -- 或者是因特网协议（IP）地址
                    当您点击 HTML 页面中的某个链接时，对应的 <a> 标签指向万维网上的一个地址。
                    统一资源定位器（URL）用于定位万维网上的文档（或其他数据）。        
                    网址，比如 http://www.w3school.com.cn/html/index.asp，遵守以下的语法规则：
                    scheme://host.domain:port/path/filename
                    解释：
                    scheme - 定义因特网服务的类型。最常见的类型是 http
                                URL Schemes
                                以下是其中一些最流行的 scheme：
                                Scheme  访问  用于...
                                http    超文本传输协议 以 http:// 开头的普通网页。不加密。
                                https   安全超文本传输协议   安全网页。加密所有信息交换。
                                ftp 文件传输协议  用于将文件下载或上传至网站。
                                file        您计算机上的文件。                    
                    host - 定义域主机（http 的默认主机是 www）
                    domain - 定义因特网域名，比如 w3school.com.cn
                    :port - 定义主机上的端口号（http 的默认端口号是 80）
                    path - 定义服务器上的路径（如果省略，则文档必须位于网站的根目录中）。
                    filename - 定义文档/资源的名称
        HTML 提示() - 如何查看源代码 -- 单击右键，然后选择“查看源文件”
        HTML 文档类型() -- HTML <!DOCTYPE> 声明帮助浏览器正确地显示网页 -- <!DOCTYPE> 不是 HTML 标签。它为浏览器提供一项信息（声明），即 HTML 是用什么版本编写的
        HTML 快速参考 
                    HTML Basic Document
                                <html>
                                <head>
                                <title>Document name goes here</title>
                                </head>
                                <body>
                    Visible text goes here
                                </body>
                                </html>
                                Text Elements
                                <p>This is a paragraph</p>
                                <br> (line break)
                                <hr> (horizontal rule)
                                <pre>This text is preformatted</pre>
                    Logical Styles
                                <em>This text is emphasized</em>
                                <strong>This text is strong</strong>
                                <code>This is some computer code</code>
                    Physical Styles
                                <b>This text is bold</b>
                                <i>This text is italic</i>
                    Links, Anchors, and Image Elements
                                <a href="http://www.example.com/">This is a Link</a>
                                <a href="http://www.example.com/"><img src="URL"
                                alt="Alternate Text"></a>
                                <a href="mailto:webmaster@example.com">Send e-mail</a>A named anchor:
                                <a name="tips">Useful Tips Section</a>
                                <a href="#tips">Jump to the Useful Tips Section</a>
                    Unordered list
                                <ul>
                                <li>First item</li>
                                <li>Next item</li>
                                </ul>
                    Ordered list
                                <ol>
                                <li>First item</li>
                                <li>Next item</li>
                                </ol>
                    Definition list
                                <dl>
                                <dt>First term</dt>
                                <dd>Definition</dd>
                                <dt>Next term</dt>
                                <dd>Definition</dd>
                                </dl>
                    Tables
                                <table border="1">
                                <tr>
                                  <th>someheader</th>
                                  <th>someheader</th>
                                </tr>
                                <tr>
                                  <td>sometext</td>
                                  <td>sometext</td>
                                </tr>
                                </table>
                    Frames
                                <frameset cols="25%,75%">
                                  <frame src="page1.htm">
                                  <frame src="page2.htm">
                                </frameset>
                    Forms
                                <form action="http://www.example.com/test.asp" method="post/get">
                                <input type="text" name="lastname"
                                value="Nixon" size="30" maxlength="50">
                                <input type="password">
                                <input type="checkbox" checked="checked">
                                <input type="radio" checked="checked">
                                <input type="submit">
                                <input type="reset">
                                <input type="hidden">
                                <select>
                                <option>Apples
                                <option selected>Bananas
                                <option>Cherries
                                </select>
                                <textarea name="Comment" rows="60"
                                cols="20"></textarea>
                                </form>
                    Entities
                                &lt; is the same as <
                                &gt; is the same as >
                                &#169; is the same as ©
                    Other Elements
                                <!-- This is a comment -->
                                <blockquote>
                                Text quoted from some source.
                                </blockquote>
                                <address>
                                Address 1<br>
                                Address 2<br>
                                City<br>
                                </address>        
        Web 浏览器--作用是读取 HTML 文档，并以网页的形式显示出它们。浏览器不会显示 HTML 标签，而是使用标签来解释页面的内容
                <html> 与 </html> 之间的文本描述网页
                <body> 与 </body> 之间的文本是可见的页面内容
                <h1> 与 </h1> 之间的文本被显示为标题
                <p> 与 </p> 之间的文本被显示为段落
JavaScript 教程()--网络的脚本语言 -- 用于操作 HTML 元素 -- JavaScript 由 web 浏览器来执行 -- 浏览器会在读取代码时，逐行地执行脚本代码
            JavaScript 简介() -- 特点与用途
                        用来改进设计、验证表单、检测浏览器、创建cookies，以及更多的应用
                        可用于 HTML 和 web，更可广泛用于服务器、PC、笔记本电脑、平板电脑和智能手机等设备
                        是一种轻量级的编程语言
                        可插入 HTML 页面的编程代码 
            JavaScript 使用() -- HTML 中的脚本或脚本文件必须位于 <script> ... </script> 标签内 -- <script>标签可被放置在  <body> 或 <head> 标签中
                        <script>JavaScript代码</script>
                        <script src="JavaScript文件路径"></script>  # // 放入一个单独的 .js 文件中，有利于JavaScript代码的 维护和复用--外部脚本不能包含 <script> 标签 
                        JavaScript 是所有现代浏览器以及 HTML5 中的默认脚本语言。不必在 <script> 标签中使用 type="text/javascript"
            JavaScript 运行() -- 浏览器会解释并执行位于HTML <script> 和 </script> 中的 脚本或脚本文件 -- JavaScript 由 web 浏览器来执行
            JavaScript 调试() -- Chrome浏览器 -- 开发者工具 -- 控制台 -- 可以直接输入JavaScript代码，按回车后执行
            JavaScript 语法() -- 每个语句以 ; 结束，语句块用 {...} 包裹（语句块是一组语句的集合，可以嵌套，形成层级结构），大小写敏感 -- 会忽略多余的空格--使用反斜杠对代码行进行换行
            JavaScript 输出()
                        操作 HTML 元素
                                    如需从 JavaScript 访问某个 HTML 元素，您可以使用 document.getElementById(id) 方法。
                                    请使用 "id" 属性来标识 HTML 元素，并改变其内容
                        写到文档输出 -- 使用 document.write("html代码") 仅仅向文档输出写内容--如果在文档已完成加载后执行 document.write，整个 HTML 页面将被覆盖
            JavaScript 语句() -- 向浏览器发出的命令。语句的作用是告诉浏览器该做什么 -- JavaScript 对大小写敏感
                        分号 ;
                                    分号用于分隔 JavaScript 语句。
                                    通常我们在每条可执行的语句结尾添加分号。
                                    使用分号的另一用处是在一行中编写多条语句。    
                        JavaScript 代码 -- 是 JavaScript 语句的序列        
                        JavaScript 代码块
                                    JavaScript 语句通过代码块的形式进行组合。
                                    块由左花括号开始，由右花括号结束。
                                    块的作用是使语句序列一起执行。
                                    JavaScript 函数是将语句组合在块中的典型例子     
                        JavaScript 对大小写敏感
                        空格 --  JavaScript 会忽略多余的空格。您可以向脚本添加空格，来提高其可读性
                        对代码行进行折行 -- 可以在文本字符串中使用反斜杠对代码行进行换行
            JavaScript 注释() -- 可用于提高代码的可读性、调试 -- JavaScript 不会执行注释 --  单行注释以 // 开头 --  多行注释以 /* 开始，以 */ 结尾
            JavaScript 变量() -- 变量是存储信息的容器 -- "var 关键词来声明（创建）变量 -- 使用等号向变量赋值 -- 可以一条语句，多个变量（以 var 开头，并使用逗号分隔变量）"
                        "一个好的编程习惯是，在代码开始处，统一对需要的变量进行声明"
                        使用等号=对变量进行赋值。可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量，但是要注意只能用var申明一次
                        Value = undefined -- 在计算机程序中，经常会声明无值的变量。未使用值来声明的变量，其值实际上是 undefined

                        
                        局部变量 -- 函数内部声明的变量（使用 var）是局部变量，所以只能在函数内部访问它 -- 只要函数运行完毕，本地变量就会被删除
                        全局变量 -- 在函数外声明的变量（使用 var）是全局变量，不使用 var 申明的变量皆为全局变量，网页上的所有脚本和函数都能访问它 - 全局变量会绑定到window上

                        JavaScript 变量的生存期
                                    JavaScript 变量的生命期从它们被声明的时间开始。
                                    局部变量会在函数运行以后被删除。
                                    全局变量会在页面关闭后被删除。   

                        名字空间 -- 全局变量会绑定到window上，不同的JavaScript文件如果使用了相同的全局变量，或者定义了相同名字的顶层函数，都会造成命名冲突，并且很难被发现
                                    减少冲突的一个方法是把自己的所有变量和函数全部绑定到一个全局变量中
                                                // 唯一的全局变量MYAPP:
                                                var MYAPP = {};

                                                // 其他变量:
                                                MYAPP.name = 'myapp';
                                                MYAPP.version = 1.0;

                                                // 其他函数:
                                                MYAPP.foo = function () {
                                                    return 'foo';
                                                };        
                                                把自己的代码全部放入唯一的名字空间MYAPP中，会大大减少全局变量冲突的可能                            
                        块级作用域

                        在函数内部首先申明所有变量
                        不同函数内部的同名变量互相独立，互不影响
                        函数可以嵌套，此时，内部函数可以访问外部函数定义的变量，反过来则不行
                        函数在查找变量时从自身函数定义开始，从“内”向“外”查找。如果内部函数定义了与外部函数重名的变量，则内部函数的变量将“屏蔽”外部函数的变量


                        strict模式，在strict模式下运行的JavaScript代码，强制通过var申明变量，未使用var申明变量就使用的，将导致运行错误
                                    启用strict模式的方法是在JavaScript代码的第一行写上：
                                    'use strict'; -- 不支持strict模式的浏览器会把它当做一个字符串语句执行，支持strict模式的浏览器将开启strict模式运行JavaScript             
            JavaScript 数据类型() -- 字符串、数字、布尔值、数组、对象、Null、Undefined -- JavaScript 拥有动态类型（相同的变量可用作不同的类型） -- 变量均为对象
                        字符串 -- 以单引号 " ' " 或双引号 ' " '括起来的任意文本
                                ·   转义字符 '\ ' -- 可以转义很多字符，'比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\。'
                                                ASCII字符可以以\x##形式的十六进制表示，例如：
                                                '\x41'; // 完全等同于 'A'
                                                还可以用\u####表示一个Unicode字符：
                                                '\u4e2d\u6587'; // 完全等同于 '中文'                      
                                    多行字符串 -- 用反引号 ` ... ` 表示 -- 由于多行字符串用\n写起来比较费事，所以最新的ES6标准新增了一种多行字符串的表示方法，用` ... `表示   
                                    模板字符串$ -- ${变量} -- 如果有很多变量需要连接，用+号就比较麻烦。ES6新增了一种模板字符串
                                                要把多个字符串连接起来，可以用+号连接  
                                                            var name = '小明';
                                                            var age = 20;
                                                            var message = '你好, ' + name + ', 你今年' + age + '岁了!';
                                                            alert(message);      
                                                模板字符串$ ` ` -- 非模板字符串不会替换变量
                                                            var name = '小明';
                                                            var age = 20;
                                                            var message = `你好, ${name}, 你今年${age}岁了!`;
                                                            alert(message);                                                                                          
                                    操作字符串
                                                获取字符串某个指定位置的字符 -- 变量[索引]-- 字符串是不可变的，如果对字符串的某个索引赋值，不会有任何错误，但也没有任何效果
                                                变量.length  返回字符串长度
                                                变量.toUpperCase() 把一个字符串全部变为大写
                                                变量.toLowerCase() 把一个字符串全部变为小写
                                                变量.indexOf() 搜索指定字符串出现的位置
                                                            var s = 'hello, world';
                                                            s.indexOf('world'); // 返回7
                                                            s.indexOf('World'); // 没有找到指定的子串，返回 -1                 
                                                变量.substring() 返回指定索引区间的子串               
                                                            var s = 'hello, world'
                                                            s.substring(0, 5); // 从索引0开始到5（不包括5），返回'hello'
                                                            s.substring(7); // 从索引7开始到结束，返回'world'                                                                
                        数字 -- JavaScript不区分整数和浮点数，统一用Number表示
                                •   123; // 整数123
                                •   0.456; // 浮点数0.456
                                •   1.2345e3; // 科学计数法表示1.2345x1000，等同于1234.5
                                •   -99; // 负数
                                •   NaN; // NaN表示Not a Number，当无法计算结果时用NaN表示 -- NaN这个特殊的Number与所有其他值都不相等，包括它自己
                                            •   NaN === NaN; // false
                                            •   唯一能判断NaN的方法是通过isNaN()函数：
                                            •   isNaN(NaN); // true                                
                                •   Infinity; // Infinity表示无限大，当数值超过了JavaScript的Number所能表示的最大值时，就表示为Infinity
                                •   计算机由于使用二进制，所以，有时候用十六进制表示整数比较方便，十六进制用0x前缀和0-9，a-f表示，例如：0xff00，
                                        0xa5b4c3d2，等等，它们和十进制表示的数值完全一样。
                                •   Number可以直接做四则运算，规则和数学一致                                                     
                        布尔值 -- true、false两种值，布尔运算 -- && 与运算 -- || 或运算 -- ! 非运算
                        数组 -- 是一组按顺序排列的集合，用 [] 表示，元素之间用 , 分隔 -- 集合的每个值称为元素 -- 可以包括任意数据类型 -- 也可以通过Array()函数 创建数组
                                    创建方式
                                                [1, 2, 3.14, 'Hello', null, true]; // 出于代码的可读性考虑，强烈建议直接使用 []
                                                new Array(1, 2, 3); // 创建了数组[1, 2, 3]
                                    操作数据
                                                要取得Array的长度，直接访问length属性 -- 直接给Array的 length 赋一个新的值会导致Array大小的变化
                                                            var arr = [1, 2, 3];
                                                            arr.length; // 3
                                                            arr.length = 6;
                                                            arr; // arr变为[1, 2, 3, undefined, undefined, undefined]
                                                            arr.length = 2;
                                                            arr; // arr变为[1, 2]    
                                                访问数组元素 -- 数组变量[索引]     
                                                修改数组元素 -- 数组变量[索引] = new_value -- 通过索引把对应的元素修改为新的值 
                                                            var arr = ['A', 'B', 'C'];
                                                            arr[1] = 99;
                                                            arr; // arr现在变为['A', 99, 'C']
                                                            通过索引赋值时，索引超过了范围，同样会引起Array大小的变化
                                                                        var arr = [1, 2, 3];
                                                                        arr[5] = 'x';
                                                                        arr; // arr变为[1, 2, 3, undefined, undefined, 'x']
                                                indexOf() -- 搜索一个指定的元素的位置
                                                slice(起始索引，终止索引) -- 截取Array的部分元素，然后返回一个新的Array -- 左闭右开
                                                            var arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];
                                                            arr.slice(0, 3); // 从索引0开始，到索引3结束，但不包括索引3: ['A', 'B', 'C']
                                                            arr.slice(3); // 从索引3开始到结束: ['D', 'E', 'F', 'G']    
                                                push()  向Array的末尾添加若干元素
                                                pop()  则把Array的最后一个元素删除掉               
                                                unshift()方法  往Array的头部添加若干元素
                                                shift()方法  则把Array的第一个元素删掉
                                                sort() 可以对当前Array进行排序 -- 它会直接修改当前Array的元素位置，直接调用时，按照默认顺序排序          
                                                reverse() 把整个Array的元素给掉个个，也就是反转  
                                                splice()方法  是修改Array的“万能方法”，它可以从指定的索引开始删除若干元素，然后再从该位置添加若干元素
                                                            var arr = ['Microsoft', 'Apple', 'Yahoo', 'AOL', 'Excite', 'Oracle'];
                                                            // 从索引2开始删除3个元素,然后再添加两个元素:
                                                            arr.splice(2, 3, 'Google', 'Facebook'); // 返回删除的元素 ['Yahoo', 'AOL', 'Excite']
                                                            arr; // ['Microsoft', 'Apple', 'Google', 'Facebook', 'Oracle']
                                                            // 只删除,不添加:
                                                            arr.splice(2, 2); // ['Google', 'Facebook']
                                                            arr; // ['Microsoft', 'Apple', 'Oracle']
                                                            // 只添加,不删除:
                                                            arr.splice(2, 0, 'Google', 'Facebook'); // 返回[],因为没有删除任何元素
                                                            arr; // ['Microsoft', 'Apple', 'Google', 'Facebook', 'Oracle']                                                
                                                concat()方法  把当前的Array和另一个Array连接起来，并返回一个新的Array
                                                join()方法  是一个非常实用的方法，它把当前Array的每个元素都用指定的字符串连接起来，然后返回连接后的字符串
                                                            var arr = ['A', 'B', 'C', 1, 2, 3];
                                                            arr.join('-'); // 'A-B-C-1-2-3'             
                                    多维数组                               
                                    数组的元素可以通过索引来访问。请注意，索引的起始值为0
                        对象 -- 是一组由 键 : 值 组成的无序集合 -- 键都是字符串类型，值可以是任意数据类型 -- 对象属性（对象变量.属性名）-- 对象方法（对象变量.方法名()）-- 详见后述
                        Map -- 是一组键值对的结构，具有极快的查找速度 -- Number或者其他数据类型作为键
                                    初始化Map需要一个二维数组，或者直接初始化一个空Map -- var m = new Map(); // 空Map
                                    方法
                                                m.set('Adam', 67); // 添加新的key-value
                                                m.set('Bob', 59); // 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
                                                m.has('Adam'); // 是否存在key 'Adam': true
                                                m.get('Adam'); // 67
                                                m.delete('Adam'); // 删除key 'Adam'
                                                m.get('Adam'); // undefined             
                        Set --  是一组key的集合，但不存储value -- 由于key不能重复，所以，在Set中，没有重复的key -- 重复元素在Set中自动被过滤        
                                    要创建一个Set，需要提供一个Array作为输入，或者直接创建一个空Set
                                                var s1 = new Set(); // 空Set
                                                var s2 = new Set([1, 2, 3]); // 含1, 2, 3         
                                    操作                           
                                                add(key)方法可以添加元素到Set中，可以重复添加，但不会有效果
                                                delete(key)方法可以删除元素
                        Null -- 表示一个“空”的值 -- 它和0以及空字符串''不同，0是一个数值，''表示长度为0的字符串，而null表示“空
                                    在其他语言中，也有类似JavaScript的null的表示，
                                    例如Java也用null，Swift用nil，Python用None表示                        
                        Undefined -- 表示“未定义”

                        iterable类型 -- Array、Map和Set都属于iterable类型 -- 具有iterable类型的集合可以通过新的 for ... of循环来遍历
                                    for ... of 循环和 for ... in 循环有何区别
                                                for ... in 循环
                                                            由于历史遗留问题，它遍历的实际上是对象的属性名称。一个Array数组实际上也是一个对象，
                                                            它的每个元素的索引被视为一个属性。

                                                            当我们手动给Array对象添加了额外的属性后，for ... in循环将带来意想不到的意外效果：

                                                            var a = ['A', 'B', 'C'];
                                                            a.name = 'Hello';
                                                            for (var x in a) {
                                                                alert(x); // '0', '1', '2', 'name'
                                                            }
                                                            for ... in循环将把name包括在内，但Array的length属性却不包括在内。
                                                for ... of 循环则完全修复了这些问题，它只循环集合本身的元素：

                                                            var a = ['A', 'B', 'C'];
                                                            a.name = 'Hello';
                                                            for (var x of a) {
                                                                alert(x); // 'A', 'B', 'C'
                                                            }     
                                    iterable内置的 forEach 方法 -- 接收一个函数，每次迭代就自动回调该函数  -- 参数名字是不固定，但是位置是固定的 -- 参数不用声明
                                                以Array为例：

                                                            var a = ['A', 'B', 'C'];
                                                            a.forEach(function (element, index, array) {
                                                                // element: 指向当前元素的值
                                                                // index: 指向当前索引
                                                                // array: 指向Array对象本身
                                                                alert(element);
                                                            });             
                                                Set与Array类似，但Set没有索引，因此回调函数的前两个参数都是元素本身
                                                            var s = new Set(['A', 'B', 'C']);
                                                            s.forEach(function (element, sameElement, set) {
                                                                alert(element);
                                                            });    
                                                Map的回调函数参数依次为value、key和map本身：

                                                            var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
                                                            m.forEach(function (value, key, map) {
                                                                alert(value);
                                                            });                                                                                                                                                     
                                                
                                                如果对某些参数不感兴趣，由于JavaScript的函数调用不要求参数必须一致，因此可以忽略它们。例如，只需要获得Array的element：

                                                            var a = ['A', 'B', 'C'];
                                                            a.forEach(function (element) {
                                                                alert(element);
                                                            });            
            JavaScript 对象() -- JavaScript 中的所有事物都是对象 -- 对象是拥有属性和方法的特殊数据类型 -- 属性是与对象相关的值 -- 方法是能够在对象上执行的动作
                        {...}  表示一个对象，键值对以xxx: xxx形式申明，用,隔开
                        内建对象 -- 如 String、Date、Array 等
                        访问对象的属性 -- 属性是与对象相关的值 -- 语法 -- objectName.propertyName -- 如果属性名包含特殊字符 - 则 objectName['propertyName']
                                    JavaScript的对象是动态类型，你可以自由地给一个对象添加或删除属性
                                                var xiaoming = {
                                                    name: '小明'
                                                };
                                                xiaoming.age; // undefined
                                                xiaoming.age = 18; // 新增一个age属性
                                                xiaoming.age; // 18
                                                delete xiaoming.age; // 删除age属性
                                                xiaoming.age; // undefined
                                                delete xiaoming['name']; // 删除name属性
                                                xiaoming.name; // undefined
                                                delete xiaoming.school; // 删除一个不存在的school属性也不会报错                                    
                                    访问不存在的属性不报错，而是返回undefined
                                    检测对象是否拥有某一属性，可以用in操作符
                                                var xiaoming = {
                                                    name: '小明',
                                                    birth: 1990,
                                                    school: 'No.1 Middle School',
                                                    height: 1.70,
                                                    weight: 65,
                                                    score: null
                                                };
                                                'name' in xiaoming; // true
                                                'grade' in xiaoming; // false
                                    不过要小心，如果in判断一个属性存在，这个属性不一定是xiaoming的，它可能是xiaoming继承得到的：

                                                'toString' in xiaoming; // true
                                                因为toString定义在object对象中，而所有对象最终都会在原型链上指向object，所以xiaoming也拥有toString属性。
                                    要判断一个属性是否是xiaoming自身拥有的，而不是继承得到的，可以用hasOwnProperty()方法：

                                                var xiaoming = {
                                                    name: '小明'
                                                };
                                                xiaoming.hasOwnProperty('name'); // true
                                                xiaoming.hasOwnProperty('toString'); // false                                    
                        访问对象的方法 -- 方法是能够在对象上执行的动作 -- 语法 -- objectName.methodName()
                        创建 JavaScript 对象
                                    JavaScript对每个创建的对象都会设置一个原型，指向它的原型对象
                                                当我们用obj.xxx访问一个对象的属性时，JavaScript引擎先在当前对象上查找该属性，如果没有找到，
                                                就到其原型对象上找，如果还没有找到，就一直上溯到Object.prototype对象，最后，如果还没有找到，就只能返回undefined        
                                                例如，创建一个Array对象：
                                                var arr = [1, 2, 3];
                                                其原型链是：
                                                arr ----> Array.prototype ----> Object.prototype ----> null                       

                                                当我们创建一个函数时：
                                                function foo() {
                                                    return 0;
                                                }
                                                函数也是一个对象，它的原型链是：
                                                foo ----> Function.prototype ----> Object.prototype ----> null                                                     
                                    定义并创建对象的实例
                                                实例
                                                            person=new Object();
                                                            person.firstname="Bill";
                                                            person.lastname="Gates";
                                                            person.age=56;
                                                            person.eyecolor="blue";                     
                                                实例
                                                            person={firstname:"John",lastname:"Doe",age:50,eyecolor:"blue"};               
                                    使用函数来定义对象，然后创建新的对象实例 -- 使用对象构造器
                                                实例
                                                            function person(firstname,lastname,age,eyecolor)
                                                            {
                                                            this.firstname=firstname;
                                                            this.lastname=lastname;
                                                            this.age=age;
                                                            this.eyecolor=eyecolor;
                                                            }
                                                创建 JavaScript 对象实例
                                                            一旦您有了对象构造器，就可以创建新的对象实例，就像这样：
                                                            var myFather=new person("Bill","Gates",56,"blue");
                                                            var myMother=new person("Steve","Jobs",48,"green");
                                    把属性添加到 JavaScript 对象
                                                您可以通过为对象赋值，向已有对象添加新属性：
                                                假设 personObj 已存在 - 您可以为其添加这些新属性：firstname、lastname、age 以及 eyecolor：
                                                person.firstname="Bill";
                                                person.lastname="Gates";
                                                person.age=56;
                                                person.eyecolor="blue";

                                                x=person.firstname;
                                                在以上代码执行后，x 的值将是：
                                                Bill
                                    把方法添加到 JavaScript 对象
                                                方法只不过是附加在对象上的函数。
                                                在构造器函数内部定义对象的方法：
                                                function person(firstname,lastname,age,eyecolor)
                                                {
                                                this.firstname=firstname;
                                                this.lastname=lastname;
                                                this.age=age;
                                                this.eyecolor=eyecolor;

                                                this.changeName=changeName;
                                                function changeName(name)
                                                {
                                                this.lastname=name;
                                                }
                                                }
                                                changeName() 函数 name 的值赋给 person 的 lastname 属性。
                                                现在您可以试一下：
                                                myMother.changeName("Ballmer");            
                        typeof 操作符获取对象的类型 -- 它总是返回一个字符串
                                    typeof 123; // 'number'
                                    typeof NaN; // 'number'
                                    typeof 'str'; // 'string'
                                    typeof true; // 'boolean'
                                    typeof undefined; // 'undefined'
                                    typeof Math.abs; // 'function'
                                   
                                    typeof null; // 'object'
                                    typeof []; // 'object'
                                    typeof {}; // 'object'           
                                    可见，number、string、boolean、function和undefined有别于其他类型。
                                    特别注意null的类型是object，Array的类型也是object，
                                    如果我们用typeof，将无法区分出null、Array和通常意义上的object {}                                                 
                        包装对象 -- 包装对象用 new 创建 -- number、boolean和string都有包装对象 -- 最好不要使用
                                    除了这些类型外，JavaScript还提供了包装对象，熟悉Java的小伙伴肯定很清楚int和Integer这种暧昧关系。
                                                number、boolean和string都有包装对象。没错，在JavaScript中，字符串也区分string类型和它的包装类型。包装对象用new创建：
                                                var n = new Number(123); // 123,生成了新的包装类型
                                                var b = new Boolean(true); // true,生成了新的包装类型
                                                var s = new String('str'); // 'str',生成了新的包装类型
                                    虽然包装对象看上去和原来的值一模一样，显示出来也是一模一样，但他们的类型已经变为object了！所以，包装对象和原始值用===比较会返回false：
                                                typeof new Number(123); // 'object'
                                                new Number(123) === 123; // false

                                                typeof new Boolean(true); // 'object'
                                                new Boolean(true) === true; // false

                                                typeof new String('str'); // 'object'
                                                new String('str') === 'str'; // false
                                    所以闲的蛋疼也不要使用包装对象！尤其是针对string类型！！！
                                    如果我们在使用Number、Boolean和String时，没有写new会发生什么情况？
                                                此时，Number()、Boolean和String()被当做普通函数，把任何类型的数据转换为number、boolean和string类型（注意不是其包装类型）：
                                                var n = Number('123'); // 123，相当于parseInt()或parseFloat()
                                                typeof n; // 'number'

                                                var b = Boolean('true'); // true
                                                typeof b; // 'boolean'

                                                var b2 = Boolean('false'); // true! 'false'字符串转换结果为true！因为它是非空字符串！
                                                var b3 = Boolean(''); // false

                                                var s = String(123.45); // '123.45'
                                                typeof s; // 'string'
                                                是不是感觉头大了？这就是JavaScript特有的催眠魅力！
                                    总结一下，有这么几条规则需要遵守：
                                                •   不要使用new Number()、new Boolean()、new String()创建包装对象；
                                                •   用parseInt()或parseFloat()来转换任意类型到number；
                                                •   用String()来转换任意类型到string，或者直接调用某个对象的toString()方法；
                                                •   通常不必把任意类型转换为boolean再判断，因为可以直接写if (myVar) {...}；
                                                •   typeof操作符可以判断出number、boolean、string、function和undefined；
                                                •   判断Array要使用Array.isArray(arr)；
                                                •   判断null请使用myVar === null；
                                                •   判断某个全局变量是否存在用typeof window.myVar === 'undefined'；
                                                •   函数内部判断某个变量是否存在用typeof myVar === 'undefined'。
                                                最后有细心的同学指出，任何对象都有toString()方法吗？null和undefined就没有！确实如此，这两个特殊值要除外，虽然null还伪装成了object类型。
                                                更细心的同学指出，number对象调用toString()报SyntaxError：
                                                123.toString(); // SyntaxError
                                                遇到这种情况，要特殊处理一下：
                                                123..toString(); // '123', 注意是两个点！ -- 因为第一个点是指小数点，第二个点才是调用toString()方法，所以3.14不需要用两个点调用toString()方法
                                                (123).toString(); // '123'
                                    不要问为什么，这就是JavaScript代码的乐趣！
            JavaScript 面向对象编程() -- 
                        面向对象的两个基本概念
                                    1.  类：类是对象的类型模板，例如，定义Student类来表示学生，类本身是一种类型，Student表示学生类型，但不表示任何具体的某个学生；
                                    2.  实例：实例是根据类创建的对象，例如，根据Student类可以创建出xiaoming、xiaohong、xiaojun等多个实例，每个实例表示一个具体的学生，他们全都属于Student类型。
                                    
                                    JavaScript不区分类和实例的概念，而是通过原型（prototype）来实现面向对象编程
                                    JavaScript的原型链和Java的Class区别就在，它没有“Class”的概念，所有对象都是实例，所谓继承关系不过是把一个对象的原型指向另一个对象而已           
                        创建对象 -- JavaScript 对每个创建的对象都会设置一个原型，指向它的原型对象
                                    直接用 { ... } 创建一个对象
                                    用构造函数创建对象 -- new 关键字
                                                先定义一个构造函数：
                                                            function Student(name) {
                                                                this.name = name;
                                                                this.hello = function () {
                                                                    alert('Hello, ' + this.name + '!');
                                                                }
                                                            }
                                                            你会问，咦，这不是一个普通函数吗？
                                                这确实是一个普通函数，但是在JavaScript中，可以用关键字new来调用这个函数，并返回一个对象：
                                                            var xiaoming = new Student('小明');
                                                            xiaoming.name; // '小明'
                                                            xiaoming.hello(); // Hello, 小明!
                                                注意，如果不写new，这就是一个普通函数，它返回undefined。但是，如果写了new，它就变成了一个构造函数，它绑定的this
                                                            指向新创建的对象，并默认返回this，也就是说，不需要在最后写return this;。
                                                新创建的xiaoming的原型链是：xiaoming ----> Student.prototype ----> Object.prototype ----> null
                                                用new Student()创建的对象还从原型上获得了一个constructor属性，它指向函数Student本身：
                                                            xiaoming.constructor === Student.prototype.constructor; // true
                                                            Student.prototype.constructor === Student; // true

                                                            Object.getPrototypeOf(xiaoming) === Student.prototype; // true

                                                            xiaoming instanceof Student; // true
                                                现在我们就认为xiaoming、xiaohong这些对象“继承”自Student。
                                                不过还有一个小问题，注意观察：
                                                            xiaoming.name; // '小明'
                                                            xiaohong.name; // '小红'
                                                            xiaoming.hello; // function: Student.hello()
                                                            xiaohong.hello; // function: Student.hello()
                                                            xiaoming.hello === xiaohong.hello; // false

                                                            xiaoming和xiaohong各自的name不同，这是对的，否则我们无法区分谁是谁了。
                                                            xiaoming和xiaohong各自的hello是一个函数，但它们是两个不同的函数，虽然函数名称和代码都是相同的！
                                                            如果我们通过new Student()创建了很多对象，这些对象的hello函数实际上只需要共享同一个函数就可以了，这样
                                                            可以节省很多内存。
                                                要让创建的对象共享一个hello函数，根据对象的属性查找原则，我们只要把hello函数移动到xiaoming、xiaohong
                                                这些对象共同的原型上就可以了，也就是Student.prototype

                                                            修改代码如下：
                                                            function Student(name) {
                                                                this.name = name;
                                                            }

                                                            Student.prototype.hello = function () {
                                                                alert('Hello, ' + this.name + '!');
                                                            };
                                                            用new创建基于原型的JavaScript的对象就是这么简单！
                                                            xiaoming.hello === xiaohong.hello; // true
                        对象属性的查找原则
                                    当我们用obj.xxx访问一个对象的属性时，JavaScript引擎先在当前对象上查找该属性，如果没有找到，就到其原型对象上找，如果还没有找到，
                                    就一直上溯到Object.prototype对象，最后，如果还没有找到，就只能返回undefined
                                                例如，创建一个Array对象：
                                                            var arr = [1, 2, 3];
                                                其原型链是：
                                                            arr ----> Array.prototype ----> Object.prototype ----> null
                                                            Array.prototype定义了indexOf()、shift()等方法，因此你可以在所有的Array对象上直接调用这些方法。
                                                当我们创建一个函数时：
                                                            function foo() {
                                                                return 0;
                                                            }
                                                函数也是一个对象，它的原型链是：
                                                            foo ----> Function.prototype ----> Object.prototype ----> null
                                                            由于Function.prototype定义了apply()等方法，因此，所有函数都可以调用apply()方法。
                                                            很容易想到，如果原型链很长，那么访问一个对象的属性就会因为花更多的时间查找而变得更慢，因此要注意不要把原型链搞得太长。
                        原型继承
                                    在传统的基于Class的语言如Java、C++中，继承的本质是扩展一个已有的Class，并生成新的Subclass。
                                    由于这类语言严格区分类和实例，继承实际上是类型的扩展。但是，JavaScript由于采用原型继承，我们无法直接扩展一个Class，因为根本不存在Class这种类型。
                                    但是办法还是有的。我们先回顾Student构造函数：
                                                function Student(props) {
                                                    this.name = props.name || 'Unnamed';
                                                }

                                                Student.prototype.hello = function () {
                                                    alert('Hello, ' + this.name + '!');
                                                }
                                    以及Student的原型链：
                                     
                                    现在，我们要基于Student扩展出PrimaryStudent，可以先定义出PrimaryStudent：
                                                function PrimaryStudent(props) {
                                                    // 调用Student构造函数，绑定this变量:
                                                    Student.call(this, props);
                                                    this.grade = props.grade || 1;
                                                }
                                    但是，调用了Student构造函数不等于继承了Student，PrimaryStudent创建的对象的原型是：
                                    new PrimaryStudent() ----> PrimaryStudent.prototype ----> Object.prototype ----> null
                                    必须想办法把原型链修改为：
                                    new PrimaryStudent() ----> PrimaryStudent.prototype ----> Student.prototype ----> Object.prototype ----> null
                                    这样，原型链对了，继承关系就对了。新的基于PrimaryStudent创建的对象不但能调用PrimaryStudent.prototype定义的方法，也可以调用Student.prototype定义的方法。
                                    如果你想用最简单粗暴的方法这么干：
                                                PrimaryStudent.prototype = Student.prototype;
                                                是不行的！如果这样的话，PrimaryStudent和Student共享一个原型对象，那还要定义PrimaryStudent干啥？

                                    我们必须借助一个中间对象来实现正确的原型链，这个中间对象的原型要指向Student.prototype。为了实现这一点，参考道爷（就是发明JSON的那个道格拉斯）的代码，中间对象可以用一个空函数F来实现：
                                                // PrimaryStudent构造函数:
                                                            function PrimaryStudent(props) {
                                                                Student.call(this, props);
                                                                this.grade = props.grade || 1;
                                                            }

                                                // 空函数F:
                                                            function F() {
                                                            }

                                                // 把F的原型指向Student.prototype:

                                                            F.prototype = Student.prototype;

                                                // 把PrimaryStudent的原型指向一个新的F对象，F对象的原型正好指向Student.prototype:

                                                            PrimaryStudent.prototype = new F();

                                                // 把PrimaryStudent原型的构造函数修复为PrimaryStudent:

                                                            PrimaryStudent.prototype.constructor = PrimaryStudent;

                                                // 继续在PrimaryStudent原型（就是new F()对象）上定义方法：
                                                            PrimaryStudent.prototype.getGrade = function () {
                                                                return this.grade;
                                                            };

                                                // 创建xiaoming:
                                                            var xiaoming = new PrimaryStudent({
                                                                name: '小明',
                                                                grade: 2
                                                            });
                                                            xiaoming.name; // '小明'
                                                            xiaoming.grade; // 2

                                                // 验证原型:
                                                            xiaoming.__proto__ === PrimaryStudent.prototype; // true
                                                            xiaoming.__proto__.__proto__ === Student.prototype; // true

                                                // 验证继承关系:
                                                            xiaoming instanceof PrimaryStudent; // true
                                                            xiaoming instanceof Student; // true
                                                            用一张图来表示新的原型链：
                                     
                                    注意，函数F仅用于桥接，我们仅创建了一个new F()实例，而且，没有改变原有的Student定义的原型链。
                                    如果把继承这个动作用一个inherits()函数封装起来，还可以隐藏F的定义，并简化代码：
                                                function inherits(Child, Parent) {
                                                    var F = function () {};
                                                    F.prototype = Parent.prototype;
                                                    Child.prototype = new F();
                                                    Child.prototype.constructor = Child;
                                                }
                                    这个inherits()函数可以复用：
                                                function Student(props) {
                                                    this.name = props.name || 'Unnamed';
                                                }

                                                Student.prototype.hello = function () {
                                                    alert('Hello, ' + this.name + '!');
                                                }

                                                function PrimaryStudent(props) {
                                                    Student.call(this, props);
                                                    this.grade = props.grade || 1;
                                                }

                                    // 实现原型继承链:
                                                inherits(PrimaryStudent, Student);

                                                // 绑定其他方法到PrimaryStudent原型:
                                                PrimaryStudent.prototype.getGrade = function () {
                                                    return this.grade;
                                                };
                                    小结
                                                JavaScript的原型继承实现方式就是：
                                                1.  定义新的构造函数，并在内部用call()调用希望“继承”的构造函数，并绑定this；
                                                2.  借助中间函数F实现原型链继承，最好通过封装的inherits函数完成；
                                                3.  继续在新的构造函数的原型上定义新方法。
                                    评论
                                                •    
                                                JavaScript真能穷对付...
                                                匿名sina网友V created at 2016-10-16 19:11, Last updated at 1-22 19:27
                                                上个教程里学到了构造函数加原型的方式创建对象. 这个教程里学到了以构造原型链为目标的原型式继承.
                                                虽然掌握不了原型式继承的写法,好在理解了它的思路.
                                                也是服了javascript了,明明力不从心还死撑,穷对付着硬上. 这样野路子的创建对象,这样野路子的实现继承,当初还不如设计成主流的继承方式.
                                                Brendan Eich这哥们简直是在犯罪,就冲这样的创建对象和实现继承方式就应该击毙了他.
                        class继承
                                    在上面的章节中我们看到了JavaScript的对象模型是基于原型实现的，特点是简单，缺点是理解起来比传统的类－实例模型要困难，
                                    最大的缺点是继承的实现需要编写大量代码，并且需要正确实现原型链。
                                    有没有更简单的写法？有！
                                    新的关键字class从ES6开始正式被引入到JavaScript中。class的目的就是让定义类更简单。
                                    我们先回顾用函数实现Student的方法：
                                                function Student(name) {
                                                    this.name = name;
                                                }

                                                Student.prototype.hello = function () {
                                                    alert('Hello, ' + this.name + '!');
                                                }
                                    如果用新的class关键字来编写Student，可以这样写：
                                                class Student {
                                                    constructor(name) {
                                                        this.name = name;
                                                    }

                                                    hello() {
                                                        alert('Hello, ' + this.name + '!');
                                                    }
                                                }
                                    比较一下就可以发现，class的定义包含了构造函数constructor和定义在原型对象上的函数hello()（注意没有function关键字），这样就避免了Student.prototype.hello = function () {...}这样分散的代码。
                                    最后，创建一个Student对象代码和前面章节完全一样：
                                                var xiaoming = new Student('小明');
                                                xiaoming.hello();
                                    class继承
                                    用class定义对象的另一个巨大的好处是继承更方便了。想一想我们从Student派生一个PrimaryStudent需要编写的代码量。
                                    现在，原型继承的中间对象，原型对象的构造函数等等都不需要考虑了，直接通过extends来实现：
                                                class PrimaryStudent extends Student {
                                                    constructor(name, grade) {
                                                        super(name); // 记得用super调用父类的构造方法!
                                                        this.grade = grade;
                                                    }

                                                    myGrade() {
                                                        alert('I am at grade ' + this.grade);
                                                    }
                                                }
                                    注意PrimaryStudent的定义也是class关键字实现的，而extends则表示原型链对象来自Student。子类的构造函数可能会与
                                    父类不太相同，例如，PrimaryStudent需要name和grade两个参数，并且需要通过super(name)来调用父类的构造函数，
                                    否则父类的name属性无法正常初始化。
                                    PrimaryStudent已经自动获得了父类Student的hello方法，我们又在子类中定义了新的myGrade方法。
                                    ES6引入的class和原有的JavaScript原型继承有什么区别呢？实际上它们没有任何区别，class的作用就是让JavaScript引擎去实现
                                    原来需要我们自己编写的原型链代码。简而言之，用class的好处就是极大地简化了原型链代码。
                                    你一定会问，class这么好用，能不能现在就用上？
                                                现在用还早了点，因为不是所有的主流浏览器都支持ES6的class。如果一定要现在就用上，就需要一个工具把class代码转换为传统的
                                                prototype代码，可以试试Babel这个工具。

            JavaScript 函数() -- 函数是由事件驱动的或被调用时执行的可重复使用代码块 -- 参数数量随意，但出现顺序需一致
                        JavaScript 函数语法
                                    函数就是包裹在花括号中的代码块，前面使用了"关键词 function" 申明函数 -- 当调用该函数时，会执行函数内的代码 -- 块的作用是使语句序列一起执行
                                    function functionname(arguments)         //  可以发送任意多的参数，由逗号 (,) 分隔
                                    {
                                    这里是要执行的代码                                  //  如果没有return语句，函数执行完毕后也会返回结果，只是结果为undefined
                                    }                                                              //  return 后 整个 JavaScript 并不会停止执行，仅仅是函数。JavaScript 将继续执行代码，从调用函数的地方
                        函数定义
                                    第一种方式
                                                function abs(x) {
                                                    if (x >= 0) {
                                                        return x;
                                                    } else {
                                                        return -x;
                                                    }
                                                }
                                                上述abs()函数的定义如下：
                                                function指出这是一个函数定义；
                                                abs是函数的名称；
                                                (x)括号内列出函数的参数，多个参数以,分隔；
                                                { ... }之间的代码是函数体，可以包含若干语句，甚至可以没有任何语句。                                    
                                    第二种定义 -- 函数也是一个对象，上述定义的abs()函数实际上是一个函数对象，而函数名abs可以视为指向该函数的变量
                                                    var abs = function (x) {
                                                        if (x >= 0) {
                                                            return x;
                                                        } else {
                                                            return -x;
                                                        }
                                                    };                                                    
                                                    在这种方式下，function (x) { ... }是一个匿名函数，它没有函数名。但是，这个匿名函数赋值给了变量abs，所以，通过
                                                    变量abs就可以调用该函数      
                        调用函数 -- 调用函数时，按顺序传入参数即可 -- 允许传入任意个参数而不影响调用
                        函数执行方式
                                加载执行--页面加载时执行函数代码
                                事件触发执行--某个事件发生时执行函数代码
                        高阶函数 -- 变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
                        常用函数
                                alert("alert函数被触发后会弹出提示信息！")
                                document.write("HTML代码") -- 注意使用该函数仅仅向文档输出写内容--绝不要使用在文档加载之后使用 document.write()。这会覆盖该文档
                                document.getElementById(value) -- 该函数可获得HTML文档中，id 属性值为 value 的对象 -- 故请使用 "id" 属性来标识 HTML 元素
                                document.getElementById("demo").innerHTML="替换内容"; --向 id="demo" 的 HTML 元素输出文本 "替换内容" -- 修改 HTML 内容最简单的方法
                                document.getElementById(id).attribute=new value -- 改变 HTML 元素的属性
                                                <img id="image" src="smiley.gif">
                                                <script>
                                                document.getElementById("image").src="landscape.jpg";
                                                </script>                           
                                document.getElementById(id).style.property=new style -- 改变 HTML 元素的样式
                                                    <p id="p2">Hello World!</p>
                                                    <script>
                                                    document.getElementById("p2").style.color="blue";
                                                    </script>                                
                                toUpperCase() -- 将文本转换为大写
                                toLowerCase() -- 将文本转换为小写
                                indexOf() -- 定位字符串中某一个指定的字符首次出现的位置
                                match() -- 查找字符串中特定的字符，并且如果找到的话，则返回这个字符，没有找到返回 null
                                replace() -- 方法在字符串中用某些字符替换另一些字符
                                            var str="Visit Microsoft!"
                                            document.write(str.replace(/Microsoft/,"W3School"))
                                            返回 Visit W3School!                                
                                setTimeout() -- 未来的某时执行代码 - 语法 --  setTimeout("javascript语句",毫秒)
                                map() --Array.map(f(x)) -- 把f(x)作用在Array的每一个元素并把结果生成一个新的Array
                                            function pow(x) {
                                                return x * x;
                                            }
                                            var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
                                            arr.map(pow); // [1, 4, 9, 16, 25, 36, 49, 64, 81]
                                            map()传入的参数是pow，即函数对象本身。                                
                                reduce() -- Array.reduce(f(x)) -- 把一个函数作用在这个Array的[x1, x2, x3...]上，这个函数必须接收两个参数，reduce()把结果继续和序列的下一个元素做累积计算
                                            其效果就是：
                                            [x1, x2, x3, x4].reduce(f) = f(f(f(x1, x2), x3), x4)
                                            比方说对一个Array求和，就可以用reduce实现：
                                            var arr = [1, 3, 5, 7, 9];
                                            arr.reduce(function (x, y) {
                                                return x + y;
                                            }); // 25                               
                                filter() -- Array.filter(f(x)) 用于把Array的某些元素过滤掉，返回剩下的元素 -- filter()把传入的函数依次作用于每个元素，然后根据返回值是true还是false决定保留还是丢弃该元素
                                            例如，在一个Array中，删掉偶数，只保留奇数，可以这么写：
                                            var arr = [1, 2, 4, 5, 6, 9, 10, 15];
                                            var r = arr.filter(function (x) {
                                                return x % 2 !== 0;
                                            });
                                            r; // [1, 5, 9, 15]
                                            把一个Array中的空字符串删掉，可以这么写：
                                            var arr = ['A', '', 'B', null, undefined, 'C', '  '];
                                            var r = arr.filter(function (s) {
                                                return s && s.trim(); // 注意：IE9以下的版本没有trim()方法
                                            });
                                            arr; // ['A', 'B', 'C']
                                            可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。                                
                                sort() -- Array.sort(f(x)) 排序的核心是比较两个元素的大小 -- Array的sort()方法默认把所有元素先转换为String再按照ASCII的大小比较 排序 -- sort()方法也是一个高阶函数，它还可以接收一个比较函数来实现自定义的排序
                                            比较的过程必须通过函数抽象出来。通常规定，对于两个元素x和y，如果认为x < y，则返回-1(返回较小者 y)，如果认为x == y，则返回0，
                                            如果认为x > y，则返回1(即返回较大者 x)，这样，排序算法就不用关心具体的比较过程，而是根据比较结果直接排序。
                                            cmp(x, y)返回-1表示x<y，返回1表示x>y，返回0表示x=y
                                                        至于为什么x<y是根据业务逻辑决定的，比如你可以认为'apple'<'Zoo'，也可以认为'apple'>'Zoo'
                                                        排序函数根据返回值判断x和y的大小                                            
                                            友情提示，sort()方法会直接对Array进行修改，它返回的结果仍是当前Array
                                            JavaScript的Array的sort()方法就是用于排序的，但是排序结果可能让你大吃一惊：
                                                        // 看上去正常的结果:
                                                        ['Google', 'Apple', 'Microsoft'].sort(); // ['Apple', 'Google', 'Microsoft'];
                                                        // apple排在了最后:
                                                        ['Google', 'apple', 'Microsoft'].sort(); // ['Google', 'Microsoft", 'apple']
                                                        // 无法理解的结果:
                                                        [10, 20, 1, 2].sort(); // [1, 10, 2, 20]
                                                        第二个排序把apple排在了最后，是因为字符串根据ASCII码进行排序，而小写字母a的ASCII码在大写字母之后。
                                                        第三个排序结果是什么鬼？简单的数字排序都能错？
                                                        这是因为Array的sort()方法默认把所有元素先转换为String再排序，结果'10'排在了'2'的前面，因为字符'1'比字符'2'的ASCII码小。                                                                                                
                                                        如果不知道sort()方法的默认排序规则，直接对数字排序，绝对栽进坑里！
                                                        幸运的是，sort()方法也是一个高阶函数，它还可以接收一个比较函数来实现自定义的排序。
                                                        要按数字大小排序，我们可以这么写：
                                                        var arr = [10, 20, 1, 2];
                                                        arr.sort(function (x, y) {
                                                            if (x < y) {
                                                                return -1;
                                                            }
                                                            if (x > y) {
                                                                return 1;
                                                            }
                                                            return 0;
                                                        }); // [1, 2, 10, 20]
                                                        如果要倒序排序，我们可以把大的数放前面：
                                                        var arr = [10, 20, 1, 2];
                                                        arr.sort(function (x, y) {
                                                            if (x < y) {
                                                                return 1;
                                                            }
                                                            if (x > y) {
                                                                return -1;
                                                            }
                                                            return 0;
                                                        }); // [20, 10, 2, 1]
                                                        var arr = [10, 20, 1, 2];
                                                        function sortNumber(n1, n2) {
                                                            return n1 - n2;
                                                        }
                                                        arr.sort(sortNumber); // [1, 2, 10, 20]
                                                        默认情况下，对字符串排序，是按照ASCII的大小比较的，现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，
                                                        不必对现有代码大加改动，只要我们能定义出忽略大小写的比较算法就可以：
                                                        var arr = ['Google', 'apple', 'Microsoft'];
                                                        arr.sort(function (s1, s2) {
                                                            x1 = s1.toUpperCase();
                                                            x2 = s2.toUpperCase();
                                                            if (x1 < x2) {
                                                                return -1;
                                                            }
                                                            if (x1 > x2) {
                                                                return 1;
                                                            }
                                                            return 0;
                                                        }); // ['apple', 'Google', 'Microsoft']
                                                        忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。
                                                        从上述例子可以看出，高阶函数的抽象能力是非常强大的，而且，核心代码可以保持得非常简洁。
                                                        最后友情提示，sort()方法会直接对Array进行修改，它返回的结果仍是当前Array：
                                                        var a1 = ['B', 'A', 'C'];
                                                        var a2 = a1.sort();
                                                        a1; // ['A', 'B', 'C']
                                                        a2; // ['A', 'B', 'C']
                                                        a1 === a2; // true, a1和a2是同一对象
                                            随机排序的方法：
                                                        Array.sort(function () {
                                                                return 0.5-Math.random()
                                                            })
                                                        这样就能把数组里的东西打乱排序啦！
                                Date()  -- 表示日期和时间
                                            获取系统当前时间
                                                        var now = new Date();
                                                        now; // Sat Mar 18 2017 18:38:13 GMT+0800 (China Standard Time)
                                                        now.getFullYear(); // 2015, 年份
                                                        now.getMonth(); // 5, 月份，注意月份范围是0~11，5表示六月
                                                        now.getDate(); // 24, 表示24号
                                                        now.getDay(); // 3, 表示星期三
                                                        now.getHours(); // 19, 24小时制
                                                        now.getMinutes(); // 49, 分钟
                                                        now.getSeconds(); // 22, 秒
                                                        now.getMilliseconds(); // 875, 毫秒数
                                                        now.getTime(); // 1435146562875, 以number形式表示的时间戳
                                                        注意，当前时间是浏览器从本机操作系统获取的时间，所以不一定准确，因为用户可以把当前时间设定为任何值。    
                                            创建一个指定日期和时间
                                                        var d = new Date(2015, 5, 19, 20, 15, 30, 123);
                                                        d; // Fri Jun 19 2015 20:15:30 GMT+0800 (CST)
                                                        你可能观察到了一个非常非常坑爹的地方，就是JavaScript的月份范围用整数表示是0~11，0表示一月，1表示二月……，所以
                                                        要表示6月，我们传入的是5！这绝对是JavaScript的设计者当时脑抽了一下，但是现在要修复已经不可能了。         
                                                        第二种创建一个指定日期和时间的方法是解析一个符合ISO 8601格式的字符串：
                                                        var d = Date.parse('2015-06-24T19:49:22.875+08:00');
                                                        d; // 1435146562875
                                                        但它返回的不是Date对象，而是一个时间戳。不过有时间戳就可以很容易地把它转换为一个Date：
                                                        var d = new Date(1435146562875);
                                                        d; // Wed Jun 24 2015 19:49:22 GMT+0800 (CST)                                                   
                                            时区
                                                        Date对象表示的时间总是按浏览器所在时区显示的，不过我们既可以显示本地时间，也可以显示调整后的UTC时间：
                                                        var d = new Date(1435146562875);
                                                        d.toLocaleString(); // '2015/6/24 下午7:49:22'，本地时间（北京时区+8:00），显示的字符串与操作系统设定的格式有关
                                                        d.toUTCString(); // 'Wed, 24 Jun 2015 11:49:22 GMT'，UTC时间，与本地时间相差8小时
                                                        那么在JavaScript中如何进行时区转换呢？实际上，只要我们传递的是一个number类型的时间戳，我们就不用关心时区转换。任何浏览器都可以把一个时间戳正确转换为本地时间。
                                                        时间戳是个什么东西？时间戳是一个自增的整数，它表示从1970年1月1日零时整的GMT时区开始的那一刻，到现在的毫秒数。假设浏览器所在电脑的时间是准确的，那么世界上无论哪个时区的电脑，它们此刻产生的时间戳数字都是一样的，所以，时间戳可以精确地表示一个时刻，并且与时区无关。
                                                        所以，我们只需要传递时间戳，或者把时间戳从数据库里读出来，再让JavaScript自动转换为当地时间就可以了。
                                                        要获取当前时间戳，可以用：
                                                        if (Date.now) {
                                                            alert(Date.now()); // 老版本IE没有now()方法
                                                        } else {
                                                            alert(new Date().getTime());
                                                        }
                                getTime() 返回从 1970 年 1 月 1 日至今的毫秒数
                                闭包() -- 把函数作为结果值返回-- 闭包就是携带状态的函数，并且它的状态可以完全对外隐藏起来 -- 参见 Python
                                            普通的函数就好像你去买冰激凌。卖家直接给你一个冰激凌，闭包就是直接给你一个冰箱，你想啥时候吃就啥时候吃，哈哈，跟OC里面的Block非常向                                                                                                                        
                                            注意到返回的函数在其定义内部引用了局部变量arr，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，
                                            闭包用起来简单，实现起来可不容易。
                                            另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：
                                            function count() {
                                                var arr = [];
                                                for (var i=1; i<=3; i++) {
                                                    arr.push(function () {
                                                        return i * i;
                                                    });
                                                }
                                                return arr;
                                            }
                                            var results = count();
                                            var f1 = results[0];
                                            var f2 = results[1];
                                            var f3 = results[2];
                                            在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都添加到一个Array中返回了。
                                            你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：
                                            f1(); // 16
                                            f2(); // 16
                                            f3(); // 16
                                            全部都是16！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i
                                            已经变成了4，因此最终结果为16。
                                            返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
                                            如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量
                                            后续如何更改，已绑定到函数参数的值不变：
                                            function count() {
                                                var arr = [];
                                                for (var i=1; i<=3; i++) {
                                                    arr.push((function (n) {
                                                        return function () {
                                                            return n * n;
                                                        }
                                                    })(i));
                                                }
                                                return arr;
                                            }
                                            var results = count();
                                            var f1 = results[0];
                                            var f2 = results[1];
                                            var f3 = results[2];
                                            f1(); // 1
                                            f2(); // 4
                                            f3(); // 9
                                            注意这里用了一个“创建一个匿名函数并立刻执行”的语法：
                                            (function (x) {
                                                return x * x;
                                            })(3); // 9
                                            理论上讲，创建一个匿名函数并立刻执行可以这么写：
                                            function (x) { return x * x } (3);
                                            但是由于JavaScript语法解析的问题，会报SyntaxError错误，因此需要用括号把整个函数定义括起来：
                                            (function (x) { return x * x }) (3);
                                            通常，一个立即执行的匿名函数可以把函数体拆开，一般这么写：
                                            (function (x) {
                                                return x * x;
                                            })(3);
                                            说了这么多，难道闭包就是为了返回一个函数然后延迟执行吗？
                                            当然不是！闭包有非常强大的功能。举个栗子：
                                            在面向对象的程序设计语言里，比如Java和C++，要在对象内部封装一个私有变量，可以用private修饰一个成员变量。
                                            在没有class机制，只有函数的语言里，借助闭包，同样可以封装一个私有变量。我们用JavaScript创建一个计数器：
                                            'use strict';
                                            function create_counter(initial) {
                                                var x = initial || 0;
                                                return {
                                                    inc: function () {
                                                        x += 1;
                                                        return x;
                                                    }
                                                }
                                            }
                                            它用起来像这样：
                                            var c1 = create_counter();
                                            c1.inc(); // 1
                                            c1.inc(); // 2
                                            c1.inc(); // 3
                                            var c2 = create_counter(10);
                                            c2.inc(); // 11
                                            c2.inc(); // 12
                                            c2.inc(); // 13
                                            在返回的对象中，实现了一个闭包，该闭包携带了局部变量x，并且，从外部代码根本无法访问到变量x。换句话说，闭包就是携带状态的函数，
                                            并且它的状态可以完全对外隐藏起来。
                                            闭包还可以把多参数的函数变成单参数的函数。例如，要计算xy可以用Math.pow(x, y)函数，不过考虑到经常计算x2或x3，我们可以利用
                                            闭包创建新的函数pow2和pow3：
                                            function make_pow(n) {
                                                return function (x) {
                                                    return Math.pow(x, n);
                                                }
                                            }
                                            // 创建两个新函数:
                                            var pow2 = make_pow(2);
                                            var pow3 = make_pow(3);
                                            pow2(5); // 25
                                            pow3(7); // 343                                
                                箭头函数(Arrow Function) -- 箭头函数相当于匿名函数，并且简化了函数定义 -- 用call()或者apply()调用箭头函数
                                        为什么叫Arrow Function？因为它的定义用的就是一个箭头：x => x * x
                                                    上面的箭头函数相当于：
                                                    function (x) {
                                                        return x * x;
                                                    }
                                        箭头函数有两种格式，一种像上面的 x => x * x，只包含一个表达式，连{ ... }和 return 都省略掉了。
                                        还有一种可以包含多条语句，这时候就不能省略{ ... }和return：
                                                    x => {
                                                        if (x > 0) {
                                                            return x * x;
                                                        }
                                                        else {
                                                            return - x * x;
                                                        }
                                                    }
                                        如果参数不是一个，就需要用括号()括起来：
                                                    // 两个参数:
                                                    (x, y) => x * x + y * y
                                                    // 无参数:
                                                    () => 3.14
                                                    // 可变参数:
                                                            (x, y, ...rest) => {
                                                                var i, sum = x + y;
                                                                for (i=0; i<rest.length; i++) {
                                                                    sum += rest[i];
                                                                }
                                                                return sum;
                                                            }     
                                        如果要返回一个对象，就要注意，如果是单表达式，这么写的话会报错：
                                                    // SyntaxError:
                                                    x => { foo: x }
                                                    因为和函数体的{ ... }有语法冲突，所以要改为：
                                                    // ok:
                                                    x => ({ foo: x })
                                        this
                                                    箭头函数看上去是匿名函数的一种简写，但实际上，箭头函数和匿名函数有个明显的区别：箭头函数内部的this是词法作用域，由上下文确定。
                                                    回顾前面的例子，由于JavaScript函数对this绑定的错误处理，下面的例子无法得到预期结果：
                                                                var obj = {
                                                                    birth: 1990,
                                                                    getAge: function () {
                                                                        var b = this.birth; // 1990
                                                                        var fn = function () {
                                                                            return new Date().getFullYear() - this.birth; // this指向window或undefined
                                                                        };
                                                                        return fn();
                                                                    }
                                                                };
                                                    现在，箭头函数完全修复了this的指向，this总是指向词法作用域，也就是外层调用者obj：
                                                                var obj = {
                                                                    birth: 1990,
                                                                    getAge: function () {
                                                                        var b = this.birth; // 1990
                                                                        var fn = () => new Date().getFullYear() - this.birth; // this指向obj对象
                                                                        return fn();
                                                                    }
                                                                };
                                                                obj.getAge(); // 25
                                                    如果使用箭头函数，以前的那种hack写法：
                                                                var that = this;
                                                                就不再需要了。
                                                    由于this在箭头函数中已经按照词法作用域绑定了，所以，用call()或者apply()调用箭头函数时，无法对this进行绑定，即传入的第一个参数被忽略：
                                                                var obj = {
                                                                    birth: 1990,
                                                                    getAge: function (year) {
                                                                            var b = this.birth; // 1990
                                                                            var fn = (y) => y - this.birth; // this.birth仍是1990
                                                                            return fn.call({birth:2000}, year);
                                                                        }
                                                                    };
                                                                    obj.getAge(2015); // 25
                                生成器(generator) -- 生成器最大的特色是保存了推算元素的算法
                                            定义
                                                        generator（生成器）是ES6标准引入的新的数据类型。一个generator看上去像一个函数，但可以返回多次。
                                                        ES6定义generator标准的哥们借鉴了Python的generator的概念和语法
                                                        我们先复习函数的概念。一个函数是一段完整的代码，调用一个函数就是传入参数，然后返回结果：
                                                                    function foo(x) {
                                                                        return x + x;
                                                                    }
                                                                    var r = foo(1); // 调用foo函数
                                                                    函数在执行过程中，如果没有遇到return语句（函数末尾如果没有return，就是隐含的return undefined;），控制权无法交回被调用的代码。
                                                        generator跟函数很像，定义如下：
                                                                    function* foo(x) {
                                                                        yield x + 1;
                                                                        yield x + 2;
                                                                        return x + 3;
                                                                    }
                                                        generator和函数不同的是，generator由function*定义（注意多出的*号），并且，除了return语句，还可以用yield返回多次。
                                                        大多数同学立刻就晕了，generator就是能够返回多次的“函数”？返回多次有啥用？
                                                        还是举个栗子吧
                                                                    我们以一个著名的斐波那契数列为例，它由0，1开头：
                                                                    0 1 1 2 3 5 8 13 21 34 ...
                                                                    要编写一个产生斐波那契数列的函数，可以这么写：
                                                                    function fib(max) {
                                                                        var
                                                                            t,
                                                                            a = 0,
                                                                            b = 1,
                                                                            arr = [0, 1];
                                                                        while (arr.length < max) {
                                                                            t = a + b;
                                                                            a = b;
                                                                            b = t;
                                                                            arr.push(t);
                                                                        }
                                                                        return arr;
                                                                    }
                                                                    // 测试:
                                                                    fib(5); // [0, 1, 1, 2, 3]
                                                                    fib(10); // [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
                                                        函数只能返回一次，所以必须返回一个Array。但是，如果换成generator，就可以一次返回一个数，不断返回多次。
                                                        用generator改写如下：
                                                                    function* fib(max) {
                                                                        var
                                                                            t,
                                                                            a = 0,
                                                                            b = 1,
                                                                            n = 1;
                                                                        while (n < max) {
                                                                            yield a;
                                                                            t = a + b;
                                                                            a = b;
                                                                            b = t;
                                                                            n ++;
                                                                        }
                                                                        return a;
                                                                    }
                                                                    直接调用试试：
                                                                    fib(5); // fib {[[GeneratorStatus]]: "suspended", [[GeneratorReceiver]]: Window}
                                            调用
                                                        直接调用一个generator和调用函数不一样，fib(5)仅仅是创建了一个generator对象，还没有去执行它。
                                                        调用generator对象有两个方法，一是不断地调用generator对象的next()方法：
                                                                    var f = fib(5);
                                                                    f.next(); // {value: 0, done: false}
                                                                    f.next(); // {value: 1, done: false}
                                                                    f.next(); // {value: 1, done: false}
                                                                    f.next(); // {value: 2, done: false}
                                                                    f.next(); // {value: 3, done: true}
                                                                    next()方法会执行generator的代码，然后，每次遇到yield x;就返回一个对象{value: x, done: true/false}，然后“暂停”。返回的value
                                                                    就是yield的返回值，done表示这个generator是否已经执行结束了。如果done为true，则value就是return的返回值。
                                                                    当执行到done为true时，这个generator对象就已经全部执行完毕，不要再继续调用next()了。
                                                        第二个方法是直接用for ... of循环迭代generator对象，这种方式不需要我们自己判断done：
                                                                    for (var x of fib(5)) {
                                                                        console.log(x); // 依次输出0, 1, 1, 2, 3
                                                                    }
                                            用途
                                                        generator和普通函数相比，有什么用？
                                                        因为generator可以在执行过程中多次返回，所以它看上去就像一个可以记住执行状态的函数，利用这一点，写一个generator就可以实现需要用面向
                                                        对象才能实现的功能。例如，用一个对象来保存状态，得这么写：
                                                                    var fib = {
                                                                        a: 0,
                                                                        b: 1,
                                                                        n: 0,
                                                                        max: 5,
                                                                        next: function () {
                                                                            var
                                                                                r = this.a,
                                                                                t = this.a + this.b;
                                                                            this.a = this.b;
                                                                            this.b = t;
                                                                            if (this.n < this.max) {
                                                                                this.n ++;
                                                                                return r;
                                                                            } else {
                                                                                return undefined;
                                                                            }
                                                                        }
                                                                    };
                                                        用对象的属性来保存状态，相当繁琐。
                                                        generator还有另一个巨大的好处，就是把异步回调代码变成“同步”代码。这个好处要等到后面学了AJAX以后才能体会到。
                                                                    没有generator之前的黑暗时代，用AJAX时需要这么写代码：
                                                                    ajax('http://url-1', data1, function (err, result) {
                                                                        if (err) {
                                                                            return handle(err);
                                                                        }
                                                                        ajax('http://url-2', data2, function (err, result) {
                                                                            if (err) {
                                                                                return handle(err);
                                                                            }
                                                                            ajax('http://url-3', data3, function (err, result) {
                                                                                if (err) {
                                                                                    return handle(err);
                                                                                }
                                                                                return success(result);
                                                                            });
                                                                        });
                                                                    });
                                                                    回调越多，代码越难看。
                                                                    有了generator的美好时代，用AJAX时可以这么写：
                                                                    try {
                                                                        r1 = yield ajax('http://url-1', data1);
                                                                        r2 = yield ajax('http://url-2', data2);
                                                                        r3 = yield ajax('http://url-3', data3);
                                                                        success(r3);
                                                                    }
                                                                    catch (err) {
                                                                        handle(err);
                                                                    }
                                                                    看上去是同步的代码，实际执行是异步的。                                                                                                        
                                                        哈哈,这位题主的性格我很喜欢,喜欢追根究底. 学习新知识的时候得闹清一切来龙去脉.对用途不明朗的知识有抵触心理.
                                                        首先,实现next_id不用generator也是没问题的.
                                                        生成器是真干货,不是原来的什么功能翻新的.
                                                        生成器最大的特色是保存了推算元素的算法,这个路子就野了. 假如我有一个正整数生成器,在内存有限的情况下,我就可以假装这个生成器里确实保存了
                                                        所有的正整数,不信的话我可以遍历看一看.
                                                        用数组怎么存得下所有的正整数,怎么替代生成器,这样的活又不像牛车拉货,一头牛拉不动多加几头牛就能解决的.
            RegExp 正则表达式() -- '一种用来匹配字符串的强有力的武器' -- 参见 Python 有区别
                        设计思想 -- 是用一种描述性的语言来给字符串定义一个规则，凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。     
                        匹配规则
                                    '\d' 可以匹配一个数字
                                    '\w' 可以匹配一个字母或数字
                                    '.' 可以匹配任意字符
                                    '*' 表示任意个字符（包括0个）
                                    '+' 表示至少一个字符
                                    '?' 表示0个或1个字符
                                    '{n}' 表示n个字符  --  '\d{3}' 表示匹配3个数字，例如'010'
                                    '{n,m}' 表示n-m个字符
                                    '\s' 可以匹配一个空格（也包括Tab等空白符）
                                    '\s+' 表示至少有一个空格，例如匹配' '，'\t\t'等
                                    '\ ' 转义特殊字符
                                    '[0-9a-zA-Z\_]' 可以匹配一个数字、字母或者下划线
                                    '[0-9a-zA-Z\_]+' 可以匹配至少由一个数字、字母或者下划线组成的字符串
                                    '[a-zA-Z\_\$][0-9a-zA-Z\_\$]*' 可以匹配由字母或下划线、$开头，后接任意个由一个数字、字母或者下划线、$组成的字符串，也就是JavaScript允许的变量名
                                    'A|B' 可以匹配A或B
                                    ^ 表示行的开头, '^\d' 表示必须以数字开头
                                    $表示行的结束，'\d$' 表示必须以数字结束
                        判断一个字符串是否是合法的Email的方法是
                                    1.  创建一个匹配Email的正则表达式
                                    2.  用该正则表达式去匹配用户的输入来判断是否合法 -- RegExp对象的test()方法
                                                var re = /^\d{3}\-\d{3,8}$/;
                                                re.test('010-12345'); // true
                                                re.test('010-1234x'); // false
                                                re.test('010 12345'); // false
                                                RegExp对象的test()方法用于测试给定的字符串是否符合条件。
                        JavaScript有两种方式创建一个正则表达式
                                    第一种方式是直接通过 /正则表达式/ 写出来 -- var re1 = /ABC\-001/;
                                    第二种方式是通过new RegExp('正则表达式')创建一个RegExp对象 -- var re2 = new RegExp('ABC\\-001');
                                    注意，如果使用第二种写法，因为字符串的转义问题，字符串的两个\\实际上是一个\
                        功能
                                    切分字符串
                                                用正则表达式切分字符串比用固定的字符更灵活，请看正常的切分代码：
                                                'a b   c'.split(' '); // ['a', 'b', '', '', 'c']
                                                嗯，无法识别连续的空格，用正则表达式试试：
                                                'a b   c'.split(/\s+/); // ['a', 'b', 'c']
                                                无论多少个空格都可以正常分割。加入,试试：
                                                'a,b, c  d'.split(/[\s\,]+/); // ['a', 'b', 'c', 'd']
                                                再加入;试试：
                                                'a,b;; c  d'.split(/[\s\,\;]+/); // ['a', 'b', 'c', 'd']
                                                如果用户输入了一组标签，下次记得用正则表达式来把不规范的输入转化成正确的数组。
                                    分组 -- 如果正则表达式中定义了组，可以在RegExp对象上用 exec()方法提取出子串来
                                                除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）。比如：
                                                ^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码：
                                                var re = /^(\d{3})-(\d{3,8})$/;
                                                re.exec('010-12345'); // ['010-12345', '010', '12345']
                                                re.exec('010 12345'); // null
                                                如果正则表达式中定义了组，就可以在RegExp对象上用exec()方法提取出子串来。
                                                exec()方法在匹配成功后，会返回一个Array，第一个元素是正则表达式匹配到的整个字符串，后面的字符串表示匹配成功的子串。
                                                exec()方法在匹配失败时返回null。
                                    贪婪匹配         
                                    全局搜索 
                                                JavaScript的正则表达式还有几个特殊的标志，最常用的是g，表示全局匹配：
                                                var r1 = /test/g;
                                                // 等价于:
                                                var r2 = new RegExp('test', 'g');
                                                全局匹配可以多次执行exec()方法来搜索一个匹配的字符串。当我们指定g标志后，每次运行exec()，正则表达式本身会更新lastIndex属性，表示上次匹配到的最后索引：
                                                var s = 'JavaScript, VBScript, JScript and ECMAScript';
                                                var re=/[a-zA-Z]+Script/g;
                                                // 使用全局匹配:
                                                re.exec(s); // ['JavaScript']
                                                re.lastIndex; // 10
                                                re.exec(s); // ['VBScript']
                                                re.lastIndex; // 20
                                                re.exec(s); // ['JScript']
                                                re.lastIndex; // 29
                                                re.exec(s); // ['ECMAScript']
                                                re.lastIndex; // 44
                                                re.exec(s); // null，直到结束仍没有匹配到
                                                全局匹配类似搜索，因此不能使用/^...$/，那样只会最多匹配一次。
                                                正则表达式还可以指定i标志，表示忽略大小写，m标志，表示执行多行匹配。
            JSON -- JavaScript Object Notation 的缩写，它是一种超轻量级的数据交换格式
                        JSON实际上是JavaScript的一个子集。在JSON中，一共就这么几种数据类型
                                    •   number：和JavaScript的number完全一致；
                                    •   boolean：就是JavaScript的true或false；
                                    •   string：就是JavaScript的string；
                                    •   null：就是JavaScript的null；
                                    •   array：就是JavaScript的Array表示方式——[]；
                                    •   object：就是JavaScript的{ ... }表示方式。
                                    以及上面的任意组合。
                        规则
                                    并且，JSON还定死了字符集必须是UTF-8，表示多语言 
                                    为了统一解析，JSON的字符串规定必须用双引号""，Object的键也必须用双引号""。
                                    几乎所有编程语言都有解析JSON的库，在JavaScript中可以直接使用JSON，因为JavaScript内置了JSON的解析。
                                    把任何JavaScript对象变成JSON，就是把这个对象序列化成一个JSON格式的字符串，这样才能够通过网络传递给其他计算机。
                                    如果我们收到一个JSON格式的字符串，只需要把它反序列化成一个JavaScript对象，就可以在JavaScript中直接使用这个对象了
                        序列化 -- JSON.stringify(对象, 处理函数/控制如何筛选对象的键值, 显示方式); -- 把对象序列化成JSON格式的字符串
                                    让我们先把小明这个对象序列化成JSON格式的字符串：
                                                var xiaoming = {
                                                    name: '小明',
                                                    age: 14,
                                                    gender: true,
                                                    height: 1.65,
                                                    grade: null,
                                                    'middle-school': '\"W3C\" Middle School',
                                                    skills: ['JavaScript', 'Java', 'Python', 'Lisp']
                                                };
                                                JSON.stringify(xiaoming); // '{"name":"小明","age":14,"gender":true,"height":1.65,"grade":null,"middle-school":"\"W3C\" Middle School","skills":["JavaScript","Java","Python","Lisp"]}'
                                    要输出得好看一些，可以加上参数，按缩进输出：
                                                JSON.stringify(xiaoming, null, '  ');
                                                结果：
                                                {
                                                  "name": "小明",
                                                  "age": 14,
                                                  "gender": true,
                                                  "height": 1.65,
                                                  "grade": null,
                                                  "middle-school": "\"W3C\" Middle School",
                                                  "skills": [
                                                    "JavaScript",
                                                    "Java",
                                                    "Python",
                                                    "Lisp"
                                                  ]
                                                }
                                    第二个参数用于控制如何筛选对象的键值，如果我们只想输出指定的属性，可以传入Array：
                                                JSON.stringify(xiaoming, ['name', 'skills'], '  ');
                                                结果：
                                                {
                                                  "name": "小明",
                                                  "skills": [
                                                    "JavaScript",
                                                    "Java",
                                                    "Python",
                                                    "Lisp"
                                                  ]
                                                }
                                    还可以传入一个函数，这样对象的每个键值对都会被函数先处理：
                                                function convert(key, value) {
                                                    if (typeof value === 'string') {
                                                        return value.toUpperCase();
                                                    }
                                                    return value;
                                                }
                                                JSON.stringify(xiaoming, convert, '  ');
                                                上面的代码把所有属性值都变成大写：
                                                {
                                                  "name": "小明",
                                                  "age": 14,
                                                  "gender": true,
                                                  "height": 1.65,
                                                  "grade": null,
                                                  "middle-school": "\"W3C\" MIDDLE SCHOOL",
                                                  "skills": [
                                                    "JAVASCRIPT",
                                                    "JAVA",
                                                    "PYTHON",
                                                    "LISP"
                                                  ]
                                                }
                                    如果我们还想要精确控制如何序列化小明，可以给xiaoming定义一个toJSON()的方法，直接返回JSON应该序列化的数据：
                                                var xiaoming = {
                                                    name: '小明',
                                                    age: 14,
                                                    gender: true,
                                                    height: 1.65,
                                                    grade: null,
                                                    'middle-school': '\"W3C\" Middle School',
                                                    skills: ['JavaScript', 'Java', 'Python', 'Lisp'],
                                                    toJSON: function () {
                                                        return { // 只输出name和age，并且改变了key：
                                                            'Name': this.name,
                                                            'Age': this.age
                                                        };
                                                    }
                                                };
                                                JSON.stringify(xiaoming); // '{"Name":"小明","Age":14}'
                        反序列化 -- JSON.parse(待反序列化的对象，处理函数)
                                    拿到一个JSON格式的字符串，我们直接用JSON.parse()把它变成一个JavaScript对象：
                                    JSON.parse('[1,2,3,true]'); // [1, 2, 3, true]
                                    JSON.parse('{"name":"小明","age":14}'); // Object {name: '小明', age: 14}
                                    JSON.parse('true'); // true
                                    JSON.parse('123.45'); // 123.45
                                    JSON.parse()还可以接收一个函数，用来转换解析出的属性：
                                    JSON.parse('{"name":"小明","age":14}', function (key, value) {
                                        // 把number * 2:
                                        if (key === 'name') {
                                            return value + '同学';
                                        }
                                        return value;
                                    }); // Object {name: '小明同学', age: 14}                                                                                                                                
            JavaScript 运算符()
                        JavaScript 算术运算符
                                    算术运算符用于执行变量与/或值之间的算术运算。
                                    给定 y=5，下面的表格解释了这些算术运算符：
                                    运算符 描述  例子  结果
                                    +   加   x=y+2   x=7
                                    -   减   x=y-2   x=3
                                    *   乘   x=y*2   x=10
                                    /   除   x=y/2   x=2.5
                                    %   求余数 (保留整数)  x=y%2   x=1
                                    ++  累加  x=++y   x=6
                                    --  递减  x=--y   x=4                            
                        JavaScript 赋值运算符
                                    赋值运算符用于给 JavaScript 变量赋值。
                                    给定 x=10 和 y=5，下面的表格解释了赋值运算符：
                                    运算符 例子  等价于 结果
                                    =   x=y     x=5
                                    +=  x+=y    x=x+y   x=15
                                    -=  x-=y    x=x-y   x=5
                                    *=  x*=y    x=x*y   x=50
                                    /=  x/=y    x=x/y   x=2
                                    %=  x%=y    x=x%y   x=0
                        用于字符串的 + 运算符 -- + 运算符用于把文本值或字符串变量加起来（连接起来）
                        对字符串和数字进行加法运算 -- 如果把数字与字符串相加，结果将成为字符串
                        JavaScript 比较和逻辑运算符 -- 比较和逻辑运算符用于测试 true 或 false
                                    比较运算符
                                                比较运算符在逻辑语句中使用，以测定变量或值是否相等。
                                                给定 x=5，下面的表格解释了比较运算符：
                                                运算符 描述  例子
                                                ==  等于  x==8 为 false --  它会自动转换数据类型再比较，很多时候，会得到非常诡异的结果
                                                === 全等（值和类型）    x===5 为 true；x==="5" 为 false  -- 不会自动转换数据类型，如果数据类型不一致，返回false，如果一致，再比较
                                                !=  不等于 x!=8 为 true
                                                >   大于  x>8 为 false
                                                <   小于  x<8 为 true
                                                >=  大于或等于   x>=8 为 false
                                                <=  小于或等于   x<=8 为 true                        
                                    如何使用
                                                可以在条件语句中使用比较运算符对值进行比较，然后根据结果来采取行动：
                                                if (age<18) document.write("Too young");
                                    逻辑运算符
                                                逻辑运算符用于测定变量或值之间的逻辑。
                                                给定 x=6 以及 y=3，下表解释了逻辑运算符：
                                                运算符 描述  例子
                                                &&  and (x < 10 && y > 1) 为 true
                                                        alert('a' && 'b'),请解释下括号内的返回值为何是'b'
                                                        &&符号的运算逻辑是，如果&&前边的结果为true（所有非空字符串轮换成布尔值时都为true）时，
                                                        则跳到&&后边执行计算，并返回&&后边的值，所以这里的返回值是'b'。
                                                ||  or  (x==5 || y==5) 为 false
                                                !   not !(x==y) 为 true
                                    条件运算符
                                                JavaScript 还包含了基于某些条件对变量进行赋值的条件运算符。
                                                语法
                                                variablename=(condition)?value1:value2 
                                                例子
                                                greeting=(visitor=="PRES")?"Dear President ":"Dear ";
                                                如果变量 visitor 中的值是 "PRES"，则向变量 greeting 赋值 "Dear President "，否则赋值 "Dear"。
            JavaScript 条件语句() -- 基于不同的条件来执行不同的动作
                        if 语句 -- 只有当指定条件为 true 时，使用该语句来执行代码
                                    语法
                                                if (条件)
                                                  {
                                                  只有当条件为 true 时执行的代码
                                                  }
                                                注意：请使用小写的 if。使用大写字母（IF）会生成 JavaScript 错误！语法
                                                if (条件)
                                                  {
                                                  只有当条件为 true 时执行的代码
                                                  }
                                                注意：请使用小写的 if。使用大写字母（IF）会生成 JavaScript 错误！                        
                        if...else 语句 -- 当条件为 true 时执行代码，当条件为 false 时执行其他代码
                                    语法
                                                if (条件)
                                                  {
                                                  当条件为 true 时执行的代码
                                                  }
                                                else
                                                  {
                                                  当条件不为 true 时执行的代码
                                                  }                        
                        if...else if....else 语句 -- 使用该语句来选择多个代码块之一来执行
                                    语法
                                                if (条件 1)
                                                  {
                                                  当条件 1 为 true 时执行的代码
                                                  }
                                                else if (条件 2)
                                                  {
                                                  当条件 2 为 true 时执行的代码
                                                  }
                                                else
                                                  {
                                                  当条件 1 和 条件 2 都不为 true 时执行的代码
                                                  }                        
                        switch 语句 -- 使用该语句来选择多个代码块之一来执行
                                    语法
                                                switch(n)
                                                {
                                                case 1:
                                                  执行代码块 1
                                                  break;
                                                case 2:
                                                  执行代码块 2
                                                  break;
                                                default:
                                                  n 与 case 1 和 case 2 不同时执行的代码
                                                }
                                    工作原理：
                                                首先设置表达式 n（通常是一个变量）。随后表达式的值会与结构中的每个 case 的值做比较。如果存在匹配，则与该 case 关联的
                                                代码块会被执行。请使用 break 来阻止代码自动地向下一个 case 运行。
                                                请使用 default 关键词来规定匹配不存在时做的事情
                                    实例
                                                显示今日的周名称。请注意 Sunday=0, Monday=1, Tuesday=2, 等等：
                                                var day=new Date().getDay();
                                                switch (day)
                                                {
                                                case 0:
                                                  x="Today it's Sunday";
                                                  break;
                                                case 1:
                                                  x="Today it's Monday";
                                                  break;
                                                case 2:
                                                  x="Today it's Tuesday";
                                                  break;
                                                case 3:
                                                  x="Today it's Wednesday";
                                                  break;
                                                case 4:
                                                  x="Today it's Thursday";
                                                  break;
                                                case 5:
                                                  x="Today it's Friday";
                                                  break;
                                                case 6:
                                                  x="Today it's Saturday";
                                                  break;
                                                }
                                                x 的结果：
                                                Today it''s Monday                        
            JavaScript 循环语句() -- 循环可以将代码块执行指定的次数    
                        for - 循环代码块一定的次数
                                    语法：
                                                for (语句 1; 语句 2; 语句 3)
                                                  {
                                                  被执行的代码块
                                                  }           
                                                语句 1 在循环（代码块）开始前执行
                                                            通常我们会使用语句 1 初始化循环中所用的变量 (var i=0)
                                                            语句 1 是可选的
                                                            可以在语句 1 中初始化任意（或者多个）值
                                                语句 2 定义运行循环（代码块）的条件
                                                            用于评估初始变量的条件
                                                            可选
                                                            语句 2 返回 true，则循环再次开始，如果返回 false，则循环将结束
                                                            如果省略了语句 2，那么必须在循环内提供 break。否则循环就无法停下来。这样有可能令浏览器崩溃
                                                语句 3 在循环（代码块）已被执行之后执行
                                                            通常语句 3 会增加初始变量的值。
                                                            语句 3 也是可选的。
                                                            语句 3 有多种用法。增量可以是负数 (i--)，或者更大 (i=i+15)。
                                                            语句 3 也可以省略（比如当循环内部有相应的代码时）                                                
                        for/in - 循环遍历对象的属性
                                    实例
                                    var person={fname:"John",lname:"Doe",age:25};
                                    for (x in person)
                                      {
                                      txt=txt + person[x];
                                      }                        
                        while - 当指定的条件为 true 时循环指定的代码块
                                    语法
                                    while (条件)
                                      {
                                      需要执行的代码
                                      }                        
                        do/while - 同样当指定的条件为 true 时循环指定的代码块 -- 该循环会执行一次代码块，在检查条件是否为真之前，然后如果条件为真的话，就会重复这个循环
                                    语法
                                    do
                                      {
                                      需要执行的代码
                                      }
                                    while (条件);      
            JavaScript with 语句() -- 用于设置代码在特定对象中的作用域 -- 为逐级的对象访问提供命名空间式的速写方式 -- 即在指定的代码区域，直接通过节点名称调用对象
                        例子，不建议使用 with 语句
                                    <html>
                                    <head>
                                    <script type="text/javascript">
                                    function validate_required(field,alerttxt)
                                    {
                                    with (field)
                                      {
                                      if (value==null||value=="")
                                        {alert(alerttxt);return false}
                                      else {return true}
                                      }
                                    }
                                    function validate_form(thisform)
                                    {
                                    with (thisform)
                                      {
                                      if (validate_required(email,"Email must be filled out!")==false)
                                        {email.focus();return false}
                                      }
                                    }
                                    </script>
                                    </head>
                                    <body>
                                    <form action="submitpage.htm" onsubmit="return validate_form(this)" method="post">
                                    Email: <input type="text" name="email" size="30">
                                    <input type="submit" value="Submit"> 
                                    </form>
                                    </body>
                                    </html>
            JavaScript Break 和 Continue 语句() -- break 语句用于跳出循环 -- continue 用于跳过循环中的一个迭代 
                        break 语句可用于跳出循环。break 语句跳出循环后，会继续执行该循环外部的代码（如果有的话）              
                        continue 语句中断循环中的迭代，如果出现了指定的条件，然后继续循环中的下一个迭代
                        JavaScript 标签 break 和 continue 语句仅仅是能够跳出代码块的语句
                                    如需标记 JavaScript 语句，请在语句之前加上冒号
                                                label:
                                                语句                                              
                                    语法
                                                break labelname;
                                                continue labelname;
                                                continue 语句（带有或不带标签引用）只能用在循环中。
                                                break 语句（不带标签引用），只能用在循环或 switch 中。
                                                通过标签引用，break 语句可用于跳出任何 JavaScript 代码块：
                                    实例
                                                cars=["BMW","Volvo","Saab","Ford"];
                                                list:
                                                {
                                                document.write(cars[0] + "<br>");
                                                document.write(cars[1] + "<br>");
                                                document.write(cars[2] + "<br>");
                                                break list;
                                                document.write(cars[3] + "<br>");
                                                document.write(cars[4] + "<br>");
                                                document.write(cars[5] + "<br>");
                                                }
            JavaScript 错误() -- Throw、Try 和 Catch
                        try 语句测试代码块的错误 -- try 语句允许我们定义在执行时进行错误测试的代码块
                        catch 语句处理错误 -- catch 语句允许我们定义当 try 代码块发生错误时，所执行的代码块， try 和 catch 是成对出现的
                                    语法
                                    try
                                              {
                                              //在这里运行代码
                                              }
                                    catch(err)
                                              {
                                              //在这里处理错误
                                              }                        
                        throw 语句创建自定义错误 -- 术语：创建或抛出异常（exception） -- 如果把 throw 与 try 和 catch 一起使用，就能够控制程序流，并生成自定义的错误消息 
                                    语法 throw exception 
                                    实例
                                                本例检测输入变量的值。如果值是错误的，会抛出一个异常（错误）。catch 会捕捉到这个错误，并显示一段自定义的错误消息：
                                                <script>
                                                function myFunction()
                                                {
                                                try
                                                  {
                                                  var x=document.getElementById("demo").value;
                                                  if(x=="")    throw "empty";
                                                  if(isNaN(x)) throw "not a number";
                                                  if(x>10)     throw "too high";
                                                  if(x<5)      throw "too low";
                                                  }
                                                catch(err)
                                                  {
                                                  var y=document.getElementById("mess");
                                                  y.innerHTML="Error: " + err + ".";
                                                  }
                                                }
                                                </script>
                                                <h1>My First JavaScript</h1>
                                                <p>Please input a number between 5 and 10:</p>
                                                <input id="demo" type="text">
                                                <button type="button" onclick="myFunction()">Test Input</button>
                                                <p id="mess"></p>                                    
            JavaScript 表单验证() -- 可用来在数据被送往服务器前对 HTML 表单中的这些输入数据进行验证
                        JavaScript 验证的这些典型的表单数据有：
                                    用户是否已填写表单中的必填项目？
                                    用户输入的邮件地址是否合法？
                                    用户是否已输入合法的日期？
                                    用户是否在数据域 (numeric field) 中输入了文本？  
                        HTML表单的输入控件主要有以下几种：
                                •   文本框，对应的<input type="text">，用于输入文本；
                                •   口令框，对应的<input type="password">，用于输入口令；
                                •   单选框，对应的<input type="radio">，用于选择一项；
                                •   复选框，对应的<input type="checkbox">，用于选择多项；
                                •   下拉框，对应的<select>，用于选择一项；
                                •   隐藏文本，对应的<input type="hidden">，用户不可见，但表单提交时会把隐藏文本发送到服务器
                        获取值
                                如果我们获得了一个<input>节点的引用，就可以直接调用value获得对应的用户输入值：
                                        // <input type="text" id="email">
                                        var input = document.getElementById('email');
                                        input.value; // '用户输入的值'
                                这种方式可以应用于text、password、hidden以及select。但是，对于单选框和复选框，value属性返回的永远是HTML预设的值，
                                而我们需要获得的实际是用户是否“勾上了”选项，所以应该用checked判断：
                                        // <label><input type="radio" name="weekday" id="monday" value="1"> Monday</label>
                                        // <label><input type="radio" name="weekday" id="tuesday" value="2"> Tuesday</label>
                                        var mon = document.getElementById('monday');
                                        var tue = document.getElementById('tuesday');
                                        mon.value; // '1'
                                        tue.value; // '2'
                                        mon.checked; // true或者false
                                        tue.checked; // true或者false
                        设置值
                                设置值和获取值类似，对于text、password、hidden以及select，直接设置value就可以：
                                        // <input type="text" id="email">
                                        var input = document.getElementById('email');
                                        input.value = 'test@example.com'; // 文本框的内容已更新
                                对于单选框和复选框，设置checked为true或false即可。
                        HTML5控件
                                HTML5新增了大量标准控件，常用的包括date、datetime、datetime-local、color等，它们都使用<input>标签：
                                        <input type="date" value="2015-07-01">
                                        <input type="datetime-local" value="2015-07-01T02:03:04">
                                        <input type="color" value="#ff0000">
                                不支持HTML5的浏览器无法识别新的控件，会把它们当做type="text"来显示。支持HTML5的浏览器将获得格式化的字符串。
                                例如，type="date"类型的input的value将保证是一个有效的YYYY-MM-DD格式的日期，或者空字符串。
                        提交表单 -- JavaScript可以以两种方式来处理表单的提交（AJAX方式在后面章节介绍）

                                方式一是通过<form>元素的 submit() 方法提交一个表单
                                        例如，响应一个<button>的click事件，在JavaScript代码中提交表单：
                                                <!-- HTML -->
                                                <form id="test-form">
                                                    <input type="text" name="test">
                                                    <button type="button" onclick="doSubmitForm()">Submit</button>
                                                </form>

                                                <script>
                                                function doSubmitForm() {
                                                    var form = document.getElementById('test-form');
                                                    // 可以在此修改form的input...
                                                    // 提交form:
                                                    form.submit();
                                                }
                                                </script>
                                        这种方式的缺点是扰乱了浏览器对form的正常提交。浏览器默认点击<button type="submit">时提交表单，或者用户在最后一个输入框按回车键
                                第二种方式是响应<form>本身的onsubmit事件，在提交form时作修改：
                                        <!-- HTML -->
                                        <form id="test-form" onsubmit="return checkForm()">
                                            <input type="text" name="test">
                                            <button type="submit">Submit</button>
                                        </form>

                                        <script>
                                        function checkForm() {
                                            var form = document.getElementById('test-form');
                                            // 可以在此修改form的input...
                                            // 继续下一步:
                                            return true;
                                        }
                                        </script>
                                        注意要return true来告诉浏览器继续提交，如果return false，浏览器将不会继续提交form，这种情况通常对应用户输入有误，提示用户错误信息后终止提交form。
                                        在检查和修改<input>时，要充分利用<input type="hidden">来传递数据。
                                        例如，很多登录表单希望用户输入用户名和口令，但是，安全考虑，提交表单时不传输明文口令，而是口令的MD5。普通JavaScript开发人员会直接修改<input>：
                                                <!-- HTML -->
                                                <form id="login-form" method="post" onsubmit="return checkForm()">
                                                    <input type="text" id="username" name="username">
                                                    <input type="password" id="password" name="password">
                                                    <button type="submit">Submit</button>
                                                </form>

                                                <script>
                                                function checkForm() {
                                                    var pwd = document.getElementById('password');
                                                    // 把用户输入的明文变为MD5:
                                                    pwd.value = toMD5(pwd.value);
                                                    // 继续下一步:
                                                    return true;
                                                }
                                                </script>
                                        这个做法看上去没啥问题，但用户输入了口令提交时，口令框的显示会突然从几个*变成32个*（因为MD5有32个字符）。
                                        要想不改变用户的输入，可以利用<input type="hidden">实现：
                                                <!-- HTML -->
                                                <form id="login-form" method="post" onsubmit="return checkForm()">
                                                    <input type="text" id="username" name="username">
                                                    <input type="password" id="input-password">
                                                    <input type="hidden" id="md5-password" name="password">
                                                    <button type="submit">Submit</button>
                                                </form>

                                                <script>
                                                function checkForm() {
                                                    var input_pwd = document.getElementById('input-password');
                                                    var md5_pwd = document.getElementById('md5-password');
                                                    // 把用户输入的明文变为MD5:
                                                    md5_pwd.value = toMD5(input_pwd.value);
                                                    // 继续下一步:
                                                    return true;
                                                }
                                                </script>
                                        注意到 id 为md5-password的<input>标记了name="password"，而用户输入的 id 为input-password的<input>没有name属性。没有name属性的<input>的数据不会被提交。
            JavaScript 操作文件()
                        在HTML表单中，可以上传文件的唯一控件就是<input type="file">。
                                注意：当一个表单包含<input type="file">时，表单的enctype必须指定为multipart/form-data，method必须指定为post，浏览器才能正确编码
                                并以multipart/form-data格式发送表单的数据。
                                出于安全考虑，浏览器只允许用户点击<input type="file">来选择本地文件，用JavaScript对<input type="file">的value赋值是没有任何效果的。
                                当用户选择了上传某个文件后，JavaScript也无法获得该文件的真实路径
                                通常，上传的文件都由后台服务器处理，JavaScript可以在提交表单时对文件扩展名做检查，以便防止用户上传无效格式的文件：
                                        var f = document.getElementById('test-file-upload');
                                        var filename = f.value; // 'C:\fakepath\test.png'
                                        if (!filename || !(filename.endsWith('.jpg') || filename.endsWith('.png') || filename.endsWith('.gif'))) {
                                            alert('Can only upload image file.');
                                            return false;
                                        }
                        File API
                                由于JavaScript对用户上传的文件操作非常有限，尤其是无法读取文件内容，使得很多需要操作文件的网页不得不用Flash这样的第三方插件来实现。
                                随着HTML5的普及，新增的File API允许JavaScript读取文件内容，获得更多的文件信息。
                                HTML5的File API提供了File和FileReader两个主要对象，可以获得文件信息并读取文件。
                                下面的例子演示了如何读取用户选取的图片文件，并在一个<div>中预览图像：
                                图片预览：
                                        var
                                            fileInput = document.getElementById('test-image-file'),
                                            info = document.getElementById('test-file-info'),
                                            preview = document.getElementById('test-image-preview');
                                        // 监听change事件:
                                        fileInput.addEventListener('change', function () {
                                            // 清除背景图片:
                                            preview.style.backgroundImage = '';
                                            // 检查文件是否选择:
                                            if (!fileInput.value) {
                                                info.innerHTML = '没有选择文件';
                                                return;
                                            }
                                            // 获取File引用:
                                            var file = fileInput.files[0];
                                            // 获取File信息:
                                            info.innerHTML = '文件: ' + file.name + '<br>' +
                                                             '大小: ' + file.size + '<br>' +
                                                             '修改: ' + file.lastModifiedDate;
                                            if (file.type !== 'image/jpeg' && file.type !== 'image/png' && file.type !== 'image/gif') {
                                                alert('不是有效的图片文件!');
                                                return;
                                            }
                                            // 读取文件:
                                            var reader = new FileReader();
                                            reader.onload = function(e) {
                                                var
                                                    data = e.target.result; // 'data:image/jpeg;base64,/9j/4AAQSk...(base64编码)...'            
                                                preview.style.backgroundImage = 'url(' + data + ')';
                                            };
                                            // 以DataURL的形式读取文件:
                                            reader.readAsDataURL(file);
                                        });
                                上面的代码演示了如何通过HTML5的File API读取文件内容。以DataURL的形式读取到的文件是一个字符串，类似于data:image/jpeg;base64,
                                /9j/4AAQSk...(base64编码)...，常用于设置图像。如果需要服务器端处理，把字符串base64,后面的字符发送给服务器并用Base64解码就可以得到
                                原始文件的二进制内容。
                        回调
                                上面的代码还演示了JavaScript的一个重要的特性就是单线程执行模式。在JavaScript中，浏览器的JavaScript执行引擎在执行JavaScript代码时，总是
                                以单线程模式执行，也就是说，任何时候，JavaScript代码都不可能同时有多于1个线程在执行。
                                你可能会问，单线程模式执行的JavaScript，如何处理多任务？
                                在JavaScript中，执行多任务实际上都是异步调用，比如上面的代码：
                                reader.readAsDataURL(file);
                                就会发起一个异步操作来读取文件内容。因为是异步操作，所以我们在JavaScript代码中就不知道什么时候操作结束，因此需要先设置一个回调函数：
                                reader.onload = function(e) {
                                    // 当文件读取完成后，自动调用此函数:
                                };
                                当文件读取完成后，JavaScript引擎将自动调用我们设置的回调函数。执行回调函数时，文件已经读取完毕，所以我们可以在回调函数内部安全地获得文件内容
                        实例1
                                HTML：前
                                        <h3>图片预览</h3>
                                        <div id="image-preview" style="border: 1px solid #ccc; width: 980px;margin:auto; height: 200px; background-size: contain; background-repeat: no-repeat; background-position: center center;">

                                        </div>
                                        <div id="info">

                                        </div>
                                        <div>
                                            <input type="file" id="file" name="file" value="" />
                                        </div>
                                JS：后
                                        <script>
                                            'use strict';
                                            var fileInput = document.getElementById('file'),
                                                info = document.getElementById('info'),
                                                preview = document.getElementById('image-preview');
                                            // 监听 type="file" 的change事件
                                            fileInput.addEventListener('change', function () {
                                                // 清除背景图片
                                                preview.style.backgroundImage = '';
                                                // 检查文件是否选择
                                                if(!fileInput.value) {
                                                    info.innerHTML = '<span style="color:red;">没有选择图片</span>';
                                                    return false;
                                                }

                                                // 获取file引用
                                                var file = fileInput.files[0];
                                                console.log(file);
                                                info.innerHTML = 
                                                                '文件: ' + file.name + '<br>'
                                                            +   '大小: ' + file.size + '<br>'
                                                            +   '修改: ' + file.lastModifiedDate;

                                                // 判断图片格式
                                                if(file.type!=='image/jpeg' && file.type !== 'image/png' && file.type !== 'image/gif') {
                                                    var p = document.createElement('p');
                                                    p.innerHTML = '<span style="color:red;">不是有效的图片文件！</span>';
                                                    info.appendChild(p);
                                                    return false;
                                                }

                                                // 展示图片
                                                var reader = new FileReader();
                                                reader.onload = function (e) {
                                                    var data = e.target.result;// data:image/jpeg;base64,
                                                    preview.style.backgroundImage = 'url("'+data+'")';
                                                }

                                                // 以DataURL的形式读取文件
                                                reader.readAsDataURL(file);
                                            });

                                        </script>
                        实例2
                                <!DOCTYPE html>
                                <html>
                                    <head>
                                        <meta charset="utf-8" />
                                        <meta name="viewport" content="width=device-width" />
                                        <title>文件api</title>
                                        <style>
                                #test-image-preview {
                                    width:500px;
                                    height:500px;
                                    border:1px solid #ff0000;
                                }

                                        </style>
                                        <script src="fileapi.js"></script>
                                    </head>
                                    <body>
                                        <div id="test-file-info"></div>
                                        <div id="test-image-preview"></div>
                                        <form action=""><input id="test-image-file" type="file"></form>
                                    </body>
                                </html>
                                fileapi.js
                                'use strict'

                                window.onload=function(){
                                    var fileInput = document.getElementById('test-image-file');
                                    var info = document.getElementById('test-file-info');
                                    var preview = document.getElementById('test-image-preview');


                                    fileInput.addEventListener('change',function(){
                                        console.log('change...');
                                        preview.style.backgroundImage='';
                                        if (!fileInput.value){
                                            info.innerHTML = '没有选择文件';
                                            return ;
                                        }
                                        var file = fileInput.files[0];
                                        info.innerHTML = '文件:' + file.name + '<br>'+'大小:'+file.size+'<br>'+'修改:'+file.lastModifiedDate;
                                        if(file.type !== 'image/jpeg' && file.type !== 'image/png' && file.type !== 'image/gif'){
                                            alert('不是有效的图片文件!');
                                            return;
                                        }

                                        var reader = new FileReader();
                                        reader.onload=function(e){
                                            console.log('reader.onload');
                                            var data = e.target.result;
                                            preview.style.backgroundImage='url('+ data +')';
                                        };
                                        reader.readAsDataURL(file);
                                    });
                                };

            JS HTML DOM -- 通过 HTML DOM(文档对象模型, Document Object Model) -- 对象树，可访问 JavaScript HTML 文档的所有元素 -- 改变 CSS
                        通过可编程的对象模型，创建动态的 HTML--改变、添加、遍历或删除页面中的所有 HTML 元素或属性
                        
                        改变 HTML 的元素
                                    改变 HTML 输出流--document.write() 可用于直接向 HTML 输出流写内容--不要在文档加载后使用 document.write()。这会覆盖该文档
                                    改变 HTML 内容--innerHTML 属性--document.getElementById(id).innerHTML=new HTML
                                                一种是修改innerHTML属性，这个方式非常强大，不但可以修改一个DOM节点的文本内容，还可以直接通过HTML片段修改DOM节点内部的子树
                                                            // 获取<p id="p-id">...</p>
                                                            var p = document.getElementById('p-id');
                                                            // 设置文本为abc:
                                                            p.innerHTML = 'ABC'; // <p id="p-id">ABC</p>
                                                            // 设置HTML:
                                                            p.innerHTML = 'ABC <span style="color:red">RED</span> XYZ';
                                                            // <p>...</p>的内部结构已修改
                                                            用innerHTML时要注意，是否需要写入HTML。如果写入的字符串是通过网络拿到了，要注意对字符编码来避免XSS攻击
                                                第二种是修改innerText或textContent属性，这样可以自动对字符串进行HTML编码，保证无法设置任何HTML标签
                                                            // 获取<p id="p-id">...</p>
                                                            var p = document.getElementById('p-id');
                                                            // 设置文本:
                                                            p.innerText = '<script>alert("Hi")</script>';
                                                            // HTML被自动编码，无法设置一个<script>节点:
                                                            // <p id="p-id">&lt;script&gt;alert("Hi")&lt;/script&gt;</p>
                                                两者的区别在于读取属性时，innerText不返回隐藏元素的文本，而textContent返回所有文本。另外注意IE<9不支持textContent                                                                        
                                    改变 HTML 属性--attribute 属性--document.getElementById(id).attribute=new value
                                    添加和删除节点（HTML 元素）
                                                创建新的 HTML 元素 -- 如需向 HTML DOM 添加新元素，必须首先创建该元素（元素节点），然后向一个已存在的元素追加该元素
                                                            当我们获得了某个DOM节点，想在这个DOM节点内插入新的DOM，应该如何做？
                                                                        如果DOM节点是空的，例<div></div>，直接使用innerHTML = '<span>child</span>'就可以修改节点的内容，相当于“插入”了新的DOM节点
                                                                        如果这个DOM节点不是空的，那就不能这么做，因为innerHTML会直接替换掉原来的所有子节点，有两个办法可以插入新的节点
                                                                                    一个是使用appendChild -- 把一个子节点添加到父节点的最后一个子节点
                                                                                                <!-- HTML结构 -->
                                                                                                        <p id="js">JavaScript</p>
                                                                                                        <div id="list">
                                                                                                            <p id="java">Java</p>
                                                                                                            <p id="python">Python</p>
                                                                                                            <p id="scheme">Scheme</p>
                                                                                                        </div>
                                                                                                把<p id="js">JavaScript</p>添加到<div id="list">的最后一项：
                                                                                                        <script>
                                                                                                        var
                                                                                                            js = document.getElementById('js'),
                                                                                                            list = document.getElementById('list');
                                                                                                        list.appendChild(js);
                                                                                                        </script>
                                                                                                现在，HTML结构变成了这样：
                                                                                                        <!-- HTML结构 -->
                                                                                                        <div id="list">
                                                                                                            <p id="java">Java</p>
                                                                                                            <p id="python">Python</p>
                                                                                                            <p id="scheme">Scheme</p>
                                                                                                            <p id="js">JavaScript</p>
                                                                                                        </div>
                                                                                                因为我们插入的js节点已经存在于当前的文档树，因此这个节点首先会从原先的位置删除，再插入到新的位置。
                                                                                                更多的时候我们会从零创建一个新的节点，然后插入到指定位置：
                                                                                                        <sctipt>
                                                                                                        var
                                                                                                            list = document.getElementById('list'),
                                                                                                            haskell = document.createElement('p');
                                                                                                        haskell.id = 'haskell';
                                                                                                        haskell.innerText = 'Haskell';
                                                                                                        list.appendChild(haskell);
                                                                                                        </script>
                                                                                                这样我们就动态添加了一个新的节点：
                                                                                                        <!-- HTML结构 -->
                                                                                                        <div id="list">
                                                                                                            <p id="java">Java</p>
                                                                                                            <p id="python">Python</p>
                                                                                                            <p id="scheme">Scheme</p>
                                                                                                            <p id="haskell">Haskell</p>
                                                                                                        </div>
                                                                                                动态创建一个节点然后添加到DOM树中，可以实现很多功能。举个例子
                                                                                                下面的代码动态创建了一个<style>节点，然后把它添加到<head>节点的末尾，这样就动态地给文档添加了新的CSS定义：
                                                                                                        var d = document.createElement('style');
                                                                                                        d.setAttribute('type', 'text/css');
                                                                                                        d.innerHTML = 'p { color: red }';
                                                                                                        document.getElementsByTagName('head')[0].appendChild(d);
                                                                                                        可以在Chrome的控制台执行上述代码，观察页面样式的变化。                                                                               
                                                                                    把子节点插入到指定的位置 --使用parentElement.insertBefore(newElement, referenceElement);，子节点会插入到referenceElement之前
                                                                                            还是以上面的HTML为例，假定我们要把Haskell插入到Python之前：
                                                                                            <!-- HTML结构 -->
                                                                                                    <div id="list">
                                                                                                        <p id="java">Java</p>
                                                                                                        <p id="python">Python</p>
                                                                                                        <p id="scheme">Scheme</p>
                                                                                                    </div>
                                                                                            可以这么写：
                                                                                                    <script>
                                                                                                    var
                                                                                                        list = document.getElementById('list'),
                                                                                                        ref = document.getElementById('python'),
                                                                                                        haskell = document.createElement('p');
                                                                                                    haskell.id = 'haskell';
                                                                                                    haskell.innerText = 'Haskell';
                                                                                                    list.insertBefore(haskell, ref);
                                                                                                    </script>
                                                                                            新的HTML结构如下：
                                                                                                    <!-- HTML结构 -->
                                                                                                    <div id="list">
                                                                                                        <p id="java">Java</p>
                                                                                                        <p id="haskell">Haskell</p>
                                                                                                        <p id="python">Python</p>
                                                                                                        <p id="scheme">Scheme</p>
                                                                                                    </div>
                                                                                            可见，使用insertBefore重点是要拿到一个“参考子节点”的引用  
                                                                                            很多时候，需要循环一个父节点的所有子节点，可以通过迭代children属性实现：
                                                                                                    var
                                                                                                        i, c,
                                                                                                        list = document.getElementById('list');
                                                                                                    for (i = 0; i < list.children.length; i++) {
                                                                                                        c = list.children[i]; // 拿到第i个子节点
                                                                                                    }
                                                删除已有的 HTML 元素 -- 如需删除 HTML 元素，必须首先获得该元素及它的父元素，调用父节点的removeChild把自己删掉
                                                            实例
                                                                        <div id="div1">
                                                                        <p id="p1">这是一个段落。</p>
                                                                        <p id="p2">这是另一个段落。</p>
                                                                        </div>
                                                                        <script>
                                                                        var parent=document.getElementById("div1");
                                                                        var child=document.getElementById("p1"); 
                                                                        parent.removeChild(child);
                                                                        </script>

                                                                        or 
                                                                        <script>
                                                                        // 拿到待删除节点:
                                                                        var self = document.getElementById('to-be-removed');
                                                                        // 拿到父节点:
                                                                        var parent = self.parentElement;
                                                                        // 删除:
                                                                        var removed = parent.removeChild(self);
                                                                        removed === self; // true
                                                                        </script>

                                                                        注意到删除后的节点虽然不在文档树中了，但其实它还在内存中，可以随时再次被添加到别的位置。
                                                                        当你遍历一个父节点的子节点并进行删除操作时，要注意，children属性是一个只读属性，并且它在子节点变化时会实时更新。
                                                                        例如，对于如下HTML结构：
                                                                                <div id="parent">
                                                                                    <p>First</p>
                                                                                    <p>Second</p>
                                                                                </div>
                                                                        当我们用如下代码删除子节点时：
                                                                            var parent = document.getElementById('parent');
                                                                            parent.removeChild(parent.children[0]);
                                                                            parent.removeChild(parent.children[1]); // <-- 浏览器报错
                                                                        浏览器报错：parent.children[1]不是一个有效的节点。原因就在于，当<p>First</p>节点被删除后，parent.children的节点数量
                                                                        已经从2变为了1，索引[1]已经不存在了。
                                                                        因此，删除多个节点时，要注意children属性时刻都在变化。

                                                                        亲自试一试
                                                            例子解释：
                                                                        这个 HTML 文档含有拥有两个子节点（两个 <p> 元素）的 <div> 元素：
                                                                        <div id="div1">
                                                                        <p id="p1">这是一个段落。</p>
                                                                        <p id="p2">这是另一个段落。</p>
                                                                        </div>
                                                                        找到 id="div1" 的元素：
                                                                        var parent=document.getElementById("div1");
                                                                        找到 id="p1" 的 <p> 元素：
                                                                        var child=document.getElementById("p1");
                                                                        从父元素中删除子元素：
                                                                        parent.removeChild(child);
                                                                        提示：如果能够在不引用父元素的情况下删除某个元素，就太好了。
                                                                        不过很遗憾。DOM 需要清楚您需要删除的元素，以及它的父元素。
                                                                        这是常用的解决方案：找到您希望删除的子元素，然后使用其 parentNode 属性来找到父元素：
                                                                        var child=document.getElementById("p1");
                                                                        child.parentNode.removeChild(child);                                                                        
                        改变 HTML 样式 -- document.getElementById(id).style.property=new style
                        查找 HTML 元素
                                                通过 id 找到 HTML 元素 - document.getElementById() -- ID在HTML文档中是唯一的，可以直接定位唯一的一个DOM节点
                                                通过标签名找到 HTML 元素 - document.getElementsByTagName() -- 总是返回一组DOM节点，要精确地选择DOM，可以先定位父节点，再从父节点开始选择，以缩小范围
                                                通过类名找到 HTML 元素 - document.getElementsByClassName() -- 总是返回一组DOM节点，要精确地选择DOM，可以先定位父节点，再从父节点开始选择，以缩小范围
                                                例如：
                                                            // 返回ID为'test'的节点：
                                                            var test = document.getElementById('test');

                                                            // 先定位ID为'test-table'的节点，再返回其内部所有tr节点：
                                                            var trs = document.getElementById('test-table').getElementsByTagName('tr');

                                                            // 先定位ID为'test-div'的节点，再返回其内部所有class包含red的节点：
                                                            var reds = document.getElementById('test-div').getElementsByClassName('red');

                                                            // 获取节点test下的所有直属子节点:
                                                            var cs = test.children;

                                                            // 获取节点test下第一个、最后一个子节点：
                                                            var first = test.firstElementChild;
                                                            var last = test.lastElementChild;

                                                使用 querySelector()和 querySelectorAll() -- 然后使用条件来获取节点，更加方便
                                                例
                                                                        // 通过querySelector获取ID为q1的节点：
                                                                        var q1 = document.querySelector('#q1');

                                                                        // 通过querySelectorAll获取q1节点内的符合条件的所有节点：
                                                                        var ps = q1.querySelectorAll('div.highlighted > p');
                        改变 CSS 
            JS HTML DOM 事件() -- 实现在事件发生时执行 JavaScript
                        HTML 事件的例子 
                                    •   当用户点击鼠标时 -- onmousedown, onmouseup 以及 onclick 构成了鼠标点击事件的所有部分
                                    •   当网页已加载时 -- onload 和 onunload 事件会在用户进入或离开页面时被触发 -- 可用于处理 cookie
                                    •   当图像已加载时
                                    •   当鼠标移动到元素上时 -- onmouseover 和 onmouseout 事件可用于在用户的鼠标移至 HTML 元素上方或移出元素时触发函数
                                    •   当输入字段被改变时 -- onchange 事件常结合对输入字段的验证来使用
                                    •   当提交 HTML 表单时
                                    •   当用户触发按键时
                                    •   当输入字段获得焦点时 -- onfocus
                        对页面中的所有事件做出反应 -- 可以在事件发生时执行 JavaScript
                                    onload 和 onunload 事件会在用户进入或离开页面时被触发   
                                    onchange 事件常结合对输入字段的验证来使用 
                                    onmouseover 和 onmouseout 事件可用于在用户的鼠标移至 HTML 元素上方或移出元素时触发函数
                                    onmousedown, onmouseup 以及 onclick 构成鼠标点击事件的所有部分--点击鼠标按钮时，触发 onmousedown 事件，释放鼠标按钮时，触发 onmouseup 事件，
                                    最后，完成鼠标点击时，触发 onclick 事件                                    
            JS Window -- 浏览器对象模型(BOM，Browser Object Model) --  使 JavaScript 有能力与浏览器“对话”
                        JS Window -- window 对象 -- 表示浏览器窗口 -- 所有 JavaScript 全局对象、函数以及变量均自动成为 window 对象的成员
                                    全局变量是 window 对象的属性。
                                    全局函数是 window 对象的方法。
                                    HTML DOM 的 document 也是 window 对象的属性之一       
                                    Window 尺寸-- 浏览器的视口，不包括工具栏和滚动条             
                                                window.innerHeight - 浏览器窗口的内部高度
                                                window.innerWidth - 浏览器窗口的内部宽度
                                                实用的 JavaScript 方案（涵盖所有浏览器）：
                                                            实例
                                                            var w=window.innerWidth
                                                            || document.documentElement.clientWidth
                                                            || document.body.clientWidth;
                                                            var h=window.innerHeight
                                                            || document.documentElement.clientHeight
                                                            || document.body.clientHeight;                                                
                                                其他 Window 方法
                                                            window.open() - 打开新窗口
                                                            window.close() - 关闭当前窗口
                                                            window.moveTo() - 移动当前窗口
                                                            window.resizeTo() - 调整当前窗口的尺寸                        
                        JS Screen -- window.screen 对象包含有关用户屏幕的信息 -- 在编写时可以不使用 window 这个前缀
                                    screen.width：屏幕宽度，以像素为单位
                                    screen.availWidth -- 可用的屏幕宽度 -- 返回访问者屏幕的宽度，以像素计，减去界面特性，比如窗口任务栏
                                    screen.height：屏幕高度，以像素为单位
                                    screen.availHeight -- 可用的屏幕高度 -- 返回访问者屏幕的高度，以像素计，减去界面特性，比如窗口任务栏     
                                    screen.colorDepth：返回颜色位数，如8、16、24
                        JS Location -- 用于获得当前页面的地址 (URL)，并把浏览器重定向到新的页面
                                    location.hostname 返回 web 主机的域名                                                  127.0.0.1
                                    location.pathname 返回当前页面的路径和文件名                                        /
                                    location.port 返回 web 主机的端口 （80 或 443）                                     9000
                                    location.protocol 返回所使用的 web 协议（http: 或 https:）                       http:
                                    location.href 属性返回当前页面的 URL                                                       http://127.0.0.1:9000/
                                    location.search                                                                                         '?a=1&b=2'
                                    location.assign() 方法 加载新的文档        
                                                <script>
                                                function newDoc()
                                                  {
                                                  window.location.assign("http://127.0.0.1:9000/static/img/blue.jpg")
                                                  }
                                                </script>
                                                <input type="button" value="加载新文档" onclick="newDoc()"> 
                                    location.reload() 方法 重新加载当前页面                                             
                        JS document -- 对象表示当前页面
                                    由于HTML在浏览器中以DOM形式表示为树形结构，document对象就是整个DOM树的根节点
                                    document的title属性 是从HTML文档中的<title>xxx</title>读取的，但是可以动态改变
                                    要查找DOM树的某个节点，需要从document对象开始查找。最常用的查找是根据ID和Tag Name
                                                我们先准备HTML数据：
                                                <dl id="drink-menu" style="border:solid 1px #ccc;padding:6px;">
                                                    <dt>摩卡</dt>
                                                    <dd>热摩卡咖啡</dd>
                                                    <dt>酸奶</dt>
                                                    <dd>北京老酸奶</dd>
                                                    <dt>果汁</dt>
                                                    <dd>鲜榨苹果汁</dd>
                                                </dl>
                                    用document对象提供的 getElementById() 和 getElementsByTagName() 可以按ID获得一个DOM节点和按Tag名称获得一组DOM节点
                                    document对象 还有一个cookie属性，可以获取当前页面的Cookie  -- JavaScript可以通过document.cookie读取到当前页面的Cookie
                        JS History -- window.history 对象包含浏览器的历史
                                    history.back() - 与在浏览器点击后退按钮相同 -- 加载历史列表中的前一个 URL
                                    history.forward() - 与在浏览器中点击按钮向前相同 -- 加载历史列表中的下一个 URL
                        JS Navigator -- window.navigator 对象包含有关访问者浏览器的信息
                                    实例
                                                <div id="example"></div>
                                                <script>
                                                txt = "<p>Browser CodeName: " + navigator.appCodeName + "</p>";
                                                txt+= "<p>Browser Name: " + navigator.appName + "</p>";
                                                txt+= "<p>Browser Version: " + navigator.appVersion + "</p>";
                                                txt+= "<p>Cookies Enabled: " + navigator.cookieEnabled + "</p>";
                                                txt+= "<p>Platform: " + navigator.platform + "</p>";
                                                txt+= "<p>User-agent header: " + navigator.userAgent + "</p>";
                                                txt+= "<p>User-agent language: " + navigator.systemLanguage + "</p>";
                                                document.getElementById("example").innerHTML=txt;
                                                </script>
                                    亲自试一试
                                                警告：来自 navigator 对象的信息具有误导性，不应该被用于检测浏览器版本，这是因为：
                                                navigator 数据可被浏览器使用者更改
                                                浏览器无法报告晚于浏览器发布的新操作系统
                                                浏览器检测
                                                由于 navigator 可误导浏览器检测，使用对象检测可用来嗅探不同的浏览器。
                                                由于不同的浏览器支持不同的对象，您可以使用对象来检测浏览器。例如，由于只有 Opera 支持属性 "window.opera"，您可以据此识别出 Opera。
                                                例子：if (window.opera) {...some action...}                        
                        JS PopupAlert -- 可以在 JavaScript 中创建三种消息框：警告框、确认框、提示框
                                    警告框 -- 经常用于确保用户可以得到某些信息 -- 当警告框出现后，用户需要点击确定按钮才能继续进行操作 -- 语法 - alert("文本")
                                    确认框 -- 用于使用户可以验证或者接受某些信息 -- 当确认框出现后，用户需要点击确定或者取消按钮才能继续进行操作 - 语法 - confirm("文本")
                                    提示框 -- 经常用于提示用户在进入页面前输入某个值 -- 当提示框出现后，用户需要输入某个值，然后点击确认或取消按钮才能继续操纵 - prompt("文本","默认值")
                        JS Timing - 计时 -- 在一个设定的时间间隔之后来执行代码，而不是在函数被调用后立即执行。我们称之为计时事件
                                    setTimeout() -- 未来的某时执行代码 - 语法 -- var t=setTimeout("javascript语句",毫秒)
                                                语法
                                                            var t=setTimeout("javascript语句",毫秒)
                                                            setTimeout() 方法会返回某个值。在上面的语句中，值被储存在名为 t 的变量中。假如你希望取消这个 setTimeout()，你可以使用这个
                                                            变量名来指定它。
                                                            setTimeout() 的第一个参数是含有 JavaScript 语句的字符串。这个语句可能诸如 "alert('5 seconds!')"，或者对函数的调用，
                                                            诸如 alertMsg()。
                                                            第二个参数指示从当前起多少毫秒后执行第一个参数。
                                                            提示：1000 毫秒等于一秒。
                                                实例
                                                            当下面这个例子中的按钮被点击时，一个提示框会在5秒中后弹出。
                                                            <html>
                                                            <head>
                                                            <script type="text/javascript">
                                                            function timedMsg()
                                                             {
                                                             var t=setTimeout("alert('5 seconds!')",5000)
                                                             }
                                                            </script>
                                                            </head>
                                                            <body>
                                                            <form>
                                                            <input type="button" value="Display timed alertbox!" onClick="timedMsg()">
                                                            </form>
                                                            </body>
                                                            </html>
                                                实例 - 无穷循环
                                                            要创建一个运行于无穷循环中的计时器，我们需要编写一个函数来调用其自身。在下面的例子中，当按钮被点击后，输入域便从 0 开始计数。
                                                            <html>
                                                            <head>
                                                            <script type="text/javascript">
                                                            var c=0
                                                            var t
                                                            function timedCount()
                                                             {
                                                             document.getElementById('txt').value=c
                                                             c=c+1
                                                             t=setTimeout("timedCount()",1000)
                                                             }
                                                            </script>
                                                            </head>
                                                            <body>
                                                            <form>
                                                            <input type="button" value="Start count!" onClick="timedCount()">
                                                            <input type="text" id="txt">
                                                            </form>
                                                            </body>
                                                            </html>                                    
                                    clearTimeout() -- 取消 setTimeout()
                                                语法
                                                            clearTimeout(setTimeout_variable)
                                                实例
                                                            下面的例子和上面的无穷循环的例子相似。唯一的不同是，现在我们添加了一个 "Stop Count!" 按钮来停止这个计数器：
                                                            <html>
                                                            <head>
                                                            <script type="text/javascript">
                                                            var c=0
                                                            var t
                                                            function timedCount()
                                                             {
                                                             document.getElementById('txt').value=c
                                                             c=c+1
                                                             t=setTimeout("timedCount()",1000)
                                                             }
                                                            function stopCount()
                                                             {
                                                             clearTimeout(t)
                                                             }
                                                            </script>
                                                            </head>
                                                            <body>
                                                            <form>
                                                            <input type="button" value="Start count!" onClick="timedCount()">
                                                            <input type="text" id="txt">
                                                            <input type="button" value="Stop count!" onClick="stopCount()">
                                                            </form>
                                                            </body>
                                                            </html>                                                                                                                                
                                    简单的计时 -- 单击本例中的按钮后，会在 5 秒后弹出一个警告框                                                                                                                                                
                                                <html>
                                                <head>
                                                <script type="text/javascript">
                                                function timedMsg()
                                                {
                                                var t=setTimeout("alert('5 秒！')",5000)
                                                }
                                                </script>
                                                </head>
                                                <body>
                                                <form>
                                                <input type="button" value="显示定时的警告框" onClick = "timedMsg()">
                                                </form>
                                                <p>请点击上面的按钮。警告框会在 5 秒后显示。</p>
                                                </body>
                                                </html>
                                    另一个简单的计时 -- 本例中的程序会执行 2 秒、4 秒和 6 秒的计时                                                                                                                                                 
                                                <html>
                                                <head>
                                                <script type="text/javascript">
                                                function timedText()
                                                {
                                                var t1=setTimeout("document.getElementById('txt').value='2 秒'",2000)
                                                var t2=setTimeout("document.getElementById('txt').value='4 秒'",4000)
                                                var t3=setTimeout("document.getElementById('txt').value='6 秒'",6000)
                                                }
                                                </script>
                                                </head>
                                                <body>
                                                <form>
                                                <input type="button" value="显示计时的文本" onClick="timedText()">
                                                <input type="text" id="txt">
                                                </form>
                                                <p>点击上面的按钮。输入框会显示出已经逝去的时间（2、4、6 秒）。</p>
                                                </body>
                                                </html>
                                    在一个无穷循环中的计时事件 -- 在本例中，单击开始计时按钮后，程序开始从 0 以秒计时。                                                                                                                                               
                                                <html>
                                                <head>
                                                <script type="text/javascript">
                                                var c=0
                                                var t
                                                function timedCount()
                                                {
                                                document.getElementById('txt').value=c
                                                c=c+1
                                                t=setTimeout("timedCount()",1000)
                                                }
                                                </script>
                                                </head>
                                                <body>
                                                <form>
                                                <input type="button" value="开始计时！" onClick="timedCount()">
                                                <input type="text" id="txt">
                                                </form>
                                                <p>请点击上面的按钮。输入框会从 0 开始一直进行计时。</p>
                                                </body>
                                                </html>
                                    带有停止按钮的无穷循环中的计时事件--在本例中，点击计数按钮后根据用户输入的数值开始倒计时，点击停止按钮停止计时。                                                                                                                                                
                                                <html>
                                                <head>
                                                <script type="text/javascript">
                                                var c=0
                                                var t
                                                function timedCount()
                                                {
                                                document.getElementById('txt').value=c
                                                c=c+1
                                                t=setTimeout("timedCount()",1000)
                                                }
                                                function stopCount()
                                                {
                                                c=0;
                                                setTimeout("document.getElementById('txt').value=0",0);
                                                clearTimeout(t);
                                                }
                                                </script>
                                                </head>
                                                <body>
                                                <form>
                                                <input type="button" value="开始计时！" onClick="timedCount()">
                                                <input type="text" id="txt">
                                                <input type="button" value="停止计时！" onClick="stopCount()">
                                                </form>
                                                <p>请点击上面的“开始计时”按钮来启动计时器。输入框会一直进行计时，从 0 开始。点击“停止计时”按钮可以终止计时，
                                                并将计数重置为 0。</p>
                                                </body>
                                                </html>
                                    使用计时事件制作的钟表 -- 一个 JavaScript 小时钟                                                                                                                                                
                                                <html>
                                                <head>
                                                <script type="text/javascript">
                                                function startTime()
                                                {
                                                var today=new Date()
                                                var h=today.getHours()
                                                var m=today.getMinutes()
                                                var s=today.getSeconds()
                                                // add a zero in front of numbers<10
                                                m=checkTime(m)
                                                s=checkTime(s)
                                                document.getElementById('txt').innerHTML=h+":"+m+":"+s
                                                t=setTimeout('startTime()',500)
                                                }
                                                function checkTime(i)
                                                {
                                                if (i<10) 
                                                  {i="0" + i}
                                                  return i
                                                }
                                                </script>
                                                </head>
                                                <body onload="startTime()">
                                                <div id="txt"></div>
                                                </body>
                                                </html>
            JS Cookies - cookie 用来识别用户 -- cookie 是存储于访问者的计算机中的变量 
                        每当同一台计算机通过浏览器请求某个页面时，就会发送这个 cookie。你可以使用 JavaScript 来创建和取回 cookie 的值
                        名字 cookie
                                    当访问者首次访问页面时，他或她也许会填写他/她们的名字。名字会存储于 cookie 中。
                                    当访问者再次访问网站时，他们会收到类似 "Welcome John Doe!" 的欢迎词。而名字则是从 cookie 中取回的。
                        密码 cookie
                                    当访问者首次访问页面时，他或她也许会填写他/她们的密码。密码也可被存储于 cookie 中。当他们再次访问网站时，
                                    密码就会从 cookie 中取回。
                        日期 cookie
                                    当访问者首次访问你的网站时，当前的日期可存储于 cookie 中。当他们再次访问网站时，他们会收到类似这样的一条
                                    消息："Your last visit was on Tuesday August 11, 2005!"。日期也是从 cookie 中取回的                                    
                        创建和存储 cookie
                                    在这个例子中我们要创建一个存储访问者名字的 cookie。当访问者首次访问网站时，他们会被要求填写姓名。名字会存储于
                                    cookie 中。当访问者再次访问网站时，他们就会收到欢迎词。
                                    首先，我们会创建一个可在 cookie 变量中存储访问者姓名的函数：
                                                function setCookie(c_name,value,expiredays)
                                                {
                                                var exdate=new Date()
                                                exdate.setDate(exdate.getDate()+expiredays)
                                                document.cookie=c_name+ "=" +escape(value)+
                                                ((expiredays==null) ? "" : ";expires="+exdate.toGMTString())
                                                }
                                    上面这个函数中的参数存有 cookie 的名称、值以及过期天数。
                                                在上面的函数中，我们首先将天数转换为有效的日期，然后，我们将 cookie 名称、值及其过期日期存入 document.cookie 对象。
                                    之后，我们要创建另一个函数来检查是否已设置 cookie：
                                                function getCookie(c_name)
                                                {
                                                if (document.cookie.length>0)
                                                  {
                                                  c_start=document.cookie.indexOf(c_name + "=")
                                                  if (c_start!=-1)
                                                    { 
                                                    c_start=c_start + c_name.length+1 
                                                    c_end=document.cookie.indexOf(";",c_start)
                                                    if (c_end==-1) c_end=document.cookie.length
                                                    return unescape(document.cookie.substring(c_start,c_end))
                                                    } 
                                                  }
                                                return ""
                                                }
                                                上面的函数首先会检查 document.cookie 对象中是否存有 cookie。假如 document.cookie 对象存有某些 cookie，那么会继续
                                                检查我们指定的 cookie 是否已储存。如果找到了我们要的 cookie，就返回值，否则返回空字符串。
                                    最后，我们要创建一个函数，这个函数的作用是：如果 cookie 已设置，则显示欢迎词，否则显示提示框来要求用户输入名字。
                                                function checkCookie()
                                                {
                                                username=getCookie('username')
                                                if (username!=null && username!="")
                                                  {alert('Welcome again '+username+'!')}
                                                else 
                                                  {
                                                  username=prompt('Please enter your name:',"")
                                                  if (username!=null && username!="")
                                                    {
                                                    setCookie('username',username,365)
                                                    }
                                                  }
                                                }
                                    这是所有的代码：
                                                <html>
                                                <head>
                                                <script type="text/javascript">
                                                function getCookie(c_name)
                                                {
                                                if (document.cookie.length>0)
                                                  c_start=document.cookie.indexOf(c_name + "=")
                                                  if (c_start!=-1)
                                                    { 
                                                    c_start=c_start + c_name.length+1 
                                                    c_end=document.cookie.indexOf(";",c_start)
                                                    if (c_end==-1) c_end=document.cookie.length
                                                    return unescape(document.cookie.substring(c_start,c_end))
                                                    } 
                                                  }
                                                return ""
                                                }
                                                function setCookie(c_name,value,expiredays)
                                                {
                                                var exdate=new Date()
                                                exdate.setDate(exdate.getDate()+expiredays)
                                                document.cookie=c_name+ "=" +escape(value)+
                                                ((expiredays==null) ? "" : ";expires="+exdate.toGMTString())
                                                }
                                                function checkCookie()
                                                {
                                                username=getCookie('username')
                                                if (username!=null && username!="")
                                                  {alert('Welcome again '+username+'!')}
                                                else 
                                                  {
                                                  username=prompt('Please enter your name:',"")
                                                  if (username!=null && username!="")
                                                    {
                                                    setCookie('username',username,365)
                                                    }
                                                  }
                                                }
                                                </script>
                                                </head>
                                                <body onLoad="checkCookie()">
                                                </body>
                                                </html>

            AJAX -- Asynchronous JavaScript and XML -- 用JavaScript执行异步网络请求 -- 不是JavaScript的规范
                        Web的运作原理：一次HTTP请求对应一个页面。
                                如果仔细观察一个Form的提交，你就会发现，一旦用户点击“Submit”按钮，表单开始提交，浏览器就会刷新页面，
                                然后在新页面里告诉你操作是成功了还是失败了。如果不幸由于网络太慢或者其他原因，就会得到一个404页面

                                如果要让用户留在当前页面中，同时发出新的HTTP请求，就必须用JavaScript发送这个新请求，接收到数据后，再用
                                JavaScript更新页面，这样一来，用户就感觉自己仍然停留在当前页面，但是数据却可以不断地更新。

                                最早大规模使用AJAX的就是Gmail，Gmail的页面在首次加载后，剩下的所有数据都依赖于AJAX来更新。

                        用JavaScript写一个完整的AJAX代码并不复杂，但是需要注意：AJAX请求是异步执行的，也就是说，要通过回调函数获得响应。

                        在现代浏览器上写AJAX主要依靠 XMLHttpRequest对象

                                通过检测window对象是否有XMLHttpRequest属性来确定浏览器是否支持标准的XMLHttpRequest，然后创建XMLHttpRequest对象
                                        如果想把标准写法和IE写法混在一起，可以这么写：
                                                var request;
                                                if (window.XMLHttpRequest) {
                                                    request = new XMLHttpRequest();
                                                } else {
                                                    request = new ActiveXObject('Microsoft.XMLHTTP');
                                                }
                                        注意，不要根据浏览器的navigator.userAgent来检测浏览器是否支持某个JavaScript特性，一是因为这个字符串本身可以伪造，
                                        二是通过IE版本判断JavaScript特性将非常复杂。
                                当创建了XMLHttpRequest对象后，要先设置 onreadystatechange 的回调函数。在回调函数中，通常我们只需通过readyState === 4 判断
                                请求是否完成，如果已完成，再根据status === 200判断是否是一个成功的响应。

                                XMLHttpRequest对象的 open() 方法有3个参数，第一个参数指定是GET还是POST，第二个参数指定URL地址（相对路径），第三个参数指定是否使用异步，
                                默认是true，所以不用写。
                                注意，千万不要把第三个参数指定为false，否则浏览器将停止响应，直到AJAX请求完成。如果这个请求耗时10秒，那么10秒内你会发现浏览器
                                处于“假死”状态。
                                最后调用 send()方法才真正发送请求。GET请求不需要参数，POST请求需要把body部分以字符串或者FormData对象传进去

                        安全限制
                                上面代码的URL使用的是相对路径。如果你把它改为'http://www.sina.com.cn/'，再运行，肯定报错。在Chrome的控制台里，还可以看到错误信息。
                                这是因为浏览器的同源策略导致的。默认情况下，JavaScript在发送AJAX请求时，URL的域名必须和当前页面完全一致。
                                完全一致的意思是，域名要相同（www.example.com和example.com不同），协议要相同（http和https不同），端口号要相同
                                （默认是:80端口，它和:8080就不同）。有的浏览器口子松一点，允许端口不同，大多数浏览器都会严格遵守这个限制。

                        那是不是用JavaScript无法请求外域（就是其他网站）的URL了呢？方法还是有的，大概有这么几种：
                                一是通过Flash插件发送HTTP请求，这种方式可以绕过浏览器的安全限制，但必须安装Flash，并且跟Flash交互。不过Flash用起来麻烦，而且现在用得也越来越少了。
                                二是通过在同源域名下架设一个代理服务器来转发，JavaScript负责把请求发送到代理服务器
                                第三种方式称为JSONP，它有个限制，只能用GET请求，并且要求返回JavaScript。这种方式跨域实际上是利用了浏览器允许跨域引用JavaScript资源
                                        <html>
                                        <head>
                                            <script src="http://example.com/abc.js"></script>
                                            ...
                                        </head>
                                        <body>
                                        ...
                                        </body>
                                        </html>
                                        JSONP通常以函数调用的形式返回，例如，返回JavaScript内容如下：
                                        foo('data');
                                        这样一来，我们如果在页面中先准备好foo()函数，然后给页面动态加一个<script>节点，相当于动态读取外域的JavaScript资源，
                                        最后就等着接收回调了

                                        以163的股票查询URL为例
                                                对于URL：http://api.money.126.net/data/feed/0000001,1399001?callback=refreshPrice，你将得到如下返回：
                                                refreshPrice({"0000001":{"code": "0000001", ... });
                                                因此我们需要首先在页面中准备好回调函数：
                                                        function refreshPrice(data) {
                                                            var p = document.getElementById('test-jsonp');
                                                            p.innerHTML = '当前价格：' +
                                                                data['0000001'].name +': ' + 
                                                                data['0000001'].price + '；' +
                                                                data['1399001'].name + ': ' +
                                                                data['1399001'].price;
                                                        }
                                                        当前价格：
                                                        刷新
                                                最后用getPrice()函数触发：
                                                        function getPrice() {
                                                            var
                                                                js = document.createElement('script'),
                                                                head = document.getElementsByTagName('head')[0];
                                                            js.src = 'http://api.money.126.net/data/feed/0000001,1399001?callback=refreshPrice';
                                                            head.appendChild(js);
                                                        }
                                                        就完成了跨域加载数据。
                                        发现一个问题,假如我们每隔一段时间就用jsonp获取数据. 那么head里边的script标签多到会炸吧. 每次请求新数据前记得把上次的script标签移除.
                                        修复Ajax请求不断增加新script的小bug

                                                function refreshPrice(data) {
                                                    var p = document.getElementById('test-jsonp');
                                                    p.innerHTML = '当前价格：' +
                                                        data['0000001'].name +': ' + 
                                                        data['0000001'].price + '；' +
                                                        data['1399001'].name + ': ' +
                                                        data['1399001'].price;
                                                }

                                                function getPrice() {
                                                    var
                                                        js = document.createElement('script'),
                                                        head = document.getElementsByTagName('head')[0],
                                                        self = document.getElementById('dynamic-jsonp');
                                                    if (self) {
                                                        var parent = self.parentElement;    
                                                        parent.removeChild(self);
                                                    }
                                                    js.id = 'dynamic-jsonp';
                                                    js.src = 'http://api.money.126.net/data/feed/0000001,1399001?callback=refreshPrice';
                                                    head.appendChild(js);
                                                }
                                CORS -- Cross-Origin Resource Sharing - 新的跨域策略 - 是HTML5规范定义的如何跨域访问资源

                                        我们先搞明白概念：
                                                Origin表示本域，也就是浏览器当前页面的域。当JavaScript向外域（如sina.com）发起请求后，浏览器收到响应后，
                                                首先检查Access-Control-Allow-Origin是否包含本域，如果是，则此次跨域请求成功，如果不是，则请求失败，JavaScript将
                                                无法获取到响应的任何数据。

                                                假设本域是my.com，外域是sina.com，只要响应头Access-Control-Allow-Origin为http://my.com，或者是*，本次请求就可以成功。
                                                可见，跨域能否成功，取决于对方服务器是否愿意给你设置一个正确的Access-Control-Allow-Origin，决定权始终在对方手中。

                                                上面这种跨域请求，称之为“简单请求”。简单请求包括GET、HEAD和POST（POST的Content-Type类型 仅限application/x-www-form-urlencoded、
                                                multipart/form-data和text/plain），并且不能出现任何自定义头（例如，X-Custom: 12345），通常能满足90%的需求

                                        无论你是否需要用JavaScript通过CORS跨域请求资源，你都要了解CORS的原理。最新的浏览器全面支持HTML5。在引用外域资源时，
                                        除了JavaScript和CSS外，都要验证CORS。例如，当你引用了某个第三方CDN上的字体文件时：
                                                /* CSS */
                                                @font-face {
                                                  font-family: 'FontAwesome';
                                                  src: url('http://cdn.com/fonts/fontawesome.ttf') format('truetype');
                                                }
                                        如果该CDN服务商未正确设置Access-Control-Allow-Origin，那么浏览器无法加载字体资源。
                                        对于PUT、DELETE以及其他类型如application/json的POST请求，在发送AJAX请求之前，浏览器会先发送一个OPTIONS请求
                                        （称为preflighted请求）到这个URL上，询问目标服务器是否接受：
                                                OPTIONS /path/to/resource HTTP/1.1
                                                Host: bar.com
                                                Origin: http://my.com
                                                Access-Control-Request-Method: POST
                                        服务器必须响应并明确指出允许的Method：
                                                HTTP/1.1 200 OK
                                                Access-Control-Allow-Origin: http://my.com
                                                Access-Control-Allow-Methods: POST, GET, PUT, OPTIONS
                                                Access-Control-Max-Age: 86400
                                        浏览器确认服务器响应的Access-Control-Allow-Methods头确实包含将要发送的AJAX请求的Method，才会继续发送AJAX，
                                        否则，抛出一个错误。
                                        由于以POST、PUT方式传送JSON格式的数据在REST中很常见，所以要跨域正确处理POST和PUT请求，服务器端必须正确响应OPTIONS请求。
                                        需要深入了解CORS的童鞋请移步 W3C文档。
            Promise -- 异步执行 -- 回调函数实现 -- promise就是eventloop + future

                        在JavaScript的世界中，所有代码都是单线程执行的。
                        由于这个“缺陷”，导致JavaScript的所有网络操作，浏览器事件，都必须是异步执行。异步执行可以用回调函数实现
                        例
                                function callback() {
                                    console.log('Done');
                                }
                                console.log('before setTimeout()');
                                setTimeout(callback, 1000); // 1秒钟后调用callback函数
                                console.log('after setTimeout()');
                                观察上述代码执行，在Chrome的控制台输出可以看到：
                                before setTimeout()
                                after setTimeout()
                                (等待1秒后)
                                Done
                        可见，异步操作会在将来的某个时间点触发一个函数调用

                        AJAX就是典型的异步操作。以上一节的代码为例：
                        request.onreadystatechange = function () {
                            if (request.readyState === 4) {
                                if (request.status === 200) {
                                    return success(request.responseText);
                                } else {
                                    return fail(request.status);
                                }
                            }
                        }
                        把回调函数success(request.responseText)和fail(request.status)写到一个AJAX操作里很正常，但是不好看，而且不利于代码复用。
                        有没有更好的写法？比如写成这样：
                                var ajax = ajaxGet('http://...');
                                ajax.ifSuccess(success)
                                    .ifFail(fail);
                                这种链式写法的好处在于，先统一执行AJAX逻辑，不关心如何处理结果，然后，根据结果是成功还是失败，在将来的
                                某个时候调用success函数或fail函数。
                        Promise对象 -- 古人云：“君子一诺千金”，这种“承诺将来会执行”的对象在JavaScript中称为 Promise对象
                        Promise 有各种开源实现，在ES6中被统一规范，由浏览器直接支持
                         
                        一个简单的Promise例子：生成一个0-2之间的随机数，如果小于1，则等待一段时间后返回成功，否则返回失败
                                首先定义一个执行函数
                                        function test(resolve, reject) {
                                            var timeOut = Math.random() * 2;
                                            log('set timeout to: ' + timeOut + ' seconds.');
                                            setTimeout(function () {
                                                if (timeOut < 1) {
                                                    log('call resolve()...');
                                                    resolve('200 OK');
                                                }
                                                else {
                                                    log('call reject()...');
                                                    reject('timeout in ' + timeOut + ' seconds.');
                                                }
                                            }, timeOut * 1000);
                                        }
                                代码解析
                                        这个test()函数有两个参数，这两个参数都是函数，如果执行成功，我们将调用resolve('200 OK')，如果执行失败，
                                        我们将调用reject('timeout in ' + timeOut + ' seconds.')。可以看出，test()函数只关心自身的逻辑，并不关心具体
                                        的resolve和reject将如何处理结果。
                                有了执行函数，我们就可以用一个Promise对象来执行它，并在将来某个时刻获得成功或失败的结果
                                        var p1 = new Promise(test);
                                        var p2 = p1.then(function (result) {
                                            console.log('成功：' + result);
                                        });
                                        var p3 = p2.catch(function (reason) {
                                            console.log('失败：' + reason);
                                        });
                                代码解析
                                变量p1是一个Promise对象，它负责执行test函数。由于test函数在内部是异步执行的，
                                当test函数执行成功时，我们告诉Promise对象：
                                        // 如果成功，执行这个函数：
                                        p1.then(function (result) {
                                            console.log('成功：' + result);
                                        });
                                当test函数执行失败时，我们告诉Promise对象：
                                        p2.catch(function (reason) {
                                            console.log('失败：' + reason);
                                        });
                                Promise对象可以串联起来，所以上述代码可以简化为：
                                        new Promise(test).then(function (result) {
                                            console.log('成功：' + result);
                                        }).catch(function (reason) {
                                            console.log('失败：' + reason);
                                        });
                                实际测试一下，看看Promise是如何异步执行的：
                                        'use strict';

                                        // 清除log:
                                        var logging = document.getElementById('test-promise-log');
                                        while (logging.children.length > 1) {
                                            logging.removeChild(logging.children[logging.children.length - 1]);
                                        }

                                        // 输出log到页面:
                                        function log(s) {
                                            var p = document.createElement('p');
                                            p.innerHTML = s;
                                            logging.appendChild(p);
                                        }

                        可见Promise最大的好处是在异步执行的流程中，把执行代码和处理结果的代码清晰地分离了

                        Promise还可以做更多的事情，比如，有若干个异步任务，需要先做任务1，如果成功后再做任务2，任何任务失败
                        则不再继续并执行错误处理函数。
                        要串行执行这样的异步任务，不用Promise需要写一层一层的嵌套代码。有了Promise，我们只需要简单地写：
                        job1.then(job2).then(job3).catch(handleError);
                        其中，job1、job2和job3都是Promise对象。
                        下面的例子演示了如何串行执行一系列需要异步计算获得结果的任务：
                                'use strict';

                                var logging = document.getElementById('test-promise2-log');
                                while (logging.children.length > 1) {
                                    logging.removeChild(logging.children[logging.children.length - 1]);
                                }

                                function log(s) {
                                    var p = document.createElement('p');
                                    p.innerHTML = s;
                                    logging.appendChild(p);
                                }
                        setTimeout可以看成一个模拟网络等异步执行的函数。现在，我们把上一节的AJAX异步执行函数转换为Promise对象，看看用Promise如何简化异步处理：
                                'use strict';

                                // ajax函数将返回Promise对象:
                                function ajax(method, url, data) {
                                    var request = new XMLHttpRequest();
                                    return new Promise(function (resolve, reject) {
                                        request.onreadystatechange = function () {
                                            if (request.readyState === 4) {
                                                if (request.status === 200) {
                                                    resolve(request.responseText);
                                                } else {
                                                    reject(request.status);
                                                }
                                            }
                                        };
                                        request.open(method, url);
                                        request.send(data);
                                    });
                                }

                        除了串行执行若干异步任务外，Promise还可以并行执行异步任务。
                        试想一个页面聊天系统，我们需要从两个不同的URL分别获得用户的个人信息和好友列表，这两个任务是可以并行执行的，用Promise.all()实现如下：
                                var p1 = new Promise(function (resolve, reject) {
                                    setTimeout(resolve, 500, 'P1');
                                });
                                var p2 = new Promise(function (resolve, reject) {
                                    setTimeout(resolve, 600, 'P2');
                                });
                                // 同时执行p1和p2，并在它们都完成后执行then:
                                Promise.all([p1, p2]).then(function (results) {
                                    console.log(results); // 获得一个Array: ['P1', 'P2']
                                });
                        有些时候，多个异步任务是为了容错。比如，同时向两个URL读取用户的个人信息，只需要获得先返回的结果即可。这种情况下，用Promise.race()实现：
                                var p1 = new Promise(function (resolve, reject) {
                                    setTimeout(resolve, 500, 'P1');
                                });
                                var p2 = new Promise(function (resolve, reject) {
                                    setTimeout(resolve, 600, 'P2');
                                });
                                Promise.race([p1, p2]).then(function (result) {
                                    console.log(result); // 'P1'
                                });
                        由于p1执行较快，Promise的then()将获得结果'P1'。p2仍在继续执行，但执行结果将被丢弃。
                        如果我们组合使用Promise，就可以把很多异步任务以并行和串行的方式组合起来执行
            
            Canvas -- HTML5新增的组件 -- 可以用JavaScript在上面绘制各种图表、动画等
                        一个Canvas定义了一个指定尺寸的矩形框，在这个范围内我们可以随意绘制
                        <canvas id="test-canvas" width="300" height="200"></canvas>

            jQuery
                        jQuery这么流行，肯定是因为它解决了一些很重要的问题。实际上，jQuery能帮我们干这些事情：
                                    •   消除浏览器差异：你不需要自己写冗长的代码来针对不同的浏览器来绑定事件，编写AJAX等代码；
                                    •   简洁的操作DOM的方法：写$('#test')肯定比document.getElementById('test')来得简洁；
                                    •   轻松实现动画、修改CSS等各种操作。
                        jQuery的理念“Write Less, Do More“，让你写更少的代码，完成更多的工作！

                        jQuery版本
                                    目前jQuery有1.x和2.x两个主要版本，区别在于2.x移除了对古老的IE 6、7、8的支持，因此2.x的代码更精简。选择哪个版本主要取决于你是否想支持IE 6~8。
                                    从jQuery官网可以下载最新版本。jQuery只是一个jquery-xxx.js文件，但你会看到有compressed（已压缩）和uncompressed（未压缩）两种版本，
                                    使用时完全一样，但如果你想深入研究jQuery源码，那就用uncompressed版本。
                        使用jQuery -- 使用jQuery只需要在页面的<head>引入jQuery文件即可
                        $符号
                                    $是著名的jQuery符号。实际上，jQuery把所有功能全部封装在一个全局变量jQuery中，而$也是一个合法的变量名，它是变量jQuery的别名
                                                window.jQuery; // jQuery(selector, context)
                                                window.$; // jQuery(selector, context)
                                                $ === jQuery; // true
                                                typeof($); // 'function'
                                    $ 本质上就是一个函数，但是函数也是对象，于是$除了可以直接调用外，也可以有很多其他属性。
                                    注意，你看到的$函数名可能不是jQuery(selector, context)，因为很多JavaScript压缩工具可以对函数名和参数改名，所以压缩过的
                                    jQuery源码$函数可能变成 a(b, c)。
                                    绝大多数时候，我们都直接用$（因为写起来更简单嘛）。但是，如果$这个变量不幸地被占用了，而且还不能改，那我们就只能让jQuery把$变量
                                    交出来，然后就只能使用jQuery这个变量：
                                                $; // jQuery(selector, context)
                                                jQuery.noConflict();
                                                $; // undefined
                                                jQuery; // jQuery(selector, context)
                                    这种黑魔法的原理是jQuery在占用$之前，先在内部保存了原来的$, 调用 jQuery.noConflict()时会把原来保存的变量还原。
                        选择器 -- jQuery的核心 -- 一个选择器写出来类似 $('#dom-id') -- jQuery的选择器就是帮助我们快速定位到一个或多个DOM节点
                                        按ID查找
                                                如果某个DOM节点有id属性，利用jQuery查找如下：
                                                // 查找<div id="abc">:
                                                var div = $('#abc');
                                                注意，#abc以#开头。返回的对象是jQuery对象。
                                                什么是jQuery对象？jQuery对象类似数组，它的每个元素都是一个引用了DOM节点的对象。
                                                以上面的查找为例，如果id为abc的<div>存在，返回的jQuery对象如下：
                                                [<div id="abc">...</div>]
                                                如果id为abc的<div>不存在，返回的jQuery对象如下：
                                                []
                                                总之jQuery的选择器不会返回undefined或者null，这样的好处是你不必在下一行判断if (div === undefined)。
                                                jQuery对象和DOM对象之间可以互相转化：
                                                var div = $('#abc'); // jQuery对象
                                                var divDom = div.get(0); // 假设存在div，获取第1个DOM元素 
                                                var another = $(divDom); // 重新把DOM包装为jQuery对象
                                                通常情况下你不需要获取DOM对象，直接使用jQuery对象更加方便。如果你拿到了一个DOM对象，那可以简单地调用 $(aDomObject)
                                                把它变成jQuery对象，这样就可以方便地使用jQuery的API了。
                                        按tag查找
                                                按tag查找只需要写上tag名称就可以了：
                                                var ps = $('p'); // 返回所有<p>节点
                                                ps.length; // 数一数页面有多少个<p>节点
                                        按class查找
                                                按class查找注意在class名称前加一个.：
                                                var a = $('.red'); // 所有节点包含`class="red"`都将返回
                                                // 例如:
                                                // <div class="red">...</div>
                                                // <p class="green red">...</p>
                                                通常很多节点有多个class，我们可以查找同时包含red和green的节点：
                                                var a = $('.red.green'); // 注意没有空格！
                                                // 符合条件的节点：
                                                // <div class="red green">...</div>
                                                // <div class="blue green red">...</div>
                                        按属性查找
                                                一个DOM节点除了id和class外还可以有很多属性，很多时候按属性查找会非常方便，比如在一个表单中按属性来查找：
                                                        var email = $('[name=email]'); // 找出<??? name="email">
                                                        var passwordInput = $('[type=password]'); // 找出<??? type="password">
                                                        var a = $('[items="A B"]'); // 找出<??? items="A B">
                                                当属性的值包含空格等特殊字符时，需要用双引号括起来。
                                                按属性查找还可以使用前缀查找或者后缀查找：
                                                        var icons = $('[name^=icon]'); // 找出所有name属性值以icon开头的DOM
                                                        // 例如: name="icon-1", name="icon-2"
                                                        var names = $('[name$=with]'); // 找出所有name属性值以with结尾的DOM
                                                        // 例如: name="startswith", name="endswith"
                                                这个方法尤其适合通过class属性查找，且不受class包含多个名称的影响：
                                                        var icons = $('[class^="icon-"]'); // 找出所有class包含至少一个以`icon-`开头的DOM
                                                        // 例如: class="icon-clock", class="abc icon-home"
                                        组合查找
                                                组合查找就是把上述简单选择器组合起来使用。如果我们查找$('[name=email]')，很可能把表单外的<div name="email">也找出来，
                                                但我们只希望查找<input>，就可以这么写：
                                                var emailInput = $('input[name=email]'); // 不会找出<div name="email">
                                                同样的，根据tag和class来组合查找也很常见：
                                                var tr = $('tr.red'); // 找出<tr class="red ...">...</tr>
                                        多项选择器
                                                多项选择器就是把多个选择器用 , 组合起来一块选：
                                                $('p,div'); // 把<p>和<div>都选出来
                                                $('p.red,p.green'); // 把<p class="red">和<p class="green">都选出来
                                                要注意的是，选出来的元素是按照它们在HTML中出现的顺序排列的，而且不会有重复元素。例如，<p class="red green">不会被
                                                上面的$('p.red,p.green')选择两次。
                                        层级选择器（Descendant Selector）-- 层级选择器更加灵活，也更强大 - 因为DOM的结构就是层级结构，所以我们经常要根据层级关系进行选择
                                                如果两个DOM元素具有层级关系，就可以用$('ancestor descendant')来选择，层级之间用空格隔开。例如：
                                                        <!-- HTML结构 -->
                                                        <div class="testing">
                                                            <ul class="lang">
                                                                <li class="lang-javascript">JavaScript</li>
                                                                <li class="lang-python">Python</li>
                                                                <li class="lang-lua">Lua</li>
                                                            </ul>
                                                        </div>
                                                要选出JavaScript，可以用层级选择器：
                                                        $('ul.lang li.lang-javascript'); // [<li class="lang-javascript">JavaScript</li>]
                                                        $('div.testing li.lang-javascript'); // [<li class="lang-javascript">JavaScript</li>]
                                                        因为<div>和<ul>都是<li>的祖先节点，所以上面两种方式都可以选出相应的<li>节点。
                                                要选择所有的<li>节点，用：$('ul.lang li');
                                                这种层级选择器相比单个的选择器好处在于，它缩小了选择范围，因为首先要定位父节点，才能选择相应的子节点，这样避免了页面其他不相关的元素。
                                                        例如：
                                                        $('form[name=upload] input');
                                                        就把选择范围限定在name属性为upload的表单里。如果页面有很多表单，其他表单的<input>不会被选择。
                                                        多层选择也是允许的：
                                                        $('form.test p input'); // 在form表单选择被<p>包含的<input>
                                        子选择器（Child Selector）
                                                子选择器$('parent>child')类似层级选择器，但是限定了层级关系必须是父子关系，就是<child>节点必须是<parent>节点的直属子节点。
                                                还是以上面的例子：
                                                $('ul.lang>li.lang-javascript'); // 可以选出[<li class="lang-javascript">JavaScript</li>]
                                                $('div.testing>li.lang-javascript'); // [], 无法选出，因为<div>和<li>不构成父子关系
                                        过滤器（Filter）-- 过滤器一般不单独使用，它通常附加在选择器上，帮助我们更精确地定位元素。观察过滤器的效果：
                                                $('ul.lang li'); // 选出JavaScript、Python和Lua 3个节点

                                                $('ul.lang li:first-child'); // 仅选出JavaScript
                                                $('ul.lang li:last-child'); // 仅选出Lua
                                                $('ul.lang li:nth-child(2)'); // 选出第N个元素，N从1开始
                                                $('ul.lang li:nth-child(even)'); // 选出序号为偶数的元素
                                                $('ul.lang li:nth-child(odd)'); // 选出序号为奇数的元素
                                        表单相关
                                        针对表单元素，jQuery还有一组特殊的选择器：
                                                    •   :input：可以选择<input>，<textarea>，<select>和<button>；
                                                    •   :file：可以选择<input type="file">，和input[type=file]一样；
                                                    •   :checkbox：可以选择复选框，和input[type=checkbox]一样；
                                                    •   :radio：可以选择单选框，和input[type=radio]一样；
                                                    •   :focus：可以选择当前输入焦点的元素，例如把光标放到一个<input>上，用$('input:focus')就可以选出；
                                                    •   :checked：选择当前勾上的单选框和复选框，用这个选择器可以立刻获得用户选择的项目，如$('input[type=radio]:checked')；
                                                    •   :enabled：可以选择可以正常输入的<input>、<select> 等，也就是没有灰掉的输入；
                                                    •   :disabled：和:enabled正好相反，选择那些不能输入的。
                                        此外，jQuery还有很多有用的选择器，例如，选出可见的或隐藏的元素：
                                                $('div:visible'); // 所有可见的div
                                                $('div:hidden'); // 所有隐藏的div
                        查找和过滤 -- 通常情况下选择器可以直接定位到我们想要的元素，但是，当我们拿到一个jQuery对象后，还可以以这个对象为基准，进行查找和过滤。
                                    查找
                                            最常见的查找是在某个节点的所有子节点中查找，使用 find()方法，它本身又接收一个任意的选择器。例如如下的HTML结构：
                                                    <!-- HTML结构 -->
                                                    <ul class="lang">
                                                        <li class="js dy">JavaScript</li>
                                                        <li class="dy">Python</li>
                                                        <li id="swift">Swift</li>
                                                        <li class="dy">Scheme</li>
                                                        <li name="haskell">Haskell</li>
                                                    </ul>
                                            用find()查找：
                                                    var ul = $('ul.lang'); // 获得<ul>
                                                    var dy = ul.find('.dy'); // 获得JavaScript, Python, Scheme
                                                    var swf = ul.find('#swift'); // 获得Swift
                                                    var hsk = ul.find('[name=haskell]'); // 获得Haskell
                                            如果要从当前节点开始向上查找，使用 parent()方法：
                                                    var swf = $('#swift'); // 获得Swift
                                                    var parent = swf.parent(); // 获得Swift的上层节点<ul>
                                                    var a = swf.parent('div.red'); // 从Swift的父节点开始向上查找，直到找到某个符合条件的节点并返回
                                            对于位于同一层级的节点，可以通过 next()和 prev()方法
                                                    例如：
                                                    当我们已经拿到Swift节点后：
                                                    var swift = $('#swift');

                                                    swift.next(); // Scheme
                                                    swift.next('[name=haskell]'); // Haskell，因为Haskell是后续第一个符合选择器条件的节点

                                                    swift.prev(); // Python
                                                    swift.prev('.js'); // JavaScript，因为JavaScript是往前第一个符合选择器条件的节点
                                    过滤
                                            和函数式编程的map、filter类似，jQuery对象也有类似的方法。
                                            filter()方法可以过滤掉不符合选择器条件的节点：
                                                    var langs = $('ul.lang li'); // 拿到JavaScript, Python, Swift, Scheme和Haskell
                                                    var a = langs.filter('.dy'); // 拿到JavaScript, Python, Scheme
                                            或者传入一个函数，要特别注意函数内部的this被绑定为DOM对象，不是jQuery对象：
                                                    var langs = $('ul.lang li'); // 拿到JavaScript, Python, Swift, Scheme和Haskell
                                                    langs.filter(function () {
                                                        return this.innerHTML.indexOf('S') === 0; // 返回S开头的节点
                                                    }); // 拿到Swift, Scheme
                                            map()方法把一个jQuery对象包含的若干DOM节点转化为其他对象：
                                                    var langs = $('ul.lang li'); // 拿到JavaScript, Python, Swift, Scheme和Haskell
                                                    var arr = langs.map(function () {
                                                        return this.innerHTML;
                                                    }).get(); // 用get()拿到包含string的Array：['JavaScript', 'Python', 'Swift', 'Scheme', 'Haskell']
                                            此外，一个jQuery对象如果包含了不止一个DOM节点，first()、last()和slice()方法可以返回一个新的jQuery对象，把不需要的DOM节点去掉：
                                                    var langs = $('ul.lang li'); // 拿到JavaScript, Python, Swift, Scheme和Haskell
                                                    var js = langs.first(); // JavaScript，相当于$('ul.lang li:first-child')
                                                    var haskell = langs.last(); // Haskell, 相当于$('ul.lang li:last-child')
                                                    var sub = langs.slice(2, 4); // Swift, Scheme, 参数和数组的slice()方法一致
                        操作DOM
                                    修改Text和HTML
                                    jQuery对象的 text()和 html()方法分别获取节点的文本和原始HTML文本，例如，如下的HTML结构：
                                                <!-- HTML结构 -->
                                                <ul id="test-ul">
                                                    <li class="js">JavaScript</li>
                                                    <li name="book">Java &amp; JavaScript</li>
                                                </ul>
                                    分别获取文本和HTML：
                                                $('#test-ul li[name=book]').text(); // 'Java & JavaScript'
                                                $('#test-ul li[name=book]').html(); // 'Java &amp; JavaScript'
                                    如何设置文本或HTML？jQuery的API设计非常巧妙：无参数调用 text()是获取文本，传入参数就变成设置文本，HTML也是类似操作，自己动手试试：
                                                'use strict';
                                                var j1 = $('#test-ul li.js');
                                                var j2 = $('#test-ul li[name=book]');

                                                •   JavaScript
                                                •   Java & JavaScript

                                                一个jQuery对象可以包含0个或任意个DOM对象，它的方法实际上会作用在对应的每个DOM节点上。在上面的例子中试试：
                                                $('#test-ul li').text('JS'); // 是不是两个节点都变成了JS？
                                                所以jQuery对象的另一个好处是我们可以执行一个操作，作用在对应的一组DOM节点上。即使选择器没有返回任何DOM节点，调用
                                                jQuery对象的方法仍然不会报错：
                                                // 如果不存在id为not-exist的节点：
                                                $('#not-exist').text('Hello'); // 代码不报错，没有节点被设置为'Hello'
                                                这意味着jQuery帮你免去了许多if语句。
                                    修改CSS
                                                jQuery对象有“批量操作”的特点，这用于修改CSS实在是太方便了。考虑下面的HTML结构：
                                                            <!-- HTML结构 -->
                                                            <ul id="test-css">
                                                                <li class="lang dy"><span>JavaScript</span></li>
                                                                <li class="lang"><span>Java</span></li>
                                                                <li class="lang dy"><span>Python</span></li>
                                                                <li class="lang"><span>Swift</span></li>
                                                                <li class="lang dy"><span>Scheme</span></li>
                                                            </ul>
                                                要高亮显示动态语言，调用jQuery对象的css('name', 'value')方法，我们用一行语句实现：
                                                注意，jQuery对象的所有方法都返回一个jQuery对象（可能是新的也可能是自身），这样我们可以进行链式调用，非常方便。
                                                        jQuery对象的css()方法可以这么用：
                                                                    var div = $('#test-div');
                                                                    div.css('color'); // '#000033', 获取CSS属性
                                                                    div.css('color', '#336699'); // 设置CSS属性
                                                                    div.css('color', ''); // 清除CSS属性
                                                                    为了和JavaScript保持一致，CSS属性可以用'background-color'和'backgroundColor'两种格式。
                                                        css()方法将作用于DOM节点的style属性，具有最高优先级。如果要修改class属性，可以用jQuery提供的下列方法：
                                                                    var div = $('#test-div');
                                                                    div.hasClass('highlight'); // false， class是否包含highlight
                                                                    div.addClass('highlight'); // 添加highlight这个class
                                                                    div.removeClass('highlight'); // 删除highlight这个class
                                    显示和隐藏DOM
                                                要隐藏一个DOM，我们可以设置CSS的display属性为none，利用css()方法就可以实现。不过，要显示这个DOM就需要恢复原有的
                                                display属性，这就得先记下来原有的display属性到底是block还是inline还是别的值。
                                                考虑到显示和隐藏DOM元素使用非常普遍，jQuery直接提供show()和hide()方法，我们不用关心它是如何修改display属性的，总之它能正常工作：
                                                var a = $('a[target=_blank]');
                                                a.hide(); // 隐藏
                                                a.show(); // 显示
                                                注意，隐藏DOM节点并未改变DOM树的结构，它只影响DOM节点的显示。这和删除DOM节点是不同的。
                                    获取DOM信息 -- 利用jQuery对象的若干方法，我们直接可以获取DOM的高宽等信息，而无需针对不同浏览器编写特定代码：
                                                // 浏览器可视窗口大小:
                                                        $(window).width(); // 800
                                                        $(window).height(); // 600
                                                // HTML文档大小:
                                                        $(document).width(); // 800
                                                        $(document).height(); // 3500
                                                // 某个div的大小:
                                                var div = $('#test-div');
                                                div.width(); // 600
                                                div.height(); // 300
                                                div.width(400); // 设置CSS属性 width: 400px，是否生效要看CSS是否有效
                                                div.height('200px'); // 设置CSS属性 height: 200px，是否生效要看CSS是否有效
                                                attr()和removeAttr()方法用于操作DOM节点的属性：
                                                // <div id="test-div" name="Test" start="1">...</div>
                                                var div = $('#test-div');
                                                div.attr('data'); // undefined, 属性不存在
                                                div.attr('name'); // 'Test'
                                                div.attr('name', 'Hello'); // div的name属性变为'Hello'
                                                div.removeAttr('name'); // 删除name属性
                                                div.attr('name'); // undefined
                                                prop()方法和attr()类似，但是HTML5规定有一种属性在DOM节点中可以没有值，只有出现与不出现两种，例如：
                                                <input id="test-radio" type="radio" name="test" checked value="1">
                                                等价于：
                                                <input id="test-radio" type="radio" name="test" checked="checked" value="1">
                                                attr()和prop()对于属性checked处理有所不同：
                                                var radio = $('#test-radio');
                                                radio.attr('checked'); // 'checked'
                                                radio.prop('checked'); // true
                                                prop()返回值更合理一些。不过，用is()方法判断更好：
                                                var radio = $('#test-radio');
                                                radio.is(':checked'); // true
                                                类似的属性还有selected，处理时最好用 is(':selected')。
                                    操作表单 -- 对于表单元素，jQuery对象统一提供 val() 方法获取和设置对应的value属性：
                                                /*
                                                    <input id="test-input" name="email" value="">
                                                    <select id="test-select" name="city">
                                                        <option value="BJ" selected>Beijing</option>
                                                        <option value="SH">Shanghai</option>
                                                        <option value="SZ">Shenzhen</option>
                                                    </select>
                                                    <textarea id="test-textarea">Hello</textarea>
                                                */
                                                var
                                                    input = $('#test-input'),
                                                    select = $('#test-select'),
                                                    textarea = $('#test-textarea');

                                                input.val(); // 'test'
                                                input.val('abc@example.com'); // 文本框的内容已变为abc@example.com

                                                select.val(); // 'BJ'
                                                select.val('SH'); // 选择框已变为Shanghai

                                                textarea.val(); // 'Hello'
                                                textarea.val('Hi'); // 文本区域已更新为'Hi'
                                                可见，一个val()就统一了各种输入框的取值和赋值的问题。
                                    修改DOM结构
                                    直接使用浏览器提供的API对DOM结构进行修改，不但代码复杂，而且要针对浏览器写不同的代码。
                                    有了jQuery，我们就专注于操作jQuery对象本身，底层的DOM操作由jQuery完成就可以了，这样一来，修改DOM也大大简化了。

                                    添加DOM
                                                要添加新的DOM节点，除了通过jQuery的 html()这种暴力方法外，还可以用 append()方法，例如：
                                                <div id="test-div">
                                                    <ul>
                                                        <li><span>JavaScript</span></li>
                                                        <li><span>Python</span></li>
                                                        <li><span>Swift</span></li>
                                                    </ul>
                                                </div>
                                                如何向列表新增一个语言？首先要拿到<ul>节点：
                                                var ul = $('#test-div>ul');
                                                然后，调用append()传入HTML片段：
                                                ul.append('<li><span>Haskell</span></li>');
                                                除了接受字符串，append()还可以传入原始的DOM对象，jQuery对象和函数对象：
                                                // 创建DOM对象:
                                                var ps = document.createElement('li');
                                                ps.innerHTML = '<span>Pascal</span>';
                                                // 添加DOM对象:
                                                ul.append(ps);

                                                // 添加jQuery对象:
                                                ul.append($('#scheme'));

                                                // 添加函数对象:
                                                ul.append(function (index, html) {
                                                    return '<li><span>Language - ' + index + '</span></li>';
                                                });
                                                传入函数时，要求返回一个字符串、DOM对象或者jQuery对象。因为jQuery的 append() 可能作用于一组DOM节点，只有传入函数
                                                才能针对每个DOM生成不同的子节点。
                                                append()把DOM添加到最后，prepend()则把DOM添加到最前。
                                                另外注意，如果要添加的DOM节点已经存在于HTML文档中，它会首先从文档移除，然后再添加，也就是说，用append()，你可以移动一个DOM节点。
                                                如果要把新节点插入到指定位置，例如，JavaScript和Python之间，那么，可以先定位到JavaScript，然后用after()方法：
                                                var js = $('#test-div>ul>li:first-child');
                                                js.after('<li><span>Lua</span></li>');
                                                也就是说，同级节点可以用after()或者before()方法。
                                    删除节点
                                                要删除DOM节点，拿到jQuery对象后直接调用 remove()方法就可以了。如果jQuery对象包含若干DOM节点，实际上可以一次删除多个DOM节点：
                                                var li = $('#test-div>ul>li');
                                                li.remove(); // 所有<li>全被删除
                        事件 -- JavaScript -- 单线程 -- 依赖触发事件执行JavaScript代码
                                    背景
                                            因为JavaScript在浏览器中以单线程模式运行，页面加载后，一旦页面上所有的JavaScript代码被执行完后，
                                            就只能依赖触发事件来执行JavaScript代码。
                                            浏览器在接收到用户的鼠标或键盘输入后，会自动在对应的DOM节点上触发相应的事件。如果该节点已经
                                            绑定了对应的JavaScript处理函数，该函数就会自动调用
                                            由于不同的浏览器绑定事件的代码都不太一样，所以用jQuery来写代码，就屏蔽了不同浏览器的差异，我们
                                            总是编写相同的代码。

                                    举个例子，用户点击了超链接时弹出提示框

                                            /* HTML:
                                             *
                                             * <a id="test-link" href="#0">点我试试</a>
                                             *
                                             */

                                            // 获取超链接的jQuery对象:
                                            var a = $('#test-link');
                                            a.on('click', function () {
                                                alert('Hello!');
                                            });
                                            实测：点我试试
                                    代码解读
                                            on方法 用来绑定一个事件，我们需要传入事件名称和对应的处理函数。
                                            另一种更简化的写法是直接调用 click()方法：
                                            a.click(function () {
                                                alert('Hello!');
                                            });
                                            两者完全等价。我们通常用后面的写法。
                                    jQuery 绑定的事件
                                            鼠标事件
                                                    click: 鼠标单击时触发； dblclick：鼠标双击时触发； mouseenter：鼠标进入时触发； mouseleave：鼠标移出时触发； mousemove：鼠标
                                                    在DOM内部移动时触发； hover：鼠标进入和退出时触发两个函数，相当于mouseenter加上mouseleave。
                                            键盘事件
                                                    键盘事件仅作用在当前焦点的DOM上，通常是<input>和<textarea>。
                                                    keydown：键盘按下时触发； keyup：键盘松开时触发； keypress：按一次键后触发。
                                            其他事件
                                                    focus：当DOM获得焦点时触发； blur：当DOM失去焦点时触发； change：当<input>、<select>或<textarea>的内容
                                                    改变时触发； submit：当<form>提交时触发； ready：当页面被载入并且DOM树完成初始化后触发。
                                                    其中，ready仅作用于document对象。由于ready事件在DOM完成初始化后触发，且只触发一次，所以非常适合用来写其他的初始化代码。

                                                            假设我们想给一个<form>表单绑定submit事件，下面的代码没有预期的效果：
                                                                    <html>
                                                                    <head>
                                                                        <script>
                                                                            // 代码有误:
                                                                            $('#testForm').on('submit', function () {
                                                                                alert('submit!');
                                                                            });
                                                                        </script>
                                                                    </head>
                                                                    <body>
                                                                        <form id="testForm">
                                                                            ...
                                                                        </form>
                                                                    </body>
                                                            因为JavaScript在此执行的时候，<form>尚未载入浏览器，所以$('#testForm')返回[]，并没有绑定事件到任何DOM上。
                                                            所以我们自己的初始化代码必须放到document对象的ready事件中，保证DOM已完成初始化：
                                                                    <html>
                                                                    <head>
                                                                        <script>
                                                                            $(document).on('ready', function () {
                                                                                $('#testForm').on('submit', function () {
                                                                                    alert('submit!');
                                                                                });
                                                                            });
                                                                        </script>
                                                                    </head>
                                                                    <body>
                                                                        <form id="testForm">
                                                                            ...
                                                                        </form>
                                                                    </body>
                                                            这样写就没有问题了。因为相关代码会在DOM树初始化后再执行。
                                                            由于ready事件使用非常普遍，所以可以这样简化：
                                                                    $(document).ready(function () {
                                                                        // on('submit', function)也可以简化:
                                                                        $('#testForm').submit(function () {
                                                                            alert('submit!');
                                                                        });
                                                                    });
                                                            甚至还可以再简化为：
                                                                    $(function () {
                                                                        // init...
                                                                    });
                                                            上面的这种写法最为常见。如果你遇到$(function () {...})的形式，牢记这是document对象的ready事件处理函数。
                                                            完全可以反复绑定事件处理函数，它们会依次执行：
                                                                    $(function () {
                                                                        console.log('init A...');
                                                                    });
                                                                    $(function () {
                                                                        console.log('init B...');
                                                                    });
                                                                    $(function () {
                                                                        console.log('init C...');
                                                                    });
                                    事件参数
                                            有些事件，如mousemove和keypress，我们需要获取鼠标位置和按键的值，否则监听这些事件就没什么意义了。所有事件
                                            都会传入Event对象作为参数，可以从Event对象上获取到更多的信息：
                                                    $(function () {
                                                        $('#testMouseMoveDiv').mousemove(function (e) {
                                                            $('#testMouseMoveSpan').text('pageX = ' + e.pageX + ', pageY = ' + e.pageY);
                                                        });
                                                    });
                                            效果实测：mousemove: 在此区域移动鼠标试试
                                    取消绑定
                                            一个已被绑定的事件可以解除绑定，通过 off('click', function) 实现：
                                                    function hello() {
                                                        alert('hello!');
                                                    }
                                                    a.click(hello); // 绑定事件
                                                    // 10秒钟后解除绑定:
                                                    setTimeout(function () {
                                                        a.off('click', hello);
                                                    }, 10000);
                                            需要特别注意的是，下面这种写法是无效的：
                                                    // 绑定事件:
                                                    a.click(function () {
                                                        alert('hello!');
                                                    });
                                                    // 解除绑定:
                                                    a.off('click', function () {
                                                        alert('hello!');
                                                    });
                                            这是因为两个匿名函数虽然长得一模一样，但是它们是两个不同的函数对象，off('click', function () {...}) 无法移除已绑定的第一个匿名函数。
                                            为了实现移除效果，可以使用 off('click') 一次性移除已绑定的click事件的所有处理函数。
                                            同理，无参数调用 off() 一次性移除已绑定的所有类型的事件处理函数。
                                    事件触发条件
                                            一个需要注意的问题是，事件的触发总是由用户操作引发的。例如，我们监控文本框的内容改动：
                                                    var input = $('#test-input');
                                                    input.change(function () {
                                                        console.log('changed...');
                                                    });
                                            当用户在文本框中输入时，就会触发change事件。
                                            但是，如果用JavaScript代码去改动文本框的值，将不会触发change事件：
                                                    var input = $('#test-input');
                                                    input.val('change it!'); // 无法触发change事件
                                            有些时候，我们希望用代码触发change事件，可以直接调用无参数的 change()方法来触发该事件：
                                                    var input = $('#test-input');
                                                    input.val('change it!');
                                                    input.change(); // 触发change事件
                                                    input.change() 相当于 input.trigger('change')，它是 trigger()方法的简写。
                                            为什么我们希望手动触发一个事件呢？如果不这么做，很多时候，我们就得写两份一模一样的代码。
                                    浏览器安全限制
                                            在浏览器中，有些JavaScript代码只有在用户触发下才能执行，例如，window.open()函数：
                                                    // 无法弹出新窗口，将被浏览器屏蔽:
                                                    $(function () {
                                                        window.open('/');
                                                    });
                                                    这些“敏感代码”只能由用户操作来触发：
                                                    var button1 = $('#testPopupButton1');
                                                    var button2 = $('#testPopupButton2');

                                                    function popupTestWindow() {
                                                        window.open('/');
                                                    }

                                                    button1.click(function () {
                                                        popupTestWindow();
                                                    });

                                                    button2.click(function () {
                                                        // 不立刻执行 popupTestWindow()，100毫秒后执行:
                                                        setTimeout(popupTestWindow, 100);
                                                    });
                                            当用户点击button1时，click事件被触发，由于 popupTestWindow() 在click事件处理函数内执行，这是浏览器允许的，
                                            而 button2的click事件并未立刻执行 popupTestWindow()，延迟执行的 popupTestWindow()将被浏览器拦截。

                                    练习
                                            对如下的Form表单：
                                                    <!-- HTML结构 -->
                                                    <form id="test-form" action="test">
                                                        <legend>请选择想要学习的编程语言：</legend>
                                                        <fieldset>
                                                            <p><label class="selectAll"><input type="checkbox"> <span class="selectAll">全选</span><span class="deselectAll">全不选</span></label> <a href="#0" class="invertSelect">反选</a></p>
                                                            <p><label><input type="checkbox" name="lang" value="javascript"> JavaScript</label></p>
                                                            <p><label><input type="checkbox" name="lang" value="python"> Python</label></p>
                                                            <p><label><input type="checkbox" name="lang" value="ruby"> Ruby</label></p>
                                                            <p><label><input type="checkbox" name="lang" value="haskell"> Haskell</label></p>
                                                            <p><label><input type="checkbox" name="lang" value="scheme"> Scheme</label></p>
                                                            <p><button type="submit">Submit</button></p>
                                                        </fieldset>
                                                    </form>
                                            实现功能
                                                    绑定合适的事件处理函数，实现以下逻辑：
                                                    当用户勾上“全选”时，自动选中所有语言，并把“全选”变成“全不选”；
                                                    当用户去掉“全不选”时，自动不选中所有语言；
                                                    当用户点击“反选”时，自动把所有语言状态反转（选中的变为未选，未选的变为选中）；
                                                    当用户把所有语言都手动勾上时，“全选”被自动勾上，并变为“全不选”；
                                                    当用户手动去掉选中至少一种语言时，“全不选”自动被去掉选中，并变为“全选”。
                                            代码
                                                    <script>

                                                    'use strict';


                                                    var
                                                        form = $('#test-form'),
                                                        langs = form.find('[name=lang]'),
                                                        selectAll = form.find('label.selectAll :checkbox'),
                                                        selectAllLabel = form.find('label.selectAll span.selectAll'),
                                                        deselectAllLabel = form.find('label.selectAll span.deselectAll'),
                                                        invertSelect = form.find('a.invertSelect');

                                                    // 重置初始化状态:
                                                    form.find('*').show().off();
                                                    form.find(':checkbox').prop('checked', false).off();
                                                    deselectAllLabel.hide();
                                                    // 拦截form提交事件:
                                                    form.off().submit(function (e) {
                                                        e.preventDefault();
                                                        alert(form.serialize());
                                                    });

                                                    function updateLabel() {
                                                      let allChecked = langs.filter(':checked').length === langs.length

                                                      selectAll.prop('checked', allChecked)
                                                      if (allChecked) {
                                                        selectAllLabel.hide()
                                                        deselectAllLabel.show() 
                                                      } else {
                                                        selectAllLabel.show()
                                                        deselectAllLabel.hide() 
                                                      }
                                                    }

                                                    selectAll.change(function(e) {
                                                      langs.prop('checked', $(this).is(':checked'))
                                                      updateLabel()
                                                    })

                                                    invertSelect.click(function(e) {
                                                      langs.click()
                                                    })

                                                    langs.change(() => updateLabel())

                                                    </script>

            jQuery 实现 动画
                        背景
                                用 JavaScript实现动画，原理非常简单：我们只需要以固定的时间间隔（例如，0.1秒），每次把DOM元素的CSS样式
                                修改一点（例如，高宽各增加10%），看起来就像动画了

                                但是要用JavaScript手动实现动画效果，需要编写非常复杂的代码。如果想要把动画效果用函数封装起来便于复用，那考虑的事情就更多了
                        使用jQuery实现动画，代码已经简单得不能再简化了：只需要一行代码！
                        show / hide -- 从左上角逐渐展开或收缩
                                直接以无参数形式调用 show()和 hide()，会显示和隐藏DOM元素。但是，只要传递一个时间参数进去，就变成了动画：
                                <div id ='test-show-hide'> fdfdddddddd</div>

                                var div = $('#test-show-hide');
                                div.hide(3000); // 在3秒钟内逐渐消失
                                时间以毫秒为单位，但也可以是'slow'，'fast'这些字符串：
                                var div = $('#test-show-hide');
                                div.show('slow'); // 在0.6秒钟内逐渐显示
                                toggle()方法则根据当前状态决定是 show()还是 hide()。
                                效果实测：
                                hide('slow') show('slow') toggle('slow')
                        slideUp / slideDown -- 在垂直方向逐渐展开或收缩
                                你可能已经看出来了，show()和hide()是从左上角逐渐展开或收缩的，而slideUp()和 slideDown()则是在垂直方向逐渐展开或收缩的。
                                slideUp()把一个可见的DOM元素收起来，效果跟拉上窗帘似的，slideDown()相反，而slideToggle()则根据元素是否可见来决定下一步动作：
                                var div = $('#test-slide');
                                div.slideUp(3000); // 在3秒钟内逐渐向上消失
                                效果实测：
                                slideUp('slow') slideDown('slow') slideToggle('slow')
                        fadeIn / fadeOut -- 淡入淡出，通过不断设置DOM元素的opacity属性来实现
                                fadeIn()和 fadeOut()的动画效果是淡入淡出，也就是通过不断设置DOM元素的opacity属性来实现，而 fadeToggle()则
                                根据元素是否可见来决定下一步动作：
                                var div = $('#test-fade');
                                div.fadeOut('slow'); // 在0.6秒内淡出
                                fadeOut('slow') fadeIn('slow') fadeToggle('slow')
                        自定义动画
                                如果上述动画效果还不能满足你的要求，那就祭出最后大招：animate()，它可以实现任意动画效果，我们需要传入的参数就是DOM元素
                                最终的CSS状态和时间，jQuery在时间段内不断调整CSS直到达到我们设定的值：
                                        var div = $('#test-animate');
                                        div.animate({
                                            opacity: 0.25,
                                            width: '256px',
                                            height: '256px'
                                        }, 3000); // 在3秒钟内CSS过渡到设定值
                                animate()还可以再传入一个函数，当动画结束时，该函数将被调用：
                                        var div = $('#test-animate');
                                        div.animate({
                                            opacity: 0.25,
                                            width: '256px',
                                            height: '256px'
                                        }, 3000, function () {
                                            console.log('动画已结束');
                                            // 恢复至初始状态:
                                            $(this).css('opacity', '1.0').css('width', '128px').css('height', '128px');
                                        });
                                实际上这个回调函数参数对于基本动画也是适用的。
                                有了animate()，你就可以实现各种自定义动画效果了
                        串行动画
                                jQuery的动画效果还可以串行执行，通过 delay()方法还可以实现暂停，这样，我们可以实现更复杂的动画效果，而代码却相当简单：
                                        var div = $('#test-animates');
                                        // 动画效果：slideDown - 暂停 - 放大 - 暂停 - 缩小
                                        div.slideDown(2000)
                                           .delay(1000)
                                           .animate({
                                               width: '256px',
                                               height: '256px'
                                           }, 2000)
                                           .delay(1000)
                                           .animate({
                                               width: '128px',
                                               height: '128px'
                                           }, 2000);
                                因为动画需要执行一段时间，所以jQuery必须不断返回新的Promise对象才能后续执行操作。简单地把动画封装在函数中是不够的。
                        为什么有的动画没有效果
                                你可能会遇到，有的动画如slideUp()根本没有效果。这是因为jQuery动画的原理是逐渐改变CSS的值，如height从100px逐渐变为0。
                                但是很多不是block性质的DOM元素，对它们设置height根本就不起作用，所以动画也就没有效果。
                                此外，jQuery也没有实现对background-color的动画效果，用animate()设置background-color也没有效果。这种情况下可以使用
                                CSS3的transition实现动画效果
            jQuery 实现 AJAX
                        用JavaScript写AJAX前面已经介绍过了，主要问题就是不同浏览器需要写不同代码，并且状态和错误处理写起来很麻烦。
                        用jQuery的相关对象来处理AJAX，不但不需要考虑浏览器问题，代码也能大大简化。
                        jQuery在全局对象jQuery（也就是$）绑定了 ajax()函数，可以处理AJAX请求。ajax(url, settings)函数需要接收一个URL和一个可选的settings对象，
                        常用的选项如下：
                                •   async：是否异步执行AJAX请求，默认为true，千万不要指定为false；
                                •   method：发送的Method，缺省为'GET'，可指定为'POST'、'PUT'等；
                                •   contentType：发送POST请求的格式，默认值为'application/x-www-form-urlencoded; charset=UTF-8'，也可以指定为text/plain、application/json；
                                •   data：发送的数据，可以是字符串、数组或object。如果是GET请求，data将被转换成query附加到URL上，如果是POST请求，根据contentType把data序列化成合适的格式；
                                •   headers：发送的额外的HTTP头，必须是一个object；
                                •   dataType：接收的数据格式，可以指定为'html'、'xml'、'json'、'text'等，缺省情况下根据响应的Content-Type猜测。

                        下面的例子发送一个GET请求，并返回一个JSON格式的数据：
                                var jqxhr = $.ajax('/api/categories', {
                                    dataType: 'json'
                                });
                                // 请求已经发送了
                                不过，如何用回调函数处理返回的数据和出错时的响应呢？
                                还记得Promise对象吗？jQuery的jqXHR对象类似一个Promise对象，我们可以用链式写法来处理各种回调：
                                'use strict';

                                function ajaxLog(s) {
                                    var txt = $('#test-response-text');
                                    txt.val(txt.val() + '\n' + s);
                                }

                                $('#test-response-text').val('');

                                var jqxhr = $.ajax('/api/categories',{dataType:'json'})
                                        .done(function (data) {ajaxLog('成功，收到的数据：' + JSON.stringify(data));})
                                        .fail(function (xhr, status) {ajaxLog('失败：' + xhr.status + ', 原因：' + status);})
                                        .always(function () {ajaxLog('请求完成：无论成功或失败都会调用');});

                        get
                                对常用的AJAX操作，jQuery提供了一些辅助方法。由于GET请求最常见，所以jQuery提供了 get()方法，可以这么写：
                                var jqxhr = $.get('/path/to/resource', {
                                    name: 'Bob Lee',
                                    check: 1
                                });
                                第二个参数如果是object，jQuery自动把它变成query string然后加到URL后面，实际的URL是：
                                /path/to/resource?name=Bob%20Lee&check=1
                                这样我们就不用关心如何用URL编码并构造一个query string了。
                        post
                                post()和 get()类似，但是传入的第二个参数默认被序列化为application/x-www-form-urlencoded：
                                var jqxhr = $.post('/path/to/resource', {
                                    name: 'Bob Lee',
                                    check: 1
                                });
                                实际构造的数据name=Bob%20Lee&check=1作为POST的body被发送。
                        getJSON
                                由于JSON用得越来越普遍，所以jQuery也提供了 getJSON() 方法来快速通过GET获取一个JSON对象：
                                var jqxhr = $.getJSON('/path/to/resource', {
                                    name: 'Bob Lee',
                                    check: 1
                                }).done(function (data) {
                                    // data已经被解析为JSON对象了
                                });
                        安全限制
                                jQuery的AJAX完全封装的是JavaScript的AJAX操作，所以它的安全限制和前面讲的用JavaScript写AJAX完全一样。
                                如果需要使用JSONP，可以在ajax()中设置jsonp: 'callback'，让jQuery实现JSONP跨域加载数据。
                                关于跨域的设置请参考浏览器 - AJAX一节中CORS的设置。
            jQuery 扩展 -- 编写jQuery插件
                        背景
                                当我们使用jQuery对象的方法时，由于jQuery对象可以操作一组DOM，而且支持链式操作，所以用起来非常方便。
                                但是jQuery内置的方法永远不可能满足所有的需求。比如，我们想要高亮显示某些DOM元素，用jQuery可以这么实现：
                                $('span.hl').css('backgroundColor', '#fffceb').css('color', '#d85030');

                                $('p a.hl').css('backgroundColor', '#fffceb').css('color', '#d85030');
                                总是写重复代码可不好，万一以后还要修改字体就更麻烦了，能不能统一起来，写个highlight()方法？
                                $('span.hl').highlight();

                                $('p a.hl').highlight();
                                答案是肯定的。我们可以扩展jQuery来实现自定义方法。将来如果要修改高亮的逻辑，只需修改一处扩展代码。
                                这种方式也称为编写jQuery插件。
                        编写jQuery插件
                                    给jQuery对象绑定一个新方法是通过扩展 $.fn 对象实现的。
                                                让我们来编写第一个扩展——highlight1()：
                                                        $.fn.highlight1 = function () {
                                                            // this已绑定为当前jQuery对象:
                                                            this.css('backgroundColor', '#fffceb').css('color', '#d85030');
                                                            return this;
                                                        }
                                                            注意到函数内部的this在调用时被绑定为jQuery对象，所以函数内部代码可以正常调用所有jQuery对象的方法。
                                                                    对于如下的HTML结构：
                                                                    <!-- HTML结构 -->
                                                                    <div id="test-highlight1">
                                                                        <p>什么是<span>jQuery</span></p>
                                                                        <p><span>jQuery</span>是目前最流行的<span>JavaScript</span>库。</p>
                                                                    </div>

                                                                    来测试一下highlight1()的效果：
                                                                    'use strict';
                                                                    $('#test-highlight1 span').highlight1();

                                                            细心的童鞋可能发现了，为什么最后要return this;？因为jQuery对象支持链式操作，我们自己写的扩展方法也要能继续链式下去：
                                                            $('#test-highlight1').highlight1().slideUp(2000);
                                                            不然，用户调用的时候，就不得不把上面的代码拆成两行。
                                                            但是这个版本并不完美。有的用户希望高亮的颜色能自己来指定，怎么办？
                                                我们可以给方法加个参数，让用户自己把参数用对象传进去。于是我们有了第二个版本的 highlight2()：
                                                                代码
                                                                            $.fn.highlight2 = function (options) {
                                                                                // 要考虑到各种情况:
                                                                                // options为undefined
                                                                                // options只有部分key
                                                                                var bgcolor = options && options.backgroundColor || '#fffceb';
                                                                                var color = options && options.color || '#d85030';
                                                                                this.css('backgroundColor', bgcolor).css('color', color);
                                                                                return this;
                                                                            }
                                                                            对于如下HTML结构：
                                                                            <!-- HTML结构 -->
                                                                            <div id="test-highlight2">
                                                                                <p>什么是<span>jQuery</span> <span>Plugin</span></p>
                                                                                <p>编写<span>jQuery</span> <span>Plugin</span>可以用来扩展<span>jQuery</span>的功能。</p>
                                                                            </div>

                                                                来实测一下带参数的 highlight2()：
                                                                            'use strict';
                                                                            $('#test-highlight2 span').highlight2({backgroundColor:'#00a8e6', color: '#ffffff'});
                                                                对于默认值的处理，我们用了一个简单的&&和||短路操作符，总能得到一个有效的值
                                                另一种方法是使用jQuery提供的辅助方法$.extend(target, obj1, obj2, ...)，它把多个object对象的属性合并到第一个target对象中，
                                                    遇到同名属性，总是使用靠后的对象的值，也就是越往后优先级越高：
                                                    // 把默认值和用户传入的options合并到对象 {} 中并返回:
                                                    var opts = $.extend({}, {
                                                        backgroundColor: '#00a8e6',
                                                        color: '#ffffff'
                                                    }, options);
                                                最终版的 highlight() -- 用户自定义缺省值
                                                紧接着用户对 highlight2()提出了意见：每次调用都需要传入自定义的设置，能不能让我自己设定一个缺省值，以后的调用统一使用无参数的 highlight2()？
                                                也就是说，我们设定的默认值应该能允许用户修改。
                                                那默认值放哪比较合适？放全局变量肯定不合适，最佳地点是$.fn.highlight2这个函数对象本身。
                                                于是最终版的highlight()终于诞生了：
                                                        $.fn.highlight = function (options) {
                                                            // 合并默认值和用户设定值:
                                                            var opts = $.extend({}, $.fn.highlight.defaults, options);
                                                            this.css('backgroundColor', opts.backgroundColor).css('color', opts.color);
                                                            return this;
                                                        }

                                                        // 设定默认值:
                                                        $.fn.highlight.defaults = {
                                                            color: '#d85030',
                                                            backgroundColor: '#fff8de'
                                                        }
                                                        这次用户终于满意了。用户使用时，只需一次性设定默认值：
                                                        $.fn.highlight.defaults.color = '#fff';
                                                        $.fn.highlight.defaults.backgroundColor = '#000';
                                                        然后就可以非常简单地调用highlight()了。
                                                对如下的HTML结构：
                                                        <!-- HTML结构 -->
                                                        <div id="test-highlight">
                                                            <p>如何编写<span>jQuery</span> <span>Plugin</span></p>
                                                            <p>编写<span>jQuery</span> <span>Plugin</span>，要设置<span>默认值</span>，并允许用户修改<span>默认值</span>，
                                                            或者运行时传入<span>其他值</span>。</p>
                                                        </div>
                                                实测一下修改默认值的效果：
                                                        'use strict';
                                                        $.fn.highlight.defaults.color = '#659f13';
                                                        $.fn.highlight.defaults.backgroundColor = '#f2fae3';
                                                        $('#test-highlight p:first-child span').highlight();
                                                        $('#test-highlight p:last-child span').highlight({color:'#dd1144'})
                                    最终，我们得出编写一个jQuery插件的原则：
                                1.  给$.fn绑定函数，实现插件的代码逻辑；
                                2.  插件函数最后要return this;以支持链式调用；
                                3.  插件函数要有默认值，绑定在$.fn.<pluginName>.defaults上；
                                4.  用户在调用时可传入设定值以便覆盖默认值。
                                    针对特定元素的扩展
                                            我们知道jQuery对象的有些方法只能作用在特定DOM元素上，比如 submit()方法只能针对form。如果我们编写的扩展只能针对某些类型的
                                            DOM元素，应该怎么写？
                                            还记得jQuery的选择器支持 filter()方法来过滤吗？我们可以借助这个方法来实现针对特定元素的扩展。
                                            举个例子，现在我们要给所有指向外链的超链接加上跳转提示，怎么做？
                                                    先写出用户调用的代码：
                                                    $('#main a').external();
                                                    然后按照上面的方法编写一个external扩展：
                                                                $.fn.external = function () {
                                                                    // return返回的 each()返回结果，支持链式调用:
                                                                    return this.filter('a').each(function () {
                                                                        // 注意: each()内部的回调函数的this绑定为DOM本身!
                                                                        var a = $(this);
                                                                        var url = a.attr('href');
                                                                        if (url && (url.indexOf('http://')===0 || url.indexOf('https://')===0)) {
                                                                            a.attr('href', '#0')
                                                                             .removeAttr('target')
                                                                             .append(' <i class="uk-icon-external-link"></i>')
                                                                             .click(function () {
                                                                                if(confirm('你确定要前往' + url + '？')) {
                                                                                    window.open(url);
                                                                                }
                                                                            });
                                                                        }
                                                                    });
                                                                }
                                                    对如下的HTML结构：
                                                                <!-- HTML结构 -->
                                                                <div id="test-external">
                                                                    <p>如何学习<a href="http://jquery.com">jQuery</a>？</p>
                                                                    <p>首先，你要学习<a href="/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000">JavaScript</a>，
                                                                    并了解基本的<a href="https://developer.mozilla.org/en-US/docs/Web/HTML">HTML</a>。</p>
                                                                </div>
                                                    实测外链效果：
                                                                'use strict';
                                                                $('#test-external a').external();
                                                    代码解读
                                                                <a href="http://example.com/" target="_blank">Example</a>
                                                                .attr('href', '#0')
                                                                ==> <a href="#0" target="_blank">Example</a>
                                                                .removeAttr('target')
                                                                ==> <a href="#0">Example</a>
                                                                .append(' <i class="uk-icon-external-link"></i>')
                                                                ==> <a href="#0">Example <i class="uk-icon-external-link"></i></a>
                                                                1、把href里的链接值为#0，这样用户直接点链接就无法跳转到该地址了。
                                                                2、把target属性删除，因为target="_blank"会新开一个浏览器空白窗口。
                                                                3、加上一个<i>标签，对应的是在链接文字后面加一个提示的图标。
                                                                总体来将就是阻止用户直接点开链接，让其通过确认弹窗来做跳转。
                                                                
                                                                上面的代码中的this为什么能够直接跟Jquery的.filter方法
                                                                            联系上下文：前面还有一段内容呢：
                                                                            先写出用户调用的代码：
                                                                            $('#main a').external();
                                                                            然后按照上面的方法编写一个external扩展：
                                                                            所以，this.filter('a')...中的this，是$('#main a')。

                                                                确实preventDefault这种方法不错
                                                                            $.fn.external = function () {
                                                                                return this.filter('a').each(function () {
                                                                                    var a = $(this);
                                                                                    var url = a.attr('href');
                                                                                    if (url && (url.indexOf('http://') === 0 || url.indexOf('https://') === 0 || url.indexOf('/wiki/') === 0)) {
                                                                                        a.append(' <i class="uk-icon-external-link"></i>').click(function (e) {
                                                                                            e.preventDefault();
                                                                                            if (confirm('确定前往' + url + "页面?")) {
                                                                                                window.open(url)
                                                                                            }
                                                                                        })
                                                                                    }
                                                                                })
                                                                            }
                                                                            $('#test-external a').external();
                                                                我认为链接跳转那里写的不够好
                                                                直接event.preventDefault()阻止默认行为就好了，不用删除这个属性又添加那个属性的
                                                                还有短路操作符，总结一下： 
                                                                            逻辑或（||）：
                                                                            只要第一个值的布尔值为false，那么永远返回第二个值。 逻辑或属于短路操作，第一个值为true时，不再操作第二个值，且返回第一个值。 
                                                                            逻辑与（&&）：
                                                                            只要第一个值的布尔值为true，那么永远返回第二个值。 逻辑与属于短路操作，第一个值为false时，不再操作第二个值，且返回第一个值。
                                    小结
                                            扩展jQuery对象的功能十分简单，但是我们要遵循jQuery的原则，编写的扩展方法能支持链式调用、具备默认值和过滤特定元素，
                                            使得扩展方法看上去和jQuery本身的方法没有什么区别。

            错误处理--错误处理是程序设计时必须要考虑的问题
                        在执行JavaScript代码的时候，有些情况下会发生错误。
                        错误分两种
                                    一种是程序写的逻辑不对，导致代码执行异常。例如：
                                                var s = null;
                                                var len = s.length; // TypeError：null变量没有length属性
                                                对于这种错误，要修复程序。
                                    一种是执行过程中，程序可能遇到无法预测的异常情况而报错
                                                例如，网络连接中断，读取不存在的文件，没有操作权限等。
                                                对于这种错误，我们需要处理它，并可能需要给用户反馈。
                        对于C这样贴近系统底层的语言，错误是通过错误码返回的，用错误码表示错误在编写程序时十分不便
                                    int fd = open("/path/to/file", O_RDONLY);
                                    if (fd == -1) {
                                        printf("Error when open file!");
                                    } else {
                                        // TODO
                                    }
                                    通过错误码返回错误，就需要约定什么是正确的返回值，什么是错误的返回值。上面的open()函数约定返回-1表示错误。
                                    显然，这种用错误码表示错误在编写程序时十分不便。
                        高级语言通常都提供了更抽象的错误处理逻辑 try ... catch ... finally，JavaScript也不例外。
                                    编写的代码如下：
                                                'use strict';
                                                 
                                                var r1, r2, s = null;
                                                try {
                                                    r1 =s.length; // 此处会产生错误
                                                    r2=100; // 该语句不会执行
                                                } catch (e) {
                                                    alert('出错了：' e);
                                                } finally {
                                                    console.log('finally')
                                                }
                                                    console.log('r1 = ' + r1); // r1 应为 undefined
                                                    console.log('r2 = ' + r2); // r2 应为 undefined
                                    弹出的Alert 提示类似“出错了：TypeError: Cannot read property 'length' of null”。
                                    我们来分析一下使用try ... catch ... finally的执行流程。
                                                当代码块被try { ... }包裹的时候，就表示这部分代码执行过程中可能会发生错误，一旦发生错误，就不再继续执行
                                                后续代码，转而跳到catch块。catch (e) { ... }包裹的代码就是错误处理代码，变量e表示捕获到的错误。最后，无论
                                                有没有错误，finally一定会被执行。
                                                所以，有错误发生时，执行流程像这样：
                                                            1.  先执行try { ... }的代码；
                                                            2.  执行到出错的语句时，后续语句不再继续执行，转而执行 catch (e) { ... }代码；
                                                            3.  最后执行finally { ... }代码。
                                                而没有错误发生时，执行流程像这样：
                                                            1.  先执行try { ... }的代码；
                                                            2.  因为没有出错，catch (e) { ... }代码不会被执行；
                                                            3.  最后执行finally { ... }代码。
                                    最后请注意，catch和finally可以不必都出现。也就是说，try语句一共有三种形式：
                                                完整的try ... catch ... finally：
                                                            try {
                                                                ...
                                                            } catch (e) {
                                                                ...
                                                            } finally {
                                                                ...
                                                            }
                                                只有try ... catch，没有finally：
                                                            try {
                                                                ...
                                                            } catch (e) {
                                                                ...
                                                            }
                                                只有try ... finally，没有catch：
                                                            try {
                                                                ...
                                                            } finally {
                                                                ...
                                                            }
                        错误类型
                                    JavaScript有一个标准的Error对象表示错误，还有从Error派生的TypeError、ReferenceError等错误对象。我们在处理错误时，可以通过
                                    catch(e)捕获的 变量e 访问错误对象：
                                                try {
                                                    ...
                                                } catch (e) {
                                                    if (e instanceof TypeError) {
                                                        alert('Type error!');
                                                    } else if (e instanceof Error) {
                                                        alert(e.message);
                                                    } else {
                                                        alert('Error: ' + e);
                                                    }
                                                }
                                    使用变量e是一个习惯用法，也可以以其他变量名命名，如catch(ex)。
                        抛出错误
                                    程序也可以主动抛出一个错误，让执行流程直接跳转到catch块。抛出错误使用throw语句。
                                    例如，下面的代码让用户输入一个数字，程序接收到的实际上是一个字符串，然后用 parseInt()转换为整数。当用户输入
                                    不合法的时候，我们就抛出错误
                                                'use strict';
                                                var r, n, s;
                                                try {
                                                    s=prompt('请输入一个数字');
                                                    n = parseInt(s);
                                                    if (isNaN(n)) {
                                                        throw new Error('输入错误');
                                                    }
                                                    // 计算平方：
                                                    r = n*n;
                                                    alert(n+'*' + n + '=' + r);
                                                } catch (e) {alert('出错了：' + e);}

                                    实际上，JavaScript允许抛出任意对象，包括数字、字符串。但是，最好还是抛出一个Error对象。
                                    最后，当我们用catch捕获错误时，一定要编写错误处理语句：
                                                var n = 0, s;
                                                try {
                                                    n = s.length;
                                                } catch (e) {
                                                    console.log(e);
                                                }
                                                console.log(n);
                                    哪怕仅仅把错误打印出来，也不要什么也不干：
                                                var n = 0, s;
                                                try {
                                                    n = s.length;
                                                } catch (e) {
                                                }
                                                console.log(n);
                                    因为catch到错误却什么都不执行，就不知道程序执行过程中到底有没有发生错误。
                                    处理错误时，请不要简单粗暴地用alert()把错误显示给用户。教程的代码使用alert()是为了便于演示。
            错误传播
                        如果代码发生了错误，又没有被try ... catch捕获，那么，程序执行流程会跳转到哪呢？
                                    function getLength(s) {
                                        return s.length;
                                    }

                                    function printLength() {
                                        console.log(getLength('abc')); // 3
                                        console.log(getLength(null)); // Error!
                                    }

                                    printLength();
                        如果在一个函数内部发生了错误，它自身没有捕获，错误就会被抛到外层调用函数，如果外层函数也没有捕获，该错误会一直
                        沿着函数调用链向上抛出，直到被JavaScript引擎捕获，代码终止执行。
                        所以，我们不必在每一个函数内部捕获错误，只需要在合适的地方来个统一捕获，一网打尽
                                    e.g.
                                                'use strict'
                                                function main (s) {
                                                    console.log('BEGIN main()');
                                                    try {
                                                        foo(s);
                                                    } catch (e) {
                                                        alert('出错了：' + e);
                                                    }
                                                    console.log('END main()');
                                                }
                                                function foo(s) {
                                                    console.log('BEGIN foo()');
                                                    bar(s);
                                                    console.log('END foo()');
                                                }
                                                function bar(s) {
                                                    console.log('BEGIN bar()');
                                                    console.log('length = ' + s.length);
                                                    console.log('END bar()');
                                                }
                                                main(null);
                                    代码解读
                                                当bar()函数传入参数null时，代码会报错，错误会向上抛给调用方foo()函数，foo()函数没有try ... catch语句，
                                                所以错误继续向上抛给调用方main()函数，main()函数有try ... catch语句，所以错误最终在main()函数被处理了。
                                                至于在哪些地方捕获错误比较合适，需要视情况而定。
            异步错误处理
                        编写JavaScript代码时，我们要时刻牢记，JavaScript引擎是一个事件驱动的执行引擎，代码总是以单线程执行，而回调函数的执行
                        需要等到下一个满足条件的事件出现后，才会被执行。
                        例如，setTimeout()函数可以传入回调函数，并在指定若干毫秒后执行：
                                    function printTime() {
                                        console.log('It is time!');
                                    }

                                    setTimeout(printTime, 1000);
                                    console.log('done');
                        上面的代码会先打印done，1秒后才会打印It is time!。
                        如果printTime()函数内部发生了错误，我们试图用try包裹setTimeout()是无效的
                                    'use strict';
                                    function printTime() {
                                        throw new Error();
                                    }
                                    try {
                                        setTimeout(printTime, 1000);
                                        console.log('done');
                                    } catch (e) {
                                        alert('error');
                                    }
                                    // 直接运行，看是否会 alert
                        原因就在于调用setTimeout()函数时，传入的printTime函数并未立刻执行！紧接着，JavaScript引擎会继续执行console.log('done');
                        语句，而此时并没有错误发生。直到1秒钟后，执行printTime函数时才发生错误，但此时除了在printTime函数内部捕获错误外，
                        外层代码并无法捕获。
                        所以，涉及到异步代码，无法在调用时捕获，原因就是在捕获的当时，回调函数并未执行。
                        类似的，当我们处理一个事件时，在绑定事件的代码处，无法捕获事件处理函数的错误。
                        例如，针对以下的表单：
                                    <form>
                                        <input id="x"> + <input id="y">
                                        <button id="calc" type="button">计算</button>
                                    </form>

                                    'use strict';
                                    var $btn = $('#calc');
                                    // 取消已绑定的事件:
                                    $btn.off('click');

                                    try {
                                        $btn.click(function () {
                                            var
                                                x=parseFloat($('#x').val()),
                                                y=parseFloat($('#y').val()),
                                                r;
                                            if (isNaN(x) || isNaN(y) {
                                                throw new Error('输入有误');
                                                };)
                                            r=x+y;
                                            alert('计算结果: ' + r);
                                            });
                                    } catch (s) {
                                        alert('输入有误！');
                                    }
                        但是，用户输入错误时，处理函数并未捕获到错误。请修复错误处理代码。

            underscore -- 第三方开源库
                        前面我们已经讲过了，JavaScript是函数式编程语言，支持高阶函数和闭包。函数式编程非常强大，
                                    可以写出非常简洁的代码。例如Array的map()和filter()方法：
                                    'use strict';
                                    var a1 = [1, 4, 9, 16];
                                    var a2 = a1.map(Math.sqrt); // [1, 2, 3, 4]
                                    var a3 = a2.filter((x) => { return x % 2 === 0; }); // [2, 4]
                                    现在问题来了，Array有map()和filter()方法，可是Object没有这些方法。此外，低版本的浏览器例如
                                    IE6～8也没有这些方法，怎么办？
                                    方法一，自己把这些方法添加到Array.prototype中，然后给Object.prototype也加上mapObject()等
                                    类似的方法。
                                    方法二，直接找一个成熟可靠的第三方开源库，使用统一的函数来实现map()、filter()这些操作。
                                    我们采用方法二，选择的第三方库就是underscore。
                                    正如jQuery统一了不同浏览器之间的DOM操作的差异，让我们可以简单地对DOM进行操作，underscore
                                    则提供了一套完善的函数式编程的接口，让我们更方便地在JavaScript中实现函数式编程。
                                    jQuery在加载时，会把自身绑定到唯一的全局变量$上，underscore与其类似，会把自身绑定到唯一的
                                    全局变量_上，这也是为啥它的名字叫underscore的原因。
                                    用underscore实现map()操作如下：
                                    'use strict';
                                    _.map([1, 2, 3], (x) => x * x); // [1, 4, 9]
                                    咋一看比直接用Array.map()要麻烦一点，可是underscore的map()还可以作用于Object：
                                    'use strict';
                                    _.map({ a: 1, b: 2, c: 3 }, (v, k) => k + '=' + v); // ['a=1', 'b=2', 'c=3']
                                    后面我们会详细介绍underscore提供了一系列函数式接口。

                        underscore为集合类对象提供了一致的接口。集合类是指Array和Object，暂不支持Map和Set。
                                    map/filter
                                    和Array的map()与filter()类似，但是underscore的map()和filter()可以作用于Object。当作用于Object时，传入的函数为function (value, key)，第一个参数接收value，第二个参数接收key：
                                    'use strict';

                                    var obj = {
                                        name: 'bob',
                                        school: 'No.1 middle school',
                                        address: 'xueyuan road'
                                    };
                                     
                                    alert(JSON.stringify(upper));
                                     Run
                                    你也许会想，为啥对Object作map()操作的返回结果是Array？应该是Object才合理啊！把_.map换成
                                    _.mapObject再试试。
                                    every / some
                                    当集合的所有元素都满足条件时，_.every()函数返回true，当集合的至少一个元素满足条件时，_.some()
                                    数返回true：
                                    'use strict';
                                    // 所有元素都大于0？
                                    _.every([1, 4, 7, -3, -9], (x) => x > 0); // false
                                    // 至少一个元素大于0？
                                    _.some([1, 4, 7, -3, -9], (x) => x > 0); // true
                                    当集合是Object时，我们可以同时获得value和key：
                                    'use strict';
                                    var obj = {
                                        name: 'bob',
                                        school: 'No.1 middle school',
                                        address: 'xueyuan road'
                                    };
                                    // 判断key和value是否全部是小写：
                                     
                                    alert('every key-value are lowercase: ' + r1 + '\nsome key-value are lowercase: ' + r2);
                                     Run
                                    max / min
                                    这两个函数直接返回集合中最大和最小的数：
                                    'use strict';
                                    var arr = [3, 5, 7, 9];
                                    _.max(arr); // 9
                                    _.min(arr); // 3

                                    // 空集合会返回-Infinity和Infinity，所以要先判断集合不为空：
                                    _.max([])
                                    -Infinity
                                    _.min([])
                                    Infinity
                                    注意，如果集合是Object，max()和min()只作用于value，忽略掉key：
                                    'use strict';
                                    _.max({ a: 1, b: 2, c: 3 }); // 3
                                    groupBy
                                    groupBy()把集合的元素按照key归类，key由传入的函数返回：
                                    'use strict';

                                    var scores = [20, 81, 75, 40, 91, 59, 77, 66, 72, 88, 99];
                                    var groups = _.groupBy(scores, function (x) {
                                        if (x < 60) {
                                            return 'C';
                                        } else if (x < 80) {
                                            return 'B';
                                        } else {
                                            return 'A';
                                        }
                                    });
                                    // 结果:
                                    // {
                                    //   A: [81, 91, 88, 99],
                                    //   B: [75, 77, 66, 72],
                                    //   C: [20, 40, 59]
                                    // }
                                    可见groupBy()用来分组是非常方便的。
                                    shuffle / sample
                                    shuffle()用洗牌算法随机打乱一个集合：
                                    'use strict';
                                    // 注意每次结果都不一样：
                                    _.shuffle([1, 2, 3, 4, 5, 6]); // [3, 5, 4, 6, 2, 1]
                                    sample()则是随机选择一个或多个元素：
                                    'use strict';
                                    // 注意每次结果都不一样：
                                    // 随机选1个：
                                    _.sample([1, 2, 3, 4, 5, 6]); // 2
                                    // 随机选3个：
                                    _.sample([1, 2, 3, 4, 5, 6], 3); // [6, 1, 4]
                                    更多完整的函数请参考underscore的文档：http://underscorejs.org/#collections

                        underscore为Array提供了许多工具类方法，可以更方便快捷地操作Array。
                                    first / last
                                    顾名思义，这两个函数分别取第一个和最后一个元素：
                                    'use strict';
                                    var arr = [2, 4, 6, 8];
                                    _.first(arr); // 2
                                    _.last(arr); // 8
                                    flatten
                                    flatten()接收一个Array，无论这个Array里面嵌套了多少个Array，flatten()最后都把它们变成
                                    一个一维数组：
                                    'use strict';

                                    _.flatten([1, [2], [3, [[4], [5]]]]); // [1, 2, 3, 4, 5]
                                    zip / unzip
                                    zip()把两个或多个数组的所有元素按索引对齐，然后按索引合并成新数组。例如，你有一个
                                    Array保存了名字，另一个Array保存了分数，现在，要把名字和分数给对上，用zip()轻松实现：
                                    'use strict';

                                    var names = ['Adam', 'Lisa', 'Bart'];
                                    var scores = [85, 92, 59];
                                    _.zip(names, scores);
                                    // [['Adam', 85], ['Lisa', 92], ['Bart', 59]]
                                    unzip()则是反过来：
                                    'use strict';
                                    var namesAndScores = [['Adam', 85], ['Lisa', 92], ['Bart', 59]];
                                    _.unzip(namesAndScores);
                                    // [['Adam', 'Lisa', 'Bart'], [85, 92, 59]]
                                    object
                                    有时候你会想，与其用zip()，为啥不把名字和分数直接对应成Object呢？别急，object()
                                    函数就是干这个的：
                                    'use strict';

                                    var names = ['Adam', 'Lisa', 'Bart'];
                                    var scores = [85, 92, 59];
                                    _.object(names, scores);
                                    // {Adam: 85, Lisa: 92, Bart: 59}
                                    注意_.object()是一个函数，不是JavaScript的Object对象。
                                    range
                                    range()让你快速生成一个序列，不再需要用for循环实现了：
                                    'use strict';

                                    // 从0开始小于10:
                                    _.range(10); // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

                                    // 从1开始小于11：
                                    _.range(1, 11); // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

                                    // 从0开始小于30，步长5:
                                    _.range(0, 30, 5); // [0, 5, 10, 15, 20, 25]

                                    // 从0开始大于-10，步长-1:
                                    _.range(0, -10, -1); // [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
                                    更多完整的函数请参考underscore的文档：http://underscorejs.org/#arrays

                        因为underscore本来就是为了充分发挥JavaScript的函数式编程特性，所以也提供了大量JavaScript本身没有的高阶函数。
                                    bind
                                    bind()有什么用？我们先看一个常见的错误用法：
                                    'use strict';

                                    console.log('Hello, world!');
                                    // 输出'Hello, world!'

                                    var log = console.log;
                                    log('Hello, world!');
                                    // Uncaught TypeError: Illegal invocation
                                    如果你想用log()取代console.log()，按照上面的做法是不行的，因为直接调用log()传入的this指针是undefined，必须这么用：
                                    'use strict';

                                    var log = console.log;
                                    // 调用call并传入console对象作为this:
                                    log.call(console, 'Hello, world!')
                                    // 输出Hello, world!
                                    这样搞多麻烦！还不如直接用console.log()。但是，bind()可以帮我们把console对象直接绑定在log()的this指针上，以后调用log()就可以直接正常调用了：
                                    'use strict';

                                    var log = _.bind(console.log, console);
                                    log('Hello, world!');
                                    // 输出Hello, world!
                                    partial
                                    partial()就是为一个函数创建偏函数。偏函数是什么东东？看例子：
                                    假设我们要计算xy，这时只需要调用Math.pow(x, y)就可以了。
                                    假设我们经常计算2y，每次都写Math.pow(2, y)就比较麻烦，如果创建一个新的函数能直接这样写pow2N(y)就好了，这个新函数pow2N(y)就是根据Math.pow(x, y)创建出来的偏函数，它固定住了原函数的第一个参数（始终为2）：
                                    'use strict';

                                    var pow2N = _.partial(Math.pow, 2);
                                    pow2N(3); // 8
                                    pow2N(5); // 32
                                    pow2N(10); // 1024
                                    如果我们不想固定第一个参数，想固定第二个参数怎么办？比如，希望创建一个偏函数cube(x)，计算x3，可以用_作占位符，固定住第二个参数：
                                    'use strict';

                                    var cube = _.partial(Math.pow, _, 3);
                                    cube(3); // 27
                                    cube(5); // 125
                                    cube(10); // 1000
                                    可见，创建偏函数的目的是将原函数的某些参数固定住，可以降低新函数调用的难度。
                                    memoize
                                    如果一个函数调用开销很大，我们就可能希望能把结果缓存下来，以便后续调用时直接获得结果。举个例子，计算阶乘就比较耗时：
                                    'use strict';

                                    function factorial(n) {
                                        console.log('start calculate ' + n + '!...');
                                        var s = 1, i = n;
                                        while (i > 1) {
                                            s = s * i;
                                            i --;
                                        }
                                        console.log(n + '! = ' + s);
                                        return s;
                                    }

                                    factorial(10); // 3628800
                                    // 注意控制台输出:
                                    // start calculate 10!...
                                    // 10! = 3628800
                                    用memoize()就可以自动缓存函数计算的结果：
                                    'use strict';

                                    var factorial = _.memoize(function(n) {
                                        console.log('start calculate ' + n + '!...');
                                        var s = 1, i = n;
                                        while (i > 1) {
                                            s = s * i;
                                            i --;
                                        }
                                        console.log(n + '! = ' + s);
                                        return s;
                                    });

                                    // 第一次调用:
                                    factorial(10); // 3628800
                                    // 注意控制台输出:
                                    // start calculate 10!...
                                    // 10! = 3628800

                                    // 第二次调用:
                                    factorial(10); // 3628800
                                    // 控制台没有输出
                                    对于相同的调用，比如连续两次调用factorial(10)，第二次调用并没有计算，而是直接返回上次计算后缓存的结果。不过，当你计算factorial(9)的时候，仍然会重新计算。
                                    可以对factorial()进行改进，让其递归调用：
                                    'use strict';

                                    var factorial = _.memoize(function(n) {
                                        console.log('start calculate ' + n + '!...');
                                        if (n < 2) {
                                            return 1;
                                        }
                                        return n * factorial(n - 1);
                                    });

                                    factorial(10); // 3628800
                                    // 输出结果说明factorial(1)~factorial(10)都已经缓存了:
                                    // start calculate 10!...
                                    // start calculate 9!...
                                    // start calculate 8!...
                                    // start calculate 7!...
                                    // start calculate 6!...
                                    // start calculate 5!...
                                    // start calculate 4!...
                                    // start calculate 3!...
                                    // start calculate 2!...
                                    // start calculate 1!...

                                    factorial(9); // 362880
                                    // console无输出
                                    once
                                    顾名思义，once()保证某个函数执行且仅执行一次。如果你有一个方法叫register()，用户在页面上点两个按钮的任何一个都可以执行的话，就可以用once()保证函数仅调用一次，无论用户点击多少次：
                                    'use strict';
                                     
                                    // 测试效果:
                                    register();
                                    register();
                                    register();
                                     Run
                                    delay
                                    delay()可以让一个函数延迟执行，效果和setTimeout()是一样的，但是代码明显简单了：
                                    'use strict';

                                    // 2秒后调用alert():
                                    _.delay(alert, 2000);
                                    如果要延迟调用的函数有参数，把参数也传进去：
                                    'use strict';

                                    var log = _.bind(console.log, console);
                                    _.delay(log, 2000, 'Hello,', 'world!');
                                    // 2秒后打印'Hello, world!':
                                    更多完整的函数请参考underscore的文档：http://underscorejs.org/#functions

                        和Array类似，underscore也提供了大量针对Object的函数。
                                    keys / allKeys
                                    keys()可以非常方便地返回一个object自身所有的key，但不包含从原型链继承下来的：
                                    'use strict';

                                    function Student(name, age) {
                                        this.name = name;
                                        this.age = age;
                                    }

                                    var xiaoming = new Student('小明', 20);
                                    _.keys(xiaoming); // ['name', 'age']
                                    allKeys()除了object自身的key，还包含从原型链继承下来的：
                                    'use strict';

                                    function Student(name, age) {
                                        this.name = name;
                                        this.age = age;
                                    }
                                    Student.prototype.school = 'No.1 Middle School';
                                    var xiaoming = new Student('小明', 20);
                                    _.allKeys(xiaoming); // ['name', 'age', 'school']
                                    values
                                    和keys()类似，values()返回object自身但不包含原型链继承的所有值：
                                    'use strict';

                                    var obj = {
                                        name: '小明',
                                        age: 20
                                    };

                                    _.values(obj); // ['小明', 20]
                                    注意，没有allValues()，原因我也不知道。
                                    mapObject
                                    mapObject()就是针对object的map版本：
                                    'use strict';

                                    var obj = { a: 1, b: 2, c: 3 };
                                    // 注意传入的函数签名，value在前，key在后:
                                    _.mapObject(obj, (v, k) => 100 + v); // { a: 101, b: 102, c: 103 }
                                    invert
                                    invert()把object的每个key-value来个交换，key变成value，value变成key：
                                    'use strict';

                                    var obj = {
                                        Adam: 90,
                                        Lisa: 85,
                                        Bart: 59
                                    };
                                    _.invert(obj); // { '59': 'Bart', '85': 'Lisa', '90': 'Adam' }
                                    extend / extendOwn
                                    extend()把多个object的key-value合并到第一个object并返回：
                                    'use strict';

                                    var a = {name: 'Bob', age: 20};
                                    _.extend(a, {age: 15}, {age: 88, city: 'Beijing'}); // {name: 'Bob', age: 88, city: 'Beijing'}
                                    // 变量a的内容也改变了：
                                    a; // {name: 'Bob', age: 88, city: 'Beijing'}
                                    注意：如果有相同的key，后面的object的value将覆盖前面的object的value。
                                    extendOwn()和extend()类似，但获取属性时忽略从原型链继承下来的属性。
                                    clone
                                    如果我们要复制一个object对象，就可以用clone()方法，它会把原有对象的所有属性都复制到新的对象中：
                                    'use strict';
                                    var source = {
                                        name: '小明',
                                        age: 20,
                                        skills: ['JavaScript', 'CSS', 'HTML']
                                    };
                                     
                                    alert(JSON.stringify(copied, null, '  '));
                                     Run
                                    注意，clone()是“浅复制”。所谓“浅复制”就是说，两个对象相同的key所引用的value其实是同一对象：
                                    source.skills === copied.skills; // true
                                    也就是说，修改source.skills会影响copied.skills。
                                    isEqual
                                    isEqual()对两个object进行深度比较，如果内容完全相同，则返回true：
                                    'use strict';

                                    var o1 = { name: 'Bob', skills: { Java: 90, JavaScript: 99 }};
                                    var o2 = { name: 'Bob', skills: { JavaScript: 99, Java: 90 }};

                                    o1 === o2; // false
                                    _.isEqual(o1, o2); // true
                                    isEqual()其实对Array也可以比较：
                                    'use strict';

                                    var o1 = ['Bob', { skills: ['Java', 'JavaScript'] }];
                                    var o2 = ['Bob', { skills: ['Java', 'JavaScript'] }];

                                    o1 === o2; // false
                                    _.isEqual(o1, o2); // true
                                    更多完整的函数请参考underscore的文档：http://underscorejs.org/#objects

                        还记得jQuery支持链式调用吗？
                                    $('a').attr('target', '_blank')
                                          .append(' <i class="uk-icon-external-link"></i>')
                                          .click(function () {});
                                    如果我们有一组操作，用underscore提供的函数，写出来像这样：
                                    _.filter(_.map([1, 4, 9, 16, 25], Math.sqrt), x => x % 2 === 1);
                                    // [1, 3, 5]
                                    能不能写成链式调用？
                                    能！
                                    underscore提供了把对象包装成能进行链式调用的方法，就是chain()函数：
                                    _.chain([1, 4, 9, 16, 25])
                                     .map(Math.sqrt)
                                     .filter(x => x % 2 === 1)
                                     .value();
                                    // [1, 3, 5]
                                    因为每一步返回的都是包装对象，所以最后一步的结果需要调用value()获得最终结果。
                                    小结
                                    通过学习underscore，是不是对JavaScript的函数式编程又有了进一步的认识？

            Node.js -- JavaScript的后端开发
                        安装
                                    从本章开始，我们就正式开启JavaScript的后端开发之旅。
                                                •   Node.js是目前非常火热的技术，但是它的诞生经历却很奇特。
                                                •   众所周知，在Netscape设计出JavaScript后的短短几个月，JavaScript事实上已经是前端开发的唯一标准。
                                                •   后来，微软通过IE击败了Netscape后一统桌面，结果几年时间，浏览器毫无进步。（2001年推出的古老的IE 6到今天仍然有人在使用！）
                                                •   没有竞争就没有发展。微软认为IE6浏览器已经非常完善，几乎没有可改进之处，然后解散了IE6开发团队！而Google却认为支持现代
                                                Web应用的新一代浏览器才刚刚起步，尤其是浏览器负责运行JavaScript的引擎性能还可提升10倍。
                                                •   先是Mozilla借助已壮烈牺牲的Netscape遗产在2002年推出了Firefox浏览器，紧接着Apple于2003年在开源的KHTML浏览器的基础上
                                                推出了WebKit内核的Safari浏览器，不过仅限于Mac平台。
                                                •   随后，Google也开始创建自家的浏览器。他们也看中了WebKit内核，于是基于WebKit内核推出了Chrome浏览器。
                                                •   Chrome浏览器是跨Windows和Mac平台的，并且，Google认为要运行现代Web应用，浏览器必须有一个性能非常强劲的JavaScript引擎，
                                                于是Google自己开发了一个高性能JavaScript引擎，名字叫V8，以BSD许可证开源。
                                                •   现代浏览器大战让微软的IE浏览器远远地落后了，因为他们解散了最有经验、战斗力最强的浏览器团队！回过头再追赶却发现，支持HTML5
                                                的WebKit已经成为手机端的标准了，IE浏览器从此与主流移动端设备绝缘。
                                                •   浏览器大战和Node有何关系？
                                                •   话说有个叫Ryan Dahl的歪果仁，他的工作是用C/C++写高性能Web服务。对于高性能，异步IO、事件驱动是基本原则，但是用C/C++写
                                                就太痛苦了。于是这位仁兄开始设想用高级语言开发Web服务。他评估了很多种高级语言，发现很多语言虽然同时提供了同步IO和异步IO，
                                                但是开发人员一旦用了同步IO，他们就再也懒得写异步IO了，所以，最终，Ryan瞄向了JavaScript。
                                                •   因为JavaScript是单线程执行，根本不能进行同步IO操作，所以，JavaScript的这一“缺陷”导致了它只能使用异步IO。
                                                •   选定了开发语言，还要有运行时引擎。这位仁兄曾考虑过自己写一个，不过明智地放弃了，因为V8就是开源的JavaScript引擎。让Google
                                                投资去优化V8，咱只负责改造一下拿来用，还不用付钱，这个买卖很划算。
                                                •   于是在2009年，Ryan正式推出了基于JavaScript语言和V8引擎的开源Web服务器项目，命名为Node.js。虽然名字很土，但是，Node第一次
                                                把JavaScript带入到后端服务器开发，加上世界上已经有无数的JavaScript开发人员，所以Node一下子就火了起来。
                                                •   在Node上运行的JavaScript相比其他后端开发语言有何优势？
                                                •   最大的优势是借助JavaScript天生的事件驱动机制加V8高性能引擎，使编写高性能Web服务轻而易举。
                                                •   其次，JavaScript语言本身是完善的函数式语言，在前端开发时，开发人员往往写得比较随意，让人感觉JavaScript就是个“玩具语言”。但是，
                                                在Node环境下，通过模块化的JavaScript代码，加上函数式编程，并且无需考虑浏览器兼容性问题，直接使用最新的ECMAScript 6标准，可以完全
                                                满足工程上的需求。
                                                •   我还听说过io.js，这又是什么鬼？
                                                •   因为Node.js是开源项目，虽然由社区推动，但幕后一直由Joyent公司资助。由于一群开发者对Joyent公司的策略不满，于2014年从Node.js项目
                                                fork出了io.js项目，决定单独发展，但两者实际上是兼容的。
                                                •   然而中国有句古话，叫做“分久必合，合久必分”。分家后没多久，Joyent公司表示要和解，于是，io.js项目又决定回归Node.js。
                                                •   具体做法是将来io.js将首先添加新的特性，如果大家测试用得爽，就把新特性加入Node.js。io.js是“尝鲜版”，而Node.js是线上稳定版，相当于
                                                Fedora Linux和RHEL的关系。
                                                •   本章教程的所有代码都在Node.js上调试通过。如果你要尝试io.js也是可以的，不过两者如果遇到一些区别请自行查看io.js的文档。
                                    安装Node.js和npm
                                                安装Node.js -- 由于Node.js平台是在后端运行JavaScript代码，所以，必须首先在本机安装Node环境
                                                            •   目前Node.js的最新版本是6.2.x。首先，从Node.js官网下载对应平台的安装程序，网速慢的童鞋请移步国内镜像。
                                                            •   在Windows上安装时务必选择全部组件，包括勾选Add to Path。
                                                            •   安装完成后，在Windows环境下，请打开命令提示符，然后输入node -v，如果安装正常，你应该看到v6.2.0这样的输出：
                                                            •   C:\Users\IEUser>node -v
                                                            •   v6.2.0
                                                            •   继续在命令提示符输入node，此刻你将进入Node.js的交互环境。在交互环境下，你可以输入任意JavaScript语句，例如 100+200，回车后将得到输出结果。
                                                            •   要退出Node.js环境，连按两次Ctrl+C。
                                                            •   在Mac或Linux环境下，请打开终端，然后输入node -v，你应该看到如下输出：
                                                            •   $ node -v
                                                            •   v6.2.0
                                                            •   如果版本号不是v6.2.x，说明Node.js版本不对，后面章节的代码不保证能正常运行，请重新安装最新版本。
                                                            •   npm
                                                npm -- Node.js的包管理工具（package manager）
                                                            •   在正式开始Node.js学习之前，我们先认识一下npm
                                                            •   npm是什么东东？npm其实是Node.js的包管理工具（package manager）。
                                                            •   为啥我们需要一个包管理工具呢？因为我们在Node.js上开发时，会用到很多别人写的JavaScript代码。如果我们要使用别人写的某个包，
                                                            每次都根据名称搜索一下官方网站，下载代码，解压，再使用，非常繁琐。于是一个集中管理的工具应运而生：大家都把自己开发的模块打包
                                                            后放到npm官网上，如果要使用，直接通过npm安装就可以直接用，不用管代码存在哪，应该从哪下载。
                                                            •   更重要的是，如果我们要使用模块A，而模块A又依赖于模块B，模块B又依赖于模块X和模块Y，npm可以根据依赖关系，把所有依赖的包都
                                                            下载下来并管理起来。否则，靠我们自己手动管理，肯定既麻烦又容易出错。
                                                            •   讲了这么多，npm究竟在哪？
                                                            •   其实npm已经在Node.js安装的时候顺带装好了。我们在命令提示符或者终端输入npm -v，应该看到类似的输出：
                                                            •   C:\>npm -v
                                                            •   3.8.9
                                                            •   如果直接输入npm，你会看到类似下面的输出：
                                                            •   C:\> npm
                                                            •   
                                                            •   Usage: npm <command>
                                                            •   
                                                            •   where <command> is one of:
                                                            •       ...
                                                            •   上面的一大堆文字告诉你，npm需要跟上命令。现在我们不用关心这些命令，后面会一一讲到。目前，你只需要确保npm正确安装了，能运行就行。
                                                小结 -- 请在本机安装Node.js环境，并确保node和npm能正常运行。
                        第一个Node程序
                                    文本编辑器
                                                在前面的所有章节中，我们编写的JavaScript代码都是在浏览器中运行的，因此，我们可以直接在浏览器中敲代码，然后直接运行。
                                                从本章开始，我们编写的JavaScript代码将不能在浏览器环境中执行了，而是在Node环境中执行，因此，JavaScript代码将直接在
                                                你的计算机上以命令行的方式运行，所以，我们要先选择一个文本编辑器来编写JavaScript代码，并且把它保存到本地硬盘的某个
                                                目录，才能够执行。
                                                那么问题来了：文本编辑器到底哪家强？
                                                首先，请注意，绝对不能用Word和写字板。Word和写字板保存的不是纯文本文件。如果我们要用记事本来编写JavaScript代码，
                                                要务必注意，记事本以UTF-8格式保存文件时，会自作聪明地在文件开始的地方加上几个特殊字符（UTF-8 BOM），结果经常会
                                                导致程序运行出现莫名其妙的错误。
                                                所以，用记事本写代码时请注意，保存文件时使用ANSI编码，并且暂时不要输入中文。
                                                如果你的电脑上已经安装了Sublime Text，或者Notepad++，也可以用来编写JavaScript代码，注意用UTF-8格式保存。
                                                输入以下代码：
                                                'use strict';

                                                console.log('Hello, world.');
                                                第一行总是写上'use strict';是因为我们总是以严格模式运行JavaScript代码，避免各种潜在陷阱。
                                                然后，选择一个目录，例如C:\Workspace，把文件保存为hello.js，就可以打开命令行窗口，把当前目录切换到hello.js所在目录，
                                                然后输入以下命令运行这个程序了：
                                                C:\Workspace>node hello.js
                                                Hello, world.
                                                也可以保存为别的名字，比如first.js，但是必须要以.js结尾。此外，文件名只能是英文字母、数字和下划线的组合。
                                                如果当前目录下没有hello.js这个文件，运行node hello.js就会报错：
                                                C:\Workspace>node hello.js
                                                module.js:338
                                                    throw err;
                                                          ^
                                                Error: Cannot find module 'C:\Workspace\hello.js'
                                                    at Function.Module._resolveFilename
                                                    at Function.Module._load
                                                    at Function.Module.runMain
                                                    at startup
                                                    at node.js
                                                报错的意思就是，没有找到hello.js这个文件，因为文件不存在。这个时候，就要检查一下当前目录下是否有这个文件了。
                                    命令行模式和Node交互模式
                                                请注意区分命令行模式和Node交互模式。
                                                看到类似C:\>是在Windows提供的命令行模式：
                                                 
                                                在命令行模式下，可以执行node进入Node交互式环境，也可以执行node hello.js运行一个.js文件。
                                                看到>是在Node交互式环境下：
                                                 
                                                在Node交互式环境下，我们可以输入JavaScript代码并立刻执行。
                                                此外，在命令行模式运行.js文件和在Node交互式环境下直接运行JavaScript代码有所不同。Node交互式环境会把每一行
                                                JavaScript代码的结果自动打印出来，但是，直接运行JavaScript文件却不会。
                                                例如，在Node交互式环境下，输入：
                                                > 100 + 200 + 300;
                                                600
                                                直接可以看到结果600。
                                                但是，写一个calc.js的文件，内容如下：
                                                100 + 200 + 300;
                                                然后在命令行模式下执行：
                                                C:\Workspace>node calc.js
                                                发现什么输出都没有。
                                                这是正常的。想要输出结果，必须自己用console.log()打印出来。把calc.js改造一下：
                                                console.log(100 + 200 + 300);
                                                再执行，就可以看到结果：
                                                C:\Workspace>node calc.js
                                                600
                                    使用严格模式  node --use_strict ....js
                                                如果在JavaScript文件开头写上'use strict';，那么Node在执行该JavaScript时将使用严格模式。但是，在服务器环境下，
                                                如果有很多JavaScript文件，每个文件都写上'use strict';很麻烦。我们可以给Nodejs传递一个参数，让Node直接为所有js文件开启严格模式：
                                                node --use_strict calc.js
                                                后续代码，如无特殊说明，我们都会直接给Node传递--use_strict参数来开启严格模式。
                                    小结
                                                用文本编辑器写JavaScript程序，然后保存为后缀为.js的文件，就可以用node直接运行这个程序了。
                                                Node的交互模式和直接运行.js文件有什么区别呢？
                                                直接输入node进入交互模式，相当于启动了Node解释器，但是等待你一行一行地输入源代码，每输入一行就执行一行。
                                                直接运行node hello.js文件相当于启动了Node解释器，然后一次性把hello.js文件的源代码给执行了，你是没有机会以交互的方式输入源代码的。
                                                在编写JavaScript代码的时候，完全可以一边在文本编辑器里写代码，一边开一个Node交互式命令窗口，在写代码的过程中，
                                                把部分代码粘到命令行去验证，事半功倍！前提是得有个27 的超大显示器！
                                    参考源码 hello.js和calc.js
                        搭建Node开发环境
                                    使用文本编辑器来开发Node程序，最大的缺点是效率太低，运行Node程序还需要在命令行单独敲命令。如果还需要调试程序，就更加麻烦了。
                                    所以我们需要一个IDE集成开发环境，让我们能在一个环境里编码、运行、调试，这样就可以大大提升开发效率。
                                    Java的集成开发环境有Eclipse，Intellij idea等，C#的集成开发环境有Visual Studio，那么问题又来了：Node.js的集成开发环境到底哪家强？
                                    考察Node.js的集成开发环境，重点放在启动速度快，执行简单，调试方便这三点上。当然，免费使用是一个加分项。
                                    综合考察后，我们隆重向大家推荐Node.js集成开发环境：
                                    Visual Studio Code
                                    Visual Studio Code由微软出品，但它不是那个大块头的Visual Studio，它是一个精简版的迷你Visual Studio，并且，Visual Studio Code可以跨！平！台！Windows、Mac和Linux通用。
                                    安装Visual Studio Code
                                    可以从Visual Studio Code的官方网站下载并安装最新的1.4版本。网速慢的童鞋请移步国内镜像。
                                    安装过程中，请务必钩上以下选项：
                                     
                                     将“通过Code打开”操作添加到Windows资源管理器目录上下文菜单
                                    这将大大提升将来的操作快捷度。
                                    在Mac系统上，Finder选中一个目录，右键菜单并没有“通过Code打开”这个操作。不过我们可以通过Automator自己添加这个操作。
                                    先运行Automator，选择“服务”：
                                     
                                    然后，执行以下操作：
                                     
                                    1.  在右侧面板选择“服务”收到选定的“文件夹”，位于“Finder.app“，该选项是为了从Finder中接收一个文件夹；
                                    2.  在左侧面板选择”实用工具“，然后找到”运行Shell脚本“，把它拽到右侧面板里；
                                    3.  在右侧”运行Shell脚本“的面板里，选择Shell”/bin/bash“，传递输入“作为自变量”，然后修改Shell脚本如下：
                                    for f in "$@"
                                    do
                                        open -a "Visual Studio Code" "$f"
                                    done
                                    保存为“Open With VSCode”后，打开Finder，选中一个文件夹，点击右键，“服务”，就可以看到“Open With VSCode”菜单：
                                     
                                    运行和调试JavaScript
                                    在VS Code中，我们可以非常方便地运行JavaScript文件。
                                    VS Code以文件夹作为工程目录（Workspace Dir），所有的JavaScript文件都存放在该目录下。此外，VS Code在工程目录下还需要一个.vscode的配置目录，里面存放里VS Code需要的配置文件。
                                    假设我们在C:\Work\目录下创建了一个hello目录作为工程目录，并编写了一个hello.js文件，则该工程目录的结构如下：
                                    hello/ <-- workspace dir
                                    |
                                    +- hello.js <-- JavaScript file
                                    |
                                    +- .vscode/  <-- VS Code config
                                       |
                                       +- launch.json <-- VS Code config file for JavaScript
                                    可以用VS Code快速创建launch.json，然后修改如下：
                                    {
                                        "version": "0.2.0",
                                        "configurations": [
                                            {
                                                "name": "Run hello.js",
                                                "type": "node",
                                                "request": "launch",
                                                "program": "${workspaceRoot}/hello.js",
                                                "stopOnEntry": false,
                                                "args": [],
                                                "cwd": "${workspaceRoot}",
                                                "preLaunchTask": null,
                                                "runtimeExecutable": null,
                                                "runtimeArgs": [
                                                    "--nolazy"
                                                ],
                                                "env": {
                                                    "NODE_ENV": "development"
                                                },
                                                "externalConsole": false,
                                                "sourceMaps": false,
                                                "outDir": null
                                            }
                                        ]
                                    }
                                    有了配置文件，即可使用VS Code调试JavaScript。
                                    视频演示：
                                    参考源码
                                    hello.js
                        模块
                                    概念
                                                在计算机程序的开发过程中，随着程序代码越写越多，在一个文件里代码就会越来越长，越来越不容易维护。
                                                为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少，很多编程语言都采用
                                                这种组织代码的方式。在Node环境中，一个.js文件就称之为一个模块（module）。
                                    使用模块有什么好处？
                                                最大的好处是大大提高了代码的可维护性。其次，编写代码不必从零开始。当一个模块编写完毕，就可以被其他地方引用。我们在编写
                                                程序的时候，也经常引用其他模块，包括Node内置的模块和来自第三方的模块。
                                                使用模块还可以避免函数名和变量名冲突。相同名字的函数和变量完全可以分别存在不同的模块中，因此，我们自己在编写模块时，不必
                                                考虑名字会与其他模块冲突。
                                    例
                                                在上一节，我们编写了一个hello.js文件，这个hello.js文件就是一个模块，模块的名字就是文件名（去掉.js后缀），所以hello.js文件就是名
                                                为hello的模块。
                                                我们把hello.js改造一下，创建一个函数，这样我们就可以在其他地方调用这个函数：
                                                'use strict';

                                                var s = 'Hello';

                                                function greet(name) {
                                                    console.log(s + ', ' + name + '!');
                                                }

                                                module.exports = greet;
                                                函数greet()是我们在hello模块中定义的，你可能注意到最后一行是一个奇怪的赋值语句，它的意思是，把函数greet作为模块的输出暴露出去，
                                                这样其他模块就可以使用greet函数了。
                                                问题是其他模块怎么使用hello模块的这个greet函数呢？我们再编写一个main.js文件，调用hello模块的greet函数：
                                                'use strict';

                                                // 引入hello模块:
                                                var greet = require('./hello');

                                                var s = 'Michael';

                                                greet(s); // Hello, Michael!
                                                注意到引入hello模块用Node提供的require函数：
                                                var greet = require('./hello');
                                                引入的模块作为变量保存在greet变量中，那greet变量到底是什么东西？其实变量greet就是在hello.js中我们用module.exports = greet;输出
                                                的greet函数。所以，main.js就成功地引用了hello.js模块中定义的greet()函数，接下来就可以直接使用它了。
                                                在使用require()引入模块的时候，请注意模块的相对路径。因为main.js和hello.js位于同一个目录，所以我们用了当前目录.：
                                                var greet = require('./hello'); // 不要忘了写相对目录!
                                                如果只写模块名：
                                                var greet = require('hello');
                                                则Node会依次在内置模块、全局模块和当前模块下查找hello.js，你很可能会得到一个错误：
                                                module.js
                                                    throw err;
                                                          ^
                                                Error: Cannot find module 'hello'
                                                    at Function.Module._resolveFilename
                                                    at Function.Module._load
                                                    ...
                                                    at Function.Module._load
                                                    at Function.Module.runMain
                                                遇到这个错误，你要检查：
                                                •   模块名是否写对了；
                                                •   模块文件是否存在；
                                                •   相对路径是否写对了。
                                    CommonJS规范
                                                这种模块加载机制被称为CommonJS规范。在这个规范下，每个.js文件都是一个模块，它们内部各自使用的变量名和函数名
                                                都互不冲突，例如，hello.js和main.js都申明了全局变量var s = 'xxx'，但互不影响。
                                                一个模块想要对外暴露变量（函数也是变量），可以用module.exports = variable;，一个模块要引用其他模块暴露的变量，
                                                用var ref = require('module_name');就拿到了引用模块的变量。
                                    结论
                                                要在模块中对外输出变量，用：
                                                module.exports = variable;
                                                输出的变量可以是任意对象、函数、数组等等。
                                                要引入其他模块输出的对象，用：
                                                var foo = require('other_module');
                                                引入的对象具体是什么，取决于引入模块输出的对象。
                                    深入了解模块原理
                                                如果你想详细地了解CommonJS的模块实现原理，请继续往下阅读。如果不想了解，请直接跳到最后做练习。
                                                当我们编写JavaScript代码时，我们可以申明全局变量：
                                                var s = 'global';
                                                在浏览器中，大量使用全局变量可不好。如果你在a.js中使用了全局变量s，那么，在b.js中也使用全局变量s，将
                                                造成冲突，b.js中对s赋值会改变a.js的运行逻辑。
                                                也就是说，JavaScript语言本身并没有一种模块机制来保证不同模块可以使用相同的变量名。
                                                那Node.js是如何实现这一点的？
                                                其实要实现“模块”这个功能，并不需要语法层面的支持。Node.js也并不会增加任何JavaScript语法。实现“模块”
                                                功能的奥妙就在于JavaScript是一种函数式编程语言，它支持闭包。如果我们把一段JavaScript代码用一个函数包装
                                                起来，这段代码的所有“全局”变量就变成了函数内部的局部变量。
                                                请注意我们编写的hello.js代码是这样的：
                                                var s = 'Hello';
                                                var name = 'world';

                                                console.log(s + ' ' + name + '!');
                                                Node.js加载了hello.js后，它可以把代码包装一下，变成这样执行：
                                                (function () {
                                                    // 读取的hello.js代码:
                                                    var s = 'Hello';
                                                    var name = 'world';

                                                    console.log(s + ' ' + name + '!');
                                                    // hello.js代码结束
                                                })();
                                                这样一来，原来的全局变量s现在变成了匿名函数内部的局部变量。如果Node.js继续加载其他模块，这些模块中定义的
                                                “全局”变量s也互不干扰。
                                                所以，Node利用JavaScript的函数式编程的特性，轻而易举地实现了模块的隔离。
                                                但是，模块的输出module.exports怎么实现？
                                                这个也很容易实现，Node可以先准备一个对象module：
                                                // 准备module对象:
                                                var module = {
                                                    id: 'hello',
                                                    exports: {}
                                                };
                                                var load = function (module) {
                                                    // 读取的hello.js代码:
                                                    function greet(name) {
                                                        console.log('Hello, ' + name + '!');
                                                    }

                                                    module.exports = greet;
                                                    // hello.js代码结束
                                                    return module.exports;
                                                };
                                                var exported = load(module);
                                                // 保存module:
                                                save(module, exported);
                                                可见，变量module是Node在加载js文件前准备的一个变量，并将其传入加载函数，我们在hello.js中可以直接使用
                                                变量module原因就在于它实际上是函数的一个参数：
                                                module.exports = greet;
                                                通过把参数module传递给load()函数，hello.js就顺利地把一个变量传递给了Node执行环境，Node会把module变量
                                                保存到某个地方。
                                                由于Node保存了所有导入的module，当我们用require()获取module时，Node找到对应的module，把这个module的
                                                exports变量返回，这样，另一个模块就顺利拿到了模块的输出：
                                                var greet = require('./hello');
                                                以上是Node实现JavaScript模块的一个简单的原理介绍。
                                    module.exports vs exports
                                                很多时候，你会看到，在Node环境中，有两种方法可以在一个模块中输出变量：
                                                方法一：对module.exports赋值：
                                                // hello.js

                                                function hello() {
                                                    console.log('Hello, world!');
                                                }

                                                function greet(name) {
                                                    console.log('Hello, ' + name + '!');
                                                }

                                                module.exports = {
                                                    hello: hello,
                                                    greet: greet
                                                };
                                                方法二：直接使用exports：
                                                // hello.js

                                                function hello() {
                                                    console.log('Hello, world!');
                                                }

                                                function greet(name) {
                                                    console.log('Hello, ' + name + '!');
                                                }

                                                function hello() {
                                                    console.log('Hello, world!');
                                                }

                                                exports.hello = hello;
                                                exports.greet = greet;
                                                但是你不可以直接对exports赋值：
                                                // 代码可以执行，但是模块并没有输出任何变量:
                                                exports = {
                                                    hello: hello,
                                                    greet: greet
                                                };
                                                如果你对上面的写法感到十分困惑，不要着急，我们来分析Node的加载机制：
                                                首先，Node会把整个待加载的hello.js文件放入一个包装函数load中执行。在执行这个load()函数前，Node准备好了module变量：
                                                var module = {
                                                    id: 'hello',
                                                    exports: {}
                                                };
                                                load()函数最终返回module.exports：
                                                var load = function (exports, module) {
                                                    // hello.js的文件内容
                                                    ...
                                                    // load函数返回:
                                                    return module.exports;
                                                };

                                                var exported = load(module.exports, module);
                                                也就是说，默认情况下，Node准备的exports变量和module.exports变量实际上是同一个变量，并且初始化为空对象{}，于是，我们可以写：
                                                exports.foo = function () { return 'foo'; };
                                                exports.bar = function () { return 'bar'; };
                                                也可以写：
                                                module.exports.foo = function () { return 'foo'; };
                                                module.exports.bar = function () { return 'bar'; };
                                                换句话说，Node默认给你准备了一个空对象{}，这样你可以直接往里面加东西。
                                                但是，如果我们要输出的是一个函数或数组，那么，只能给module.exports赋值：
                                                module.exports = function () { return 'foo'; };
                                                给exports赋值是无效的，因为赋值后，module.exports仍然是空对象{}。
                                    结论
                                                如果要输出一个键值对象{}，可以利用exports这个已存在的空对象{}，并继续在上面添加新的键值；
                                                如果要输出一个函数或数组，必须直接对module.exports对象赋值。
                                                所以我们可以得出结论：直接对module.exports赋值，可以应对任何情况：
                                                module.exports = {
                                                    foo: function () { return 'foo'; }
                                                };
                                                或者：
                                                module.exports = function () { return 'foo'; };
                                                最终，我们强烈建议使用module.exports = xxx的方式来输出模块变量，这样，你只需要记忆一种方法。
                                    练习
                                                编写hello.js，输出一个或多个函数；
                                                编写main.js，引入hello模块，调用其函数。
                                    参考源码 module
                        基本模块
                                    •   因为Node.js是运行在服务区端的JavaScript环境，服务器程序和浏览器程序相比，最大的特点是没有浏览器的
                                    安全限制了，而且，服务器程序必须能接收网络请求，读写文件，处理二进制内容，所以，Node.js内置的常用模块
                                    就是为了实现基本的服务器功能。这些模块在浏览器环境中是无法被执行的，因为它们的底层代码是用C/C++在
                                    Node.js运行环境中实现的。
                                    •   global
                                    •   在前面的JavaScript课程中，我们已经知道，JavaScript有且仅有一个全局对象，在浏览器中，叫window对象。
                                    而在Node.js环境中，也有唯一的全局对象，但不叫window，而叫global，这个对象的属性和方法也和浏览器环境
                                    的window不同。进入Node.js交互环境，可以直接输入：
                                    •   > global.console
                                    •   Console {
                                    •     log: [Function: bound ],
                                    •     info: [Function: bound ],
                                    •     warn: [Function: bound ],
                                    •     error: [Function: bound ],
                                    •     dir: [Function: bound ],
                                    •     time: [Function: bound ],
                                    •     timeEnd: [Function: bound ],
                                    •     trace: [Function: bound trace],
                                    •     assert: [Function: bound ],
                                    •     Console: [Function: Console] }
                                    •   process
                                    •   process也是Node.js提供的一个对象，它代表当前Node.js进程。通过process对象可以拿到许多有用信息：
                                    •   > process === global.process;
                                    •   true
                                    •   > process.version;
                                    •   'v5.2.0'
                                    •   > process.platform;
                                    •   'darwin'
                                    •   > process.arch;
                                    •   'x64'
                                    •   > process.cwd(); //返回当前工作目录
                                    •   '/Users/michael'
                                    •   > process.chdir('/private/tmp'); // 切换当前工作目录
                                    •   undefined
                                    •   > process.cwd();
                                    •   '/private/tmp'
                                    •   JavaScript程序是由事件驱动执行的单线程模型，Node.js也不例外。Node.js不断执行响应事件的JavaScript函数，
                                    直到没有任何响应事件的函数可以执行时，Node.js就退出了。
                                    •   如果我们想要在下一次事件响应中执行代码，可以调用process.nextTick()：
                                    •   // test.js
                                    •   
                                    •   // process.nextTick()将在下一轮事件循环中调用:
                                    •   process.nextTick(function () {
                                    •       console.log('nextTick callback!');
                                    •   });
                                    •   console.log('nextTick was set!');
                                    •   用Node执行上面的代码node test.js，你会看到，打印输出是：
                                    •   nextTick was set!
                                    •   nextTick callback!
                                    •   这说明传入process.nextTick()的函数不是立刻执行，而是要等到下一次事件循环。
                                    •   Node.js进程本身的事件就由process对象来处理。如果我们响应exit事件，就可以在程序即将退出时执行某个回调函数：
                                    •   // 程序即将退出时的回调函数:
                                    •   process.on('exit', function (code) {
                                    •       console.log('about to exit with code: ' + code);
                                    •   });
                                    判断JavaScript执行环境
                                                •   有很多JavaScript代码既能在浏览器中执行，也能在Node环境执行，但有些时候，程序本身需要判断自己到底是在
                                                什么环境下执行的，常用的方式就是根据浏览器和Node环境提供的全局变量名称来判断：
                                                •   if (typeof(window) === 'undefined') {
                                                •       console.log('node.js');
                                                •   } else {
                                                •       console.log('browser');
                                                •   }
                                                •   后面，我们将介绍Node.js的常用内置模块。
                                    •   参考源码  gl.js

CSS -- 层叠样式表 (Cascading Style Sheets) -- 定义如何显示 HTML 元素 -- 同时控制多重网页的样式和布局 -  实现内容与表现分离 -- 样式通常存储在样式表中(内/外)
            样式解决的问题 
                        创建文档内容清晰地独立于文档表现层的站点
                        提高了工作效率 -- 样式通常保存在外部的 .css 文件中。通过仅仅编辑一个简单的 CSS 文档，外部样式表使你有能力同时改变站点中所有页面的布局和外观
                        样式表允许以多种方式规定样式信息
                                    样式可以规定在单个的 HTML 元素中
                                    在 HTML 页的头元素中
                                    在一个外部的 CSS 文件中
                                    以在同一个 HTML 文档内部引用多个外部样式表
                        层叠次序 -- 数字 4 拥有最高的优先权
                                    1 浏览器缺省设置
                                    2 外部样式表
                                    3 内部样式表（位于 <head> 标签内部）
                                    4 内联样式（在 HTML 元素内部）-- 拥有最高的优先权
            CSS 语法() -- selector {declaration1; declaration2; ... declarationN } -- 选择器(需要改变样式的 HTML 元素)，以及一条或多条声明(每条声明由一个属性和一个值组成)
                        单条声明() -- selector {property: value} -- 属性(property) 是您希望设置的 样式属性(style attribute)。每个属性有一个值。属性和值被冒号分开 -- 用花括号来包围声明
                        多重声明() -- selector {property: value; property: value; property: value; } --  如果值为若干单词，则要给值加引号
                        选择器分组() -- selector, selector, selector {property: value} -- 用逗号将需要分组的选择器分开 -- 被分组的选择器可以分享相同的声明
                        继承() -- 子元素从父元素继承属性
                        派生选择器() -- selector selector selector {property: value} -- 依据元素在其位置的上下文关系来定义样式 -- 使标记更加简洁
                        id 选择器() -- ' #id {property: value} -- 可以为标有特定 id 的 HTML 元素指定特定的样式 -- 以 "#" 来定义'
                        id 派生选择器() -- ' #id selector {property: value} '
                        类选择器() -- .class值 {property: value} -- 可以为标有特定 class的 HTML 元素指定特定的样式 -- 以一个点号显示
                        类派生选择器() -- .class值 selector {property: value} 
                        属性选择器() -- [指定属性] {property: value} -- 对指定属性的 HTML 元素设置样式 -- 不仅限于 class和 id 属性
                        属性和值选择器() -- [指定属性 = 指定值] {property: value}
                        属性和值选择器(多个值) -- [指定属性 ~= 指定包含值] {property: value} -- 对'包含'指定属性的 HTML 元素设置样式
                        CSS 属性选择器参考 
                                    选择器 描述
                                    [attribute] 用于选取带有指定属性的元素。
                                    [attribute=value]   用于选取带有指定属性和值的元素。
                                    [attribute~=value]  用于选取属性值中包含指定词汇的元素。
                                    [attribute|=value]  用于选取带有以指定值开头的属性值的元素，该值必须是整个单词。
                                    [attribute^=value]  匹配属性值以指定值开头的每个元素。
                                    [attribute$=value]  匹配属性值以指定值结尾的每个元素。
                                    [attribute*=value]  匹配属性值中包含指定值的每个元素。
            CSS 创建()
                        外部样式表 -- 当样式需要应用于很多页面时，是理想的选择 -- 通过改变一个文件来改变整个站点的外观 -- 每个页面使用 <link> 标签链接到样式表 -- <link> 标签在（文档的）头部
                                    <head>
                                    <link rel="stylesheet" type="text/css" href="mystyle.css" />
                                    </head>
                                    浏览器会从文件 mystyle.css 中读到样式声明，并根据它来格式文档
                                    外部样式表可以在任何文本编辑器中进行编辑。文件不能包含任何的 html 标签。样式表应该以 .css 扩展名进行保存 -- 不要在属性值与单位之间留有空格 

                        内部样式表 -- 当单个文档需要特殊的样式时，使用内部样式表。使用 <style> 标签在文档头部定义内部样式表
                                    <head>
                                    <style type="text/css">
                                      hr {color: sienna;}
                                      p {margin-left: 20px;}
                                      body {background-image: url("images/back40.gif");}
                                    </style>
                                    </head> 
                        内联样式 -- 当样式仅需要在一个元素上应用一次时 -- 慎用这种方法 -- 在相关的标签内使用样式（style）属性
                                    <p style="color: sienna; margin-left: 20px">
                                    This is a paragraph
                                    </p>
                        多重样式 -- 如果某些属性在不同的样式表中被同样的选择器定义，那么属性值将从更具体的样式表中被继承过来
                                    例如，外部样式表拥有针对 h3 选择器的三个属性：
                                    h3 {
                                      color: red;
                                      text-align: left;
                                      font-size: 8pt;
                                      }
                                    而内部样式表拥有针对 h3 选择器的两个属性：
                                    h3 {
                                      text-align: right; 
                                      font-size: 20pt;
                                      }
                                    假如拥有内部样式表的这个页面同时与外部样式表链接，那么 h3 得到的样式是：
                                    color: red; 
                                    text-align: right; 
                                    font-size: 20pt;
                                    即颜色属性将被继承于外部样式表，而文字排列（text-alignment）和字体尺寸（font-size）会被内部样式表中的规则取代。
            CSS 样式属性()
                        CSS 背景 -- 定义元素背景
                                    背景 -- 简写属性，作用是将背景属性设置在一个声明中
                                    背景色 -- {background-color: value;} -- 可以为所有元素设置背景色 -- 不能继承，其默认值是 transparent -- 这样其祖先元素的背景才能可见
                                    背景图像 -- {background-image: url(图片地址);} -- 默认值是 none，表示背景上没有放置任何图像 -- 所有背景属性都不能继承
                                    背景重复 -- {background-repeat: value;} -- 属性值 (repeat - 所有方向，repeat-x - 水平重复，repeat-y - 垂直重复) -- 默认地，背景图像将从一个元素的左上角开始
                                    背景定位 -- {background-position: value;} -- 设置背景图像的起始位置
                                    背景关联 -- {background-attachment: value;} -- 背景图像是否固定或者随着页面的其余部分滚动
                        CSS 文本 -- 定义文本外观
                                    属性  描述
                                    color   设置文本颜色
                                    direction   设置文本方向。
                                    line-height 设置行高。
                                    letter-spacing  设置字符间距。-- 与 word-spacing 的区别在于，字母间隔修改的是字符或字母之间的间隔 -- 默认关键字是 normal
                                    text-align  对齐元素中的文本。-- 值 left(左对齐)、right 、center、<CENTER>(控制元素的对齐)、justify(两端对齐)、 -- 默认值是 left
                                    text-decoration 向文本添加修饰。
                                                text-decoration 有 5 个值：
                                                none
                                                underline
                                                overline
                                                line-through
                                                blink                        
                                    text-indent 缩进元素中文本的首行。-- 可以使用所有长度单位，包括百分比值
                                    text-shadow 设置文本阴影。 
                                    text-transform  控制元素中的字母。
                                                text-transform 属性处理文本的大小写。这个属性有 4 个值：
                                                none
                                                uppercase
                                                lowercase
                                                capitalize                        
                                    unicode-bidi    设置文本方向。
                                    white-space 设置元素中空白的处理方式。
                                                    white-space 属性的行为：
                                                    值   空白符 换行符 自动换行
                                                    pre-line    合并  保留  允许
                                                    normal  合并  忽略  允许
                                                    nowrap  合并  忽略  不允许
                                                    pre 保留  保留  不允许
                                                    pre-wrap    保留  保留  允许                        
                                    word-spacing    设置字间距  --  属性接受一个正长度值或负长度值。正长度值，那么字之间的间隔就会增加。负值，会把它拉近          
                        CSS 字体 -- 定义文本的字体系列、大小、加粗、风格（如斜体）和变形（如小型大写字母）
                                    属性  描述
                                    font    简写属性。作用是把所有针对字体的属性设置在一个声明中。
                                    font-family 设置字体系列。
                                    font-size   设置字体的尺寸。
                                    font-size-adjust    当首选字体不可用时，对替换字体进行智能缩放。（CSS2.1 已删除该属性。）
                                    font-stretch    对字体进行水平拉伸。（CSS2.1 已删除该属性。）
                                    font-style  设置字体风格。
                                    font-variant    以小型大写字体或者正常字体显示文本。
                                    font-weight 设置字体的粗细。            
                        CSS 链接 -- 能够以不同的方法为链接设置样式
                                    链接的四种状态：
                                                a:link - 普通的、未被访问的链接
                                                a:visited - 用户已访问的链接
                                                a:hover - 鼠标指针位于链接的上方
                                                a:active - 链接被点击的时刻      
                                    次序规则
                                                a:hover 必须位于 a:link 和 a:visited 之后
                                                a:active 必须位于 a:hover 之后
                                    文本修饰
                                                text-decoration 属性大多用于去掉链接中的下划线，值有 none，underline
                                                background-color 属性规定链接的背景色
                        CSS 列表 -- 列表属性允许你放置、改变列表项标志，或者将图像作为列表项标志
                                    CSS 列表属性(list)
                                                属性  描述
                                                list-style  简写属性。用于把所有用于列表的属性设置于一个声明中。
                                                list-style-image    将图象设置为列表项标志。
                                                list-style-position 设置列表中列表项标志的位置。
                                                list-style-type 设置列表项标志的类型。
                                                marker-offset
                                    列表类型 -- list-style-type 属性 -- 修改用于列表项的标志类型 
                                                在一个无序列表中，列表项的标志 (marker) 是出现在各列表项旁边的圆点
                                                在有序列表中，标志可能是字母、数字或另外某种计数体系中的一个符号
                                    列表项图像 --  list-style-image 属性 -- ul li {list-style-image : url(xxx.gif)}
                                    列表标志位置 -- list-style-position 
                                    简写列表样式 -- li {list-style : url(example.gif) square inside}
                        CSS 表格 -- 改善表格的外观
                                    表格边框
                                    表格宽度和高度
                                    表格文本对齐
                                    表格内边距
                                    表格颜色
                                    Table 属性
                                                属性  描述
                                                border -- 设置表格边框
                                                border-collapse 设置是否把表格边框合并为单一的边框。
                                                border-spacing  设置分隔单元格边框的距离。
                                                caption-side    设置表格标题的位置。
                                                empty-cells 设置是否显示表格中的空单元格。
                                                table-layout    设置显示单元、行和列的算法。
                        CSS 轮廓 -- 规定元素轮廓的样式、颜色和宽度 -- 是绘制于元素周围的一条线，位于边框边缘的外围，可起到突出元素的作用
                                    属性  描述  CSS
                                    outline 在一个声明中设置所有的轮廓属性。    2
                                    outline-color   设置轮廓的颜色。    2
                                    outline-style   设置轮廓的样式。    2
                                    outline-width   设置轮廓的宽度。    2            
            CSS 框模型() -- 规定了元素框处理元素内容、内边距、边框 和 外边距 的方式 -- 一切皆为框
                        CSS 框模型概述 -- 可以使用 display 属性改变生成的框的类型 -- block值，可以让行内元素表现得像块级元素一样。none值，让生成的元素根本没有框
                                    div、h1 或 p 元素常常被称为块级元素。这意味着这些元素显示为一块内容，即“块框”。
                                    与之相反，span 和 strong 等元素称为“行内元素”，这是因为它们的内容显示在行中，即“行内框”

                                    元素框的最内部分是实际的内容，直接包围内容的是内边距。内边距的边缘是边框。边框以外是外边距，外边距默认是透明的，因此不会遮挡其后的任何元素
                                    在 CSS 中，width 和 height 指的是内容区域的宽度和高度。增加内边距、边框和外边距不会影响内容区域的尺寸，但是会增加元素框的总尺寸
                                    背景应用于由内容和内边距、边框组成的区域
                                    内边距、边框和外边距都是可选的，默认值是零
                                    提示：内边距、边框和外边距可以应用于一个元素的所有边，也可以应用于单独的边。
                                    提示：外边距可以是负值，而且在很多情况下都要使用负值的外边距。
                                    术语翻译
                                                element : 元素。
                                                padding : 内边距，也有资料将其翻译为填充。
                                                border : 边框。
                                                margin : 外边距，也有资料将其翻译为空白或空白边。
                        CSS 内边距 -- 元素的内边距在边框和内容区之间。 padding 属性 -- 定义元素边框与元素内容之间的空白区域 -- 不允许使用负值
                                    CSS 内边距属性
                                                属性  描述
                                                padding 简写属性。作用是在一个声明中设置元素的所内边距属性。
                                                padding-bottom  设置元素的下内边距。
                                                padding-left    设置元素的左内边距。
                                                padding-right   设置元素的右内边距。
                                                padding-top 设置元素的上内边距。        
                        CSS 边框 -- 元素的边框 (border) 是围绕元素内容和内边距的一条或多条线 -- CSS border 属性允许你规定元素边框的样式、宽度和颜色
                                    CSS 边框属性
                                                属性  描述
                                                border  简写属性，用于把针对四个边的属性设置在一个声明。
                                                border-style    用于设置元素所有边框的样式，或者单独地为各边设置边框样式。
                                                border-width    简写属性，用于为元素的所有边框设置宽度，或者单独地为各边边框设置宽度。
                                                border-color    简写属性，设置元素的所有边框中可见部分的颜色，或为 4 个边分别设置颜色。
                                                border-bottom   简写属性，用于把下边框的所有属性设置到一个声明中。
                                                border-bottom-color 设置元素的下边框的颜色。
                                                border-bottom-style 设置元素的下边框的样式。
                                                border-bottom-width 设置元素的下边框的宽度。
                                                border-left 简写属性，用于把左边框的所有属性设置到一个声明中。
                                                border-left-color   设置元素的左边框的颜色。
                                                border-left-style   设置元素的左边框的样式。
                                                border-left-width   设置元素的左边框的宽度。
                                                border-right    简写属性，用于把右边框的所有属性设置到一个声明中。
                                                border-right-color  设置元素的右边框的颜色。
                                                border-right-style  设置元素的右边框的样式。
                                                border-right-width  设置元素的右边框的宽度。
                                                border-top  简写属性，用于把上边框的所有属性设置到一个声明中。
                                                border-top-color    设置元素的上边框的颜色。
                                                border-top-style    设置元素的上边框的样式。
                                                border-top-width    设置元素的上边框的宽度。
                        CSS 外边距 -- 围绕在元素边框的空白区域是外边距。设置外边距会在元素外创建额外的“空白” -- margin 属性 -- 接受任何长度单位、百分数值甚至负值
                                    值复制
                                                如果缺少左外边距的值，则使用右外边距的值。
                                                如果缺少下外边距的值，则使用上外边距的值。
                                                如果缺少右外边距的值，则使用上外边距的值。          
                                    CSS 外边距属性
                                                属性  描述
                                                margin  简写属性。在一个声明中设置所有外边距属性。
                                                margin-bottom   设置元素的下外边距。
                                                margin-left 设置元素的左外边距。
                                                margin-right    设置元素的右外边距。
                                                margin-top  设置元素的上外边距。              
                        CSS 外边距合并 -- 当两个垂直外边距相遇时，它们将形成一个外边距 -- 合并后的外边距的高度等于两个发生合并的外边距的高度中的较大者

                                    注释：只有普通文档流中块框的垂直外边距才会发生外边距合并。行内框、浮动框或绝对定位之间的外边距不会合并
            CSS 定位() -- (Positioning) 属性 -- 允许你定义元素框相对于其正常位置应该出现的位置，或者相对于父元素、另一个元素甚至浏览器窗口本身的位置
                        CSS 定位属性
                                    CSS 定位属性允许你对元素进行定位。
                                    属性  描述
                                    position    把元素放置到一个静态的、相对的、绝对的、或固定的位置中。
                                    top 定义了一个定位元素的上外边距边界与其包含块上边界之间的偏移。
                                    right   定义了定位元素右外边距边界与其包含块右边界之间的偏移。
                                    bottom  定义了定位元素下外边距边界与其包含块下边界之间的偏移。
                                    left    定义了定位元素左外边距边界与其包含块左边界之间的偏移。
                                    overflow    设置当元素的内容溢出其区域时发生的事情。
                                    clip    设置元素的形状。元素被剪入这个形状之中，然后显示出来。
                                    vertical-align  设置元素的垂直对齐方式。
                                    z-index 设置元素的堆叠顺序。
                        CSS 定位概述 -- 三种基本的定位机制：普通流、浮动和绝对定位 -- 除非专门指定，否则所有框都在普通流中定位
                        static -- 元素框正常生成。块级元素生成一个矩形框，作为文档流的一部分，行内元素则会创建一个或多个行框，置于其父元素中
                        CSS 相对定位 -- relative -- 元素框偏移某个距离。元素仍保持其未定位前的形状，它原本所占的空间仍保留
                        CSS 绝对定位 -- absolute -- 元素框从文档流完全删除，并相对于其包含块定位
                        fixed -- 元素框的表现类似于将 position 设置为 absolute，不过其包含块是视窗本身
                        CSS 浮动 -- float 属性-- 浮动的框可以向左或向右移动，直到它的外边缘碰到包含框或另一个浮动框的边框为止
            CSS 选择器
                        CSS 元素选择器
                        CSS 选择器分组
                        CSS 类选择器详解
                        CSS ID 选择器详解
                        CSS 属性选择器详解
                        CSS 后代选择器
                        CSS 子元素选择器
                        CSS 相邻兄弟选择器
                        CSS 伪类
                        CSS 伪元素
            CSS 高级()
                        CSS 对齐
                                    对齐块元素 -- 块元素指的是占据全部可用宽度的元素，并且在其前后都会换行
                                    使用 margin 属性来水平对齐
                                                可通过将左和右外边距设置为 "auto"，来对齐块元素
                                    使用 position 属性进行左和右对齐
                                    使用 float 属性来进行左和右对齐
                        CSS 尺寸 -- (Dimension) 属性允许你控制元素的高度和宽度。同样，它允许你增加行间距
                                    CSS 尺寸属性
                                                CSS 尺寸属性允许你控制元素的高度和宽度。同样，还允许你增加行间距。
                                                属性  描述
                                                height  设置元素的高度。
                                                line-height 设置行高。
                                                max-height  设置元素的最大高度。
                                                max-width   设置元素的最大宽度。
                                                min-height  设置元素的最小高度。
                                                min-width   设置元素的最小宽度。
                                                width   设置元素的宽度。
                        CSS 分类 -- 分类属性允许你规定如何以及在何处显示元素
                                    CSS 分类属性 (Classification)
                                                CSS 分类属性允许你控制如何显示元素，设置图像显示于另一元素中的何处，相对于其正常位置来定位元素，使用绝对值来定位元素，以及元素的可见度。
                                                属性  描述
                                                clear   设置一个元素的侧面是否允许其他的浮动元素。
                                                cursor  规定当指向某元素之上时显示的指针类型。
                                                display 设置是否及如何显示元素。
                                                float   定义元素在哪个方向浮动。
                                                position    把元素放置到一个静态的、相对的、绝对的、或固定的位置中。
                                                visibility  设置元素是否可见或不可见。
                        CSS 导航栏 = 链接列表 -- 拥有易用的导航条对于任何网站都很重要 -- 导航栏基本上是一个链接列表，因此使用 <ul> 和 <li> 元素是非常合适的
                                                导航栏需要标准的 HTML 作为基础。
                                                            在我们的例子中，将用标准的 HTML 列表来构建导航栏。
                                                导航栏基本上是一个链接列表，因此使用 <ul> 和 <li> 元素是非常合适的：
                                                            实例
                                                            <ul>
                                                            <li><a href="default.asp">Home</a></li>
                                                            <li><a href="news.asp">News</a></li>
                                                            <li><a href="contact.asp">Contact</a></li>
                                                            <li><a href="about.asp">About</a></li>
                                                            </ul>
                                                            亲自试一试
                                                现在，让我们从列表中去掉圆点和外边距：
                                                            实例
                                                            ul
                                                            {
                                                            list-style-type:none;
                                                            margin:0;
                                                            padding:0;
                                                            }
                                                            亲自试一试
                                                            例子解释：
                                                            list-style-type:none - 删除圆点。导航栏不需要列表项标记。
                                                            把外边距和内边距设置为 0 可以去除浏览器的默认设定。
                                                            以上例子中的代码是用在垂直、水平导航栏中的标准代码。
                                                垂直导航栏
                                                            如需构建垂直导航栏，我们只需要定义 <a> 元素的样式，除了上面的代码之外：
                                                            实例
                                                            a
                                                            {
                                                            display:block;
                                                            width:60px;
                                                            }
                                                            亲自试一试
                                                            例子解释：
                                                            display:block - 把链接显示为块元素可使整个链接区域可点击（不仅仅是文本），同时也允许我们规定宽度。
                                                            width:60px - 块元素默认占用全部可用宽度。我们需要规定 60 像素的宽度。
                                                            提示：请同时看一看我们完整样式的导航栏实例。
                                                            注释：请始终规定垂直导航栏中 <a> 元素的宽度。如果省略宽度，IE6 会产生意想不到的结果。
                                                水平导航栏
                                                            有两种创建水平导航栏的方法。使用行内或浮动列表项。
                                                            两种方法都不错，但是如果您希望链接拥有相同的尺寸，就必须使用浮动方法。
                                                行内列表项
                                                            除了上面的“标准”代码，构建水平导航栏的方法之一是将 <li> 元素规定为行内元素：
                                                            实例
                                                            li
                                                            {
                                                            display:inline;
                                                            }
                                                            亲自试一试
                                                            例子解释：
                                                            display:inline; - 默认地，<li> 元素是块元素。在这里，我们去除了每个列表项前后的换行，以便让它们在一行中显示。
                                                            提示：请看一下我们完整样式的水平导航栏实例。
                                                对列表项进行浮动
                                                            在上面的例子中，链接的宽度是不同的。
                                                            为了让所有链接拥有相等的宽度，浮动 <li> 元素并规定 <a> 元素的宽度：
                                                            实例
                                                            li
                                                            {
                                                            float:left;
                                                            }
                                                            a
                                                            {
                                                            display:block;
                                                            width:60px;
                                                            }
                                                            亲自试一试
                                                            例子解释：
                                                            float:left - 使用 float 来把块元素滑向彼此。
                                                            display:block - 把链接显示为块元素可使整个链接区域可点击（不仅仅是文本），同时也允许我们规定宽度。
                                                            width:60px - 由于块元素默认占用全部可用宽度，链接无法滑动至彼此相邻。我们需要规定 60 像素的宽度。
                                                提示：请看一下我们完整样式的水平导航栏实例。            
                        CSS 图片库
                        CSS 图片透明 -- opacity 属性
                        CSS 媒介类型 -- 媒介类型(Media Types)允许你定义以何种媒介来提交文档。文档可以被显示在显示器、纸媒介或者听觉浏览器等
                                    @media 规则使你有能力在相同的样式表中，使用不同的样式规则来针对不同的媒介
                                    不同的媒介类型
                                                注释：媒介类型名称对大小写不敏感。
                                                媒介类型    描述
                                                all 用于所有的媒介设备。
                                                aural   用于语音和音频合成器。
                                                braille 用于盲人用点字法触觉回馈设备。
                                                embossed    用于分页的盲人用点字法打印机。
                                                handheld    用于小的手持的设备。
                                                print   用于打印机。
                                                projection  用于方案展示，比如幻灯片。
                                                screen  用于电脑显示器。
                                                tty 用于使用固定密度字母栅格的媒介，比如电传打字机和终端。
                                                tv  用于电视机类型的设备。
