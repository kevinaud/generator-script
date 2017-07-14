<?php 
require_once __DIR__ .'/../../PreferencesInterface/View/PrefView.php';

/**
 * @author  __author__
 * @dateChanged __today__
 * @changedBy __author__
 *
 * @description __pref__name__title__ Preference View
 */
class __upper__camel__case__View extends PrefView
{
    protected $_template =  "settings/preferences/__camel__case__Template.html";
    protected $_itemTemplate = "settings/preferences/__camel__case__Item.html";
    
    /**
     * @override PrefView::_getFilters()
     * @author __author__
     * @return return assoc array : key - filter type, value - default value
     * @description returns the filters to display for the preference
     * @dateChanged __today__
     * @changedBy   __author__
     */
    protected function _getFilters()
    {
        return array(
            // TO-DO: select filters
            //
            // 'global-smallFilter'    =>  'all',
            // 'visible-smallFilter'   =>  'visible',
            // 'initial-smallFilter'   =>  'all'
        );
    }
}

?>
