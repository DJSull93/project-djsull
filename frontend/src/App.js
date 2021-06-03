import React from "react"

const App = () => {
return(<>
<nav>
  <link to="/">Home</link>
  <link to="/">Blog</link>
  <link to="/">About Me</link>
</nav>

<h1>첫 번째 크기 헤드라인</h1>
<h2>두 번째 크기 헤드라인</h2>
<h3>세 번째 크기 헤드라인</h3>
<h4>네 번째 크기 헤드라인</h4>
<h5>다섯 번째 크기 헤드라인</h5>
<p>문단은 p로 쓰세요. p는 아마도 Paragraph의 앞글자를 따온 것이겠죠?</p>
<list href="http://www.google.com">Go to google</list>
<hr/>
<img src="./images/Figure-1.jpg" width="600px">
</img>

</>)
}

export default App