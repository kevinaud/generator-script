<?php
include_once $_SERVER['DOCUMENT_ROOT'] . "/resources/session/session.php";
include_once $_SERVER['DOCUMENT_ROOT'] . "/resources/classes/__upper__camel__case__/DAO/__upper__camel__case__DAO.php";
require_once __DIR__ . '/../../Base.php';

/**
 * @author __author__
 * @dateChanged __today__
 * @changedBy __author__ 
 *
 * @description Used to create, update, delete, and retrieve __pref__name__title__ preference data
 */
class __upper__camel__case__Action extends Base
{
__fields__public__attributes__
    protected $___camel__case__DAO;
    
    /**
     * @author __author__
     * @return array(
__commented__out__fields__
     * )
     *
     * @description gets all __pref__name__lower__ 
     * @dateChanged __today__
     * @changedBy   __author__
     */
    public static function get__upper__camel__case__()
    {
        try {
            $__camel__case__ = __upper__camel__case__DAO::get__upper__camel__case__();
            return $__camel__case__;
        } catch (Exception $e) {
            $errorMessage = Tasks::buildErrorMessage($e, __CLASS__, __FUNCTION__);
            throw new Exception($errorMessage);
        }
    }
    
    /**
     * @override Base::init()
     * @author  __author__
     * @throws Exception
     * @description initializes DAO
     * @dateChanged __today__
     * @changedBy __author__
     */
    protected function init()
    {
        try {
            $this->___camel__case__DAO = new __upper__camel__case__DAO();
        } catch(Exception $e) {
            $errorMessage = Tasks::buildErrorMessage($e, __CLASS__, __FUNCTION__);
            throw new Exception($errorMessage);
        }
    }

    /**
     * @override Base::getLoggableFields()
     * @author __author__
     * @return array[string] $loggableDBFields
     * @description returns an array of database fields to log changes for
     * @dateChanged __today__
     * @changedBy __author__
     */
    protected function getLoggableFields()
    {
        return __loggable__fields__
    }

    /**
     * @override Base::getDBFields()
     * @author __author__
     * @return array[string] $dbFields
     * @description returns an array of database fields for the class
     * @dateChanged __today__
     * @changedBy __author__
     */
    protected static function getDBFields()
    {
        return __db__fields__array__
    }

    /**
     * @override Base::getPrimaryKey()
     * @author  __author__
     * @return  string $dbKey
     * @description returns the name of the databse table primary key
     * @dateChanged __today__
     * @changedBy __author__
     */
    protected function getPrimaryKey()
    {
        return "__value__prop__";
    }

    /**
     * @override Base::geTable()
     * @author __author__
     * @return string $tableName
     * @description returns the name of the database table
     * @dateChanged __today__
     * @changedBy __author__
     */
    protected function getTable()
    {
        return "__table__";
    }

    /**
     * @override Base::preSaveCallback()
     * @author __author__
     * @return boolean 
     * @description determines wether or not saving object is permitted
     * @dateChanged __today__
     * @changedBy __author__
     */
    protected function preSaveCallback()
    {
        try {
            $response = true;

            /**
             * TO DO: IMPLEMENT VALIDATION
             */

            return $response;
        } catch (Exception $e) {
            $errorMessage = Tasks::buildErrorMessage($e, __CLASS__, __FUNCTION__);
            throw new Exception($errorMessage);
        }

    }

    /**
     * @override Base::postSaveCallback()
     * @author __author__
     * @return boolean
     * @description determines wether or not saving object is permitted
     * @dateChanged __today__
     * @changedBy __author__
     */
    protected function postSaveCallback()
    {

        /**
         * TO DO: IMPLEMENT VALIDATION
         */

        return true;
    }	

}
?>
