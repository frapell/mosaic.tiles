# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE
    PloneSandboxLayer,
)
from plone.testing import z2

import mosaic.tiles


class MosaicTilesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=mosaic.tiles)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'mosaic.tiles:default')


MOSAIC_TILES_FIXTURE = MosaicTilesLayer()


MOSAIC_TILES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MOSAIC_TILES_FIXTURE,),
    name='MosaicTilesLayer:IntegrationTesting',
)


MOSAIC_TILES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MOSAIC_TILES_FIXTURE,),
    name='MosaicTilesLayer:FunctionalTesting',
)


MOSAIC_TILES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MOSAIC_TILES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='MosaicTilesLayer:AcceptanceTesting',
)
