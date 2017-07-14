<?php
include_once $_SERVER['DOCUMENT_ROOT'] . "/resources/session/session.php";
include_Once $_SERVER['DOCUMENT_ROOT'] . "/resources/classes/__upper__camel__case__/Controller/__upper__camel__case__Controller.php";

$__camel__case__Controller = new __upper__camel__case__Controller();
$action = $_POST['action'];
switch($action)
{
    case 'save':
        Tasks::jsonResponse($__camel__case__Controller->save($_POST));
    break;
    case 'getView':
        Tasks::jsonResponse($__camel__case__Controller->getView());
    break;
    case 'getItemView':
        Tasks::jsonResponse($__camel__case__Controller->getItemView($_POST['__value__prop__']));
    break;
}
?>
