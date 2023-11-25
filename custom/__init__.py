from mkdocs.plugins import BasePlugin
import re


class MyCustom(BasePlugin):
    def on_nav(self, nav, config, files):
        self.nav = nav

        # load all the pages first, so the titles are correct
        for page in nav.pages:
            page.read_source(config)

        def recent_pages():
            # import ipdb; ipdb.set_trace()
            return [
                page
                for page in self.nav.pages
                if page.parent
                and page.parent.title == 'Posts'
                and "image" in page.meta
            ]

        setattr(nav, "recent_pages", recent_pages)
        return nav

    def on_page_context(self, context, page, config, nav):
        return context
