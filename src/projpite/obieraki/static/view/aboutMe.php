<div class="container">
<br><br><br><br>

<?php 
//$courses = $data->fetchAll();
$about = $aboutMe->fetchAll();
//$my = $myCourses->fetchAll();	 
//$class = $classes->fetchAll();
$course = $courses->fetchAll();
?>
<br><br>
<h2>Account information:</h2>

<div class="content">
<?php

                echo  '<table class="table">';
                echo  '<tr class="active"><td>Name: </td><td>'.$about[0]['name'].'</td></tr>';
                echo  '<tr><td>Surname: </td><td>'.$about[0]['surname'].'</td></tr>';
                
        if(!isset($_SESSION['student']) == ''){
                echo  '<tr class="active"><td>Field of study: </td><td>'.$about[0]['fieldofstudy'].'</td></tr>';
                echo  '<tr><td>Year: </td><td>'.$about[0]['year_2'].'</td></tr>';
                echo  '<tr class="active"><td>Semester: </td><td>'.$about[0]['semester'].'</td></tr>';
                echo  '<tr><td>ID: </td><td>'.$about[0]['id'].'</td></tr>';
        } else if(!isset($_SESSION['staff']) == '') {
                echo  '<tr class="active"><td>Department: </td><td>'.$about[0]['department'].'</td></tr>';
                echo  '<tr><td>Title: </td><td>'.$about[0]['title'].'</td></tr>';  
        }
                echo  '<tr class="active"><td>Login: </td><td>'.$about[0]['login'].'</td></tr>';
                echo  '<tr><td>E-Mail: </td><td>'.$about[0]['mail'].'</td></tr>';
                
		echo '</table></div>';	
                

    

	?>
</div>
<br><br>
