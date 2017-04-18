from tethys_sdk.base import TethysAppBase, url_map_maker


class Arcgis(TethysAppBase):
    """
    Tethys app class for arcgis.
    """

    name = 'arcgis'
    index = 'arcgis:home'
    icon = 'arcgis/images/icon.gif'
    package = 'arcgis'
    root_url = 'arcgis'
    color = '#1abc9c'
    description = 'arcgis map'
    tags = '"arcgis"'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='arcgis',
                           controller='arcgis.controllers.home'),
		   UrlMap(name='map',
                       	   url='arcgis/map',
                           controller='arcgis.controllers.map'),
        )

        return url_maps
