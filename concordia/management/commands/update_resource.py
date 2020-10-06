from django.core.management.base import BaseCommand

from ...models import Asset


class Command(BaseCommand):
    def handle(self, *, verbosity, **kwargs):
        assets = Asset.objects.filter(item__item_id="2010414646")
        for asset in assets:
            convert_resource = (
                asset.resource_url[0:37]
                + asset.download_url[66:82].replace(":", "")
                + "?sp="
                + asset.download_url[84:87]
            )
            asset.resource_url = convert_resource
            print(asset.resource_url)
            asset.save()
