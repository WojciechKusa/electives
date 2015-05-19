<?php
/**
 * view courses.
 */
?>

<div class="container">
<br><br><br><br>

<?php 
$courses = $data->fetchAll();

	 
?>


<div class="content">
    <div class="row"><div class="col-xs-6"><div id="DataTables_Table_0_length" class="dataTables_length"><label><select size="1" name="DataTables_Table_0_length" aria-controls="DataTables_Table_0"><option value="10" selected="selected">10</option><option value="25">25</option><option value="50">50</option><option value="100">100</option></select> records per page</label></div></div><div class="col-xs-6"><div class="dataTables_filter" id="DataTables_Table_0_filter"><label>Search: <input type="text" aria-controls="DataTables_Table_0"></label></div></div></div>
<?php
		$j = 0;
  		echo 	'<table class="table table-striped">';
		echo '<thead><tr><th>ID</th><th>Name</th><th>ECTS</th><th>Hours</th><th>Min students</th>
                    <th>Max students</th><th>Current number</th><th>Coordinator</th><th>Semester</th></tr></thead>
		<tbody>';

		while ($j != count($courses)) {
			
				  echo '<tr>';
				  echo '<td>'.$courses[$j][1].'</td>';
				  echo '<td><a href="index.php?controller=store&amp;action=viewCourse&amp;id='.$courses[$j]['idcourse'].'">'.$courses[$j][0].'</td>';
				  echo '<td>'.$courses[$j][2].' pkt</td>';
                                  echo '<td>'.$courses[$j][4].' h</td>';
                                  echo '<td>'.$courses[$j][5].'</td>';
                                  echo '<td>'.$courses[$j][6].'</td>';
                                  echo '<td>'.$courses[$j][11].'</td>';
                                  echo '<td>'.$courses[$j][8].' '.$courses[$j][9].' '.$courses[$j][10].'</td>';
                                  echo '<td>'; if ($courses[$j][7] == 0) echo 'Winter';
                                  else echo 'Summer'; echo '</td>';
				  echo '</tr>';
			
		$j++;
		}
			echo '</tbody></table>';
			echo '</div>';		
	
	?>
</div>


