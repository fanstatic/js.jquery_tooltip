from fanstatic import Library, ResourceInclusion

from js.jquery import jquery

library = Library('jquery_tooltip', 'resources')

jquery_tooltip_css = ResourceInclusion(library, 'jquery.tooltip.css')

jquery_tooltip = ResourceInclusion(library, 'jquery.tooltip.js',
    minified='jquery.tooltip.min.js',
    depends=[jquery, jquery_tooltip_css])

