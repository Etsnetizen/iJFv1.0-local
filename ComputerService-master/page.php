
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="image/">
    <link rel="stylesheet" type="text/css" href="css/index.css">
    <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
    <script type="text/javascript" src="js/jquery-3.3.1.min.js"></script>
    <script type="text/javascript" src="js/bootstrap.min.js"></script>
</head>

<style type="text/css">
   body{
        font-size: 12px;font-family: verdana;width: 100%;
    }
    div.page{
        text-align: center;
    }
    div.conntent{
        height: 300px;
    }
    div.page a{
        border:#aaaadd 1px solid;text-decoration: none;padding: 2px 5px 2px 5px;margin: 2px;
    }
    div.page span.current{
        border:#000099 1px solid;background-color: #000099;padding: 2px 5px 2px 5px;margin: 2px;color: #fff;font-weight: bold;
    } 
    div.page span.disabled{
        border:#eee 1px solid;padding:2px 5px 2px 5px; margin: 2px;color:#ddd;
    }
    div.page form{
        display: inline;
    }
</style>
<body>
<?php
    //设置级别错误，通知类除外
    error_reporting('E_ALL&~E_NOTICE');  
    /**1---传入页码 ,使用GET获取**/
   $page=$_GET['p'];
    /**2---根据页码取出数据：php->mysql处理**/
    $host="127.0.0.1";
    $username="root";
    $password="";
    $db="gdpujf";
    $pageSize=3;
    $showPage=5;
	
    //连接数据库,面向过程
    $conn=mysqli_connect($host,$username,$password);
    if(!$conn){
        echo "数据库连接失败";
        exit;
    }
    //选择所要操作的数据库
    mysqli_select_db($conn,$db);
    //设置数据库编码格式
    mysqli_query($conn,"SET NAMES UTF8");
    //编写sql获取分页数据 SELECT * FROM 表名 LIMIT 起始位置，显示条数
	$qid = mysqli_query($conn,"SELECT count(*) as total FROM student WHERE state='已处理'");//查询是否有重复的数据
	$res = mysqli_fetch_array($qid);
	$undone = $res['total'];
	$sql="SELECT * FROM student order by number ASC LIMIT ".(($page-1)*$pageSize+$undone).",{$pageSize}";
    $result=mysqli_query($conn,$sql);//把sql语句传送到数据库
    /*-----表格部分-----*/
	echo "<div class='conntent'>";   //将数据显示到table中，并未table设置格式
    echo "<table border=1 cellspacing=0 width=30% align=center>";
    echo "<tr><td>number</td><td>state</td></tr>";
    while ($row = mysqli_fetch_assoc($result)) {
         echo "<tr>";
         echo "<td>{$row['number']}</td>";
         echo "<td>{$row['state']}</td>";
         echo "<tr>";
    }
    echo "</table>";
    echo "</div>";
	 /*-----表格部分结束-----*/
    //释放结果
    mysqli_free_result($result);
    //获取数据总条数
	/*------分页部分-------*/
    $total_sql="SELECT COUNT(*)FROM student where state='未处理'";
    $total_result=mysqli_fetch_array(mysqli_query($conn,$total_sql));
    $total=$total_result[0];
    $total_pages=ceil($total/$pageSize);
    //关闭数据库
    mysqli_close($conn);
    /**3---显示数据+显示分页条**/
    $page_banner="<nav aria-label='Page navigation example'> <ul class='pagination'>";
    //计算偏移量
    $pageoffset=($showPage-1)/2;
    //两种情况下 首页、上一页 的显示效果
    if($page>1){
        $page_banner .= "<li class='page-item'><a class='page-link' href='".$_SERVER['PHP_SELF']."?p=1'> 首页</a></li>";
        $page_banner .= "<li class='page-item'><a class='page-link' href='".$_SERVER['PHP_SELF']."?p=" .($page-1) . "'>&laquo;上一页</a></li>";
    }else{
        $page_banner .="<li class='page-item  disabled'><a class='page-link' href='#'>首页</a></li>   ";//<li class='page-item  disabled'><a class='page-link' href=''>首页</a></li>      <span class='disabled'>首页</span>   
        $page_banner .="<li class='page-item disabled'><a class='page-link' href='#'> &laquo;上一页</a></li> ";//<li class='page-item disabled'><a class='page-link' href=''> 上一页</a></li>    <span class='disabled'><上一页</span>
    }
    //显示
    $start=1;
    $end=$total_pages;
    //当总条数大于分页数时
    if($total_pages>$showPage){
        if($page>$pageoffset+1){
            $page_banner .="...";
        }
        if($page>$pageoffset){
            $start=$page-$pageoffset;
            $end=$total_pages>$page+$pageoffset?$page+$pageoffset:$total_pages;//三段式
        }
        //最前面几个特殊页号的显示。当前指的是页号1或者2时
        else{
            $start=1;
            $end=$showPage;
        }
        //最后面几个特殊页号的显示，当前显示的是页号7和8
        if($page+$pageoffset>$total_pages){
            $start=$start-($page+$pageoffset-$end);//注意理解这一句
        }
    }
    //显示页码
    for($i=$start;$i<=$end;$i++){
        //当前页页码上显示背景色
        if($page==$i){
            $page_banner .="<li class='page-item active'><span class='page-link'>{$i}<span class='sr-only'>(current)</span></span>";
        }
        //非当前页码显示
        else{
           // $page_banner .= "<a href='".$_SERVER['PHP_SELF']."?p=" .$i . "'>{$i}</a>"; 
			 $page_banner .=  "<li class='page-item'><a class='page-link' href='".$_SERVER['PHP_SELF']."?p=" .$i . "'>{$i}</a></li>";
        }    
    }
    if($total_pages>$showPage&&$total_pages>$page+$pageoffset){
        $page_banner .="...";    
    }
    //两种情况下的尾页、下一页 的显示效果
    if($page<$total_pages){
        $page_banner .= "<li class='page-item'><a class='page-link' href='".$_SERVER['PHP_SELF']."?p=" .($page+1) . "'>下一页 &raquo;</a></li>";
        $page_banner .= "<li class='page-item'><a class='page-link' href='".$_SERVER['PHP_SELF']."?p=$total_pages'>尾页</a></li>";
    }else{
        $page_banner .="<li class='page-item  disabled'><a class='page-link' href='#'>下一页&raquo;</a></li>  ";
        $page_banner .="<li class='page-item disabled'><a class='page-link' href='#'>  尾页</a></li>";
    }
    $page_banner .= "共{$total_pages}页,";
    $page_banner .= "<form action='page.php' method='get'>";
    $page_banner .= " 到第<input type='text' size=2 value='1' name='p'>页";
    $page_banner .= "<input type='submit' value='确定'>";
    $page_banner .= "</form>";
    $page_banner .= "</ul></nav>";
    echo $page_banner;
	?>
<nav aria-label="Page navigation example">
	    <!-- Add class .pagination-lg for larger blocks or .pagination-sm for smaller blocks-->
	    <ul class="pagination">
		  <li class="page-item"><a class="page-link" href="#">首页</a></li>
	      <li class="page-item"> <a class="page-link" href="#" aria-label="Previous"> <span aria-hidden="true">&laquo;上一页</span> <span class="sr-only">Previous</span> </a> </li>
	      <li class="page-item"><a class="page-link" href="#">1</a></li>
	      <li class="page-item"><a class="page-link" href="#">2</a></li>
	      <li class="page-item"><a class="page-link" href="#">3</a></li>
	      <li class="page-item"><a class="page-link" href="#">4</a></li>
	      <li class="page-item"><a class="page-link" href="#">5</a></li>
	      <li class="page-item"> <a class="page-link" href="#" aria-label="Next"> <span aria-hidden="true">下一页&raquo;</span> <span class="sr-only">Next</span> </a> </li>
		  <li class="page-item"><a class="page-link" href="#">尾页</a></li>
        </ul>
  </nav>
</body>
</html>
