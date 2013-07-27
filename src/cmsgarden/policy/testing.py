from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class CmsgardenpolicyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import cmsgarden.policy
        xmlconfig.file(
            'configure.zcml',
            cmsgarden.policy,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cmsgarden.policy:default')

CMSGARDEN_POLICY_FIXTURE = CmsgardenpolicyLayer()
CMSGARDEN_POLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CMSGARDEN_POLICY_FIXTURE,),
    name="CmsgardenpolicyLayer:Integration"
)
CMSGARDEN_POLICY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CMSGARDEN_POLICY_FIXTURE, z2.ZSERVER_FIXTURE),
    name="CmsgardenpolicyLayer:Functional"
)
