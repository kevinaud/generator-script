<?php
include_once $_SERVER['DOCUMENT_ROOT'] . "resources/session/session.php";

/**
 * @author __author__
 * @dateChanged __today__ 
 * @changedBy __author__
 * @description __pref__name__title__ Preference DAO
 */
class __upper__camel__case__DAO 
{

    /**
     * @author __author__
     * 
     * @description gets __pref__name__lower__ preference data from database
     * @dateChanged __today__ 
     * @changedBy __author__
     * 
     */
    public  static function get__upper__camel__case__() 
    {
        try {
            $qry = "
__select__qry__
            ";

            $params = array();

            $__camel__case__ = dbQuery($qry, $params, PDO::FETCH_ASSOC);

            if ($__camel__case__ === false) {
                throw new Exception('Unable to pull __pref__name__lower__ data.');
            }
            
            return $__camel__case__;

        } catch (Exception $e) {
            $errorMessage = Tasks::buildErrorMessage($e, __CLASS__, __FUNCTION__);
            throw new Exception($errorMessage);
        }
    }

}
?>
