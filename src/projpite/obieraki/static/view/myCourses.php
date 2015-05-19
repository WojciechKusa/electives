<?php

?>

<div class="container">
<br><br><br><br>

<?php 
//$courses = $data->fetchAll();
$about = $aboutMe->fetchAll();
$my = $myCourses->fetchAll();	 
//$class = $classes->fetchAll();
$course = $courses->fetchAll();
?>
<br><br>
<h2>My courses:</h2>

<div class="content">
    <div class="row"><div class="col-xs-6"><div id="DataTables_Table_0_length" class="dataTables_length"><label><select size="1" name="DataTables_Table_0_length" aria-controls="DataTables_Table_0"><option value="10" selected="selected">10</option><option value="25">25</option><option value="50">50</option><option value="100">100</option></select> records per page</label></div></div><div class="col-xs-6"><div class="dataTables_filter" id="DataTables_Table_0_filter"><label>Search: <input type="text" aria-controls="DataTables_Table_0"></label></div></div></div>
<?php
if(!isset($_SESSION['student']) == ''){
		$j = 0;
  		echo 	'<table class="table table-striped">';
		echo '<thead><tr><th>ID</th><th>Name</th><th>ECTS</th><th>Hours</th><th>Min students</th>
                    <th>Max students</th><th>Coordinator</th><th>Semester</th><th></th></tr></thead>
		<tbody>';

		while ($j != count($my)) {
			
				  echo '<tr>';
				  echo '<td>'.$my[$j][1].'</td>';
				  echo '<td><a href="index.php?controller=store&amp;action=viewCourse&amp;id='.$my[$j]['idcourse'].'">'.$my[$j][0].'</td>';
				  echo '<td>'.$my[$j][2].' pkt</td>';
                                  echo '<td>'.$my[$j][4].' h</td>';
                                  echo '<td>'.$my[$j][5].'</td>';
                                  echo '<td>'.$my[$j][6].'</td>';
//                                  echo '<td>'.$my[$j][11].'</td>';
                                  echo '<td>'.$my[$j][8].' '.$course[$j][9].' '.$my[$j][10].'</td>';
                                  echo '<td>'; if ($my[$j]['7'] == 0) { echo 'Winter'; }
                                  else { echo 'Summer'; echo '</td>'; }
                                  echo '<td><button type="button" class="btn btn-danger" onClick="location.href=\'index.php?controller=student&amp;action=signOut&amp;id='.$my[$j]['idcourse'].'\'">Sign out</button></td>';
				  echo '</tr>';
			
		$j++;
		}
			echo '</tbody></table>';
			echo '</div>';		
}
else if(!isset($_SESSION['staff']) == '') {

    
}
	
	?>
</div>
<br><br>
