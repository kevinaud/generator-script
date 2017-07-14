<?php
include_once $_SERVER['DOCUMENT_ROOT'] . "/resources/session/session.php";
require_once $_SERVER['DOCUMENT_ROOT'] . "/resources/classes/__upper__camel__case__/Action/__upper__camel__case__Action.php";
require_once $_SERVER['DOCUMENT_ROOT'] . "/resources/classes/__upper__camel__case__/View/__upper__camel__case__View.php";
require_once $_SERVER['DOCUMENT_ROOT'] . "/resources/classes/PreferencesInterface/Controller/PrefController.php";

/**
 * @author __author__
 * @dateChanged __today__
 * @changedBy __author__
 * @description __pref__name__title__ Controller
 */
class __upper__camel__case__Controller extends PrefController
{
	protected $_actionClass = '__upper__camel__case__Action';
	protected $_viewClass = '__upper__camel__case__View';
	protected $_labelProperty = '__label__prop__';
	protected $_valueProperty = '__value__prop__';
	protected $_itemsData;

	/**
	 * @author __author__
	 * @description initializes the __pref__name__lower__ data used for __pref__name__lower__ preference views
	 * @dateChanged __today__
	 * @changedBy
	 */
	protected function _initItemsData()
	{
		try {
			$this->_itemsData = __upper__camel__case__Action::get__upper__camel__case__();
		} catch (Exception $e) {
			$errorMessage = Tasks::buildErrorMessage($e, __CLASS__, __FUNCTION__);
			throw new Exception($errorMessage);
		}
	}
	
}

?>
