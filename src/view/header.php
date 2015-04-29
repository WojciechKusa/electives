<?php
/**
 * Header
 */
?>

<!DOCTYPE html>
<html lang="pl">
	<head>
		<meta charset="UTF-8"> 
		<title>Przedmioty obieralne</title>
		<meta name="author" content="Wojciech Kusa" />
		<meta name="description" content="Strona wykonana na projekt z kursu Bazy Danych I" />
 		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="stylesheet" href="css/bootstrap.css" type="text/css" />
		<link rel="stylesheet" href="css/navi.css" type="text/css" />
		<script src="https://code.jquery.com/jquery.js"></script>
                <script src="js/jquery.js"></script>
		<script type="text/javascript" src="./js/bootstrap.js"></script>
                <script>
                    $(document).ready(function() {
                        $(".toggle").on("change", function(e) {
                            var $inp = $(this).siblings(".select");
                            if(this.checked) {
                                $inp.show();
                            }
                            else {
                                $inp.hide();
                            }
                        });
                    });
                </script>
                <script>
                $(document).ready(function() {
                    $('#example').dataTable();
                } );
                </script>
	</head>

	<body>
	<header class="navbar-fixed-top" role="banner" style="background-color:white">
		<div class="container">
	
			<div class="masthead">
			<h3 class="text-muted">Elective subjects</h3>

<div class="container">
<?php
	// Instrukcje wyboru decydujace w jakim kontekscie zostanie pokazane  menu 

	// Sprawdzenie, czy uzytkownik lub pracownik jest zalogowany, jesli nie to kontekst menu zmienia sie na menu dla osoby niezalogowanej w serwisie
	if (!isset($_SESSION['student']) && !isset($_SESSION['staff'])&& !isset($_SESSION['admin'])) {
?>
        <div class="navbar navbar-inverse navbar-static-top" role="navigation">
          <div class="container">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="index.php">Homepage</a>
            </div>
            <div class="navbar-collapse collapse">
              <ul class="nav navbar-nav">
                <li><a href="index.php?controller=store&amp;action=courses">Courses</a></li>
                <li class="dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown">Log in<b class="caret"></b></a>
                  <ul class="dropdown-menu">
                    <li><a href="index.php?controller=student&amp;action=logIn">Student log in</a></li>
                    <li class="divider"></li>
                    <li><a href="index.php?controller=staff&amp;action=logIn">Staff log in</a></li>
                    <li class="divider"></li>
                    <li><a href="index.php?controller=admin&amp;action=logIn">Admin log in</a></li>
                  </ul>
                </li>
              </ul>
            </div>
          </div>
        </div>

      </div>
		
			</ul>
	      		</div>
<?php
}
	//Sprawdza, czy student jest zalogowany
else if(!isset($_SESSION['student']) == ''){
	
    ?>
<div class="navbar navbar-inverse navbar-static-top" role="navigation">
          <div class="container">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="index.php">Homepage</a>	
            </div>
            <div class="navbar-collapse collapse">
              <ul class="nav navbar-nav">
		<li><a href="index.php?controller=store&amp;action=courses">Courses</a></li>
		<li><a href="index.php?controller=student&amp;action=myCourses">My courses</a></li>
                <li><a href="index.php?controller=student&amp;action=aboutMe">About me</a></li>
                <li><a href="index.php?controller=student&amp;action=logOut">Log out</a></li>
              </ul>
            </div>
          </div>
        </div>

      </div>
		
			</ul>
	      		</div>
<?php } 
	// Sprawdzenie, czy jest zalogowany pracownik
else if(!isset($_SESSION['staff']) == '') { 
    ?>
<div class="navbar navbar-inverse navbar-static-top" role="navigation">
          <div class="container">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="index.php">Homepage</a>	
            </div>
            <div class="navbar-collapse collapse">
              <ul class="nav navbar-nav">
                <li><a href="index.php?controller=store&amp;action=courses">Courses</a></li>

		<li><a href="index.php?controller=staff&amp;action=aboutMe">About me</a></li>

                <li><a href="index.php?controller=staff&amp;action=logOut">Log out</a></li>
              </ul>
            </div>
          </div>
        </div>

      </div>
		
			</ul>
	      		</div>
                        
<?php } 
	// Sprawdzenie czy zalogowany jest administrator
else if(!isset($_SESSION['admin']) == '') { 
    ?>
<div class="navbar navbar-inverse navbar-static-top" role="navigation">
          <div class="container">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="index.php">Homepage</a>	
            </div>
            <div class="navbar-collapse collapse">
              <ul class="nav navbar-nav">
		<li class="dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown">Courses<b class="caret"></b></a>
                  <ul class="dropdown-menu">
                   	<li><a href="index.php?controller=store&amp;action=courses">Courses</a></li>
			<li class="divider"></li>
			<li><a href="index.php?controller=store&amp;action=addCourse">Add course</a></li>
			<li class="divider"></li>
			<li><a href="index.php?controller=store&amp;action=delCourse">Delete course</a></li>                    
                  </ul>
                </li>		
		<li><a href="index.php?controller=store&amp;action=viewUsers">Users</a></li>
		
                <li><a href="index.php?controller=staff&amp;action=logOut">Log out</a></li>
              </ul>
            </div>
          </div>
        </div>

      </div>
		
			</ul>
	      		</div>
<?php } ?>

	</header>
<br><br>
