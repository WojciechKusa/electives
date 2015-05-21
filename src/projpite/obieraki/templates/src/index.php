<?php


	// init session 
	session_start();

	// define page adress 
	$site_path = realpath(dirname(__FILE__));
	define ('__SITE_PATH', $site_path);
        
	
	// include classes
	function __autoload($name){
		global $site_path;
		include $site_path."/controllers/".$name.".php";
	}


	if(isset($_GET['controller']) && isset($_GET['action'])) {
		$cntrl = $_GET['controller']."_controller";
		$action = $_GET['action'];
	} else {
		$cntrl = "store_controller";
		$action = "body";
	}


	// load controller 
	$controller = new $cntrl();

	if(isset($_GET['id'])){
		$arg = $_GET['id'];
		$controller->$action($arg);
	}
	else {
		$controller->$action();
	}

	$controller->loadView();

?>
