# -*- coding: utf-8 -*-
iface = "zope.interface Interface"
rename_dict = {
    "App.interfaces IPersistentExtra": iface,
    "App.interfaces IUndoSupport": iface,
    "Products.ResourceRegistries.interfaces.settings IResourceRegistriesSettings": iface,
    "Products.ATContentTypes.tool.metadata MetadataTool": iface,
    "Products.ATContentTypes.tool.metadata MetadataSchema": iface,
    "Products.ATContentTypes.tool.metadata ElementSpec": iface,

    "Products.PloneFormGen.content.form FormFolder": iface,
    "Products.PloneFormGen.content.fields FGStringField": iface,

    "Products.PloneFormGen.validators.MaxLengthValidator MaxLengthValidator": iface,

    "Products.PloneFormGen.content.fields FGTextField": iface,
    "Products.PloneFormGen.content.fields PlainTextField": iface,

    "Products.PloneFormGen.content.fields FGDateField": iface,
    "Products.PloneFormGen.content.fields FGIntegerField": iface,

    "Products.PloneFormGen.content.fields FGLabelField": iface,
    "Products.PloneFormGen.content.fields FGRichTextField": iface,

    "Products.PloneFormGen.content.fields FGSelectionField": iface,
    "Products.PloneFormGen.content.fields FGMultiSelectField": iface,

    "Products.PloneFormGen.content.fields FGFieldsetStart": iface,
    "Products.PloneFormGen.content.fields FGFieldsetEnd": iface,

    "Products.PloneFormGen.content.fields FGBooleanField": iface,
    "Products.PloneFormGen.content.fields FGRichLabelField": iface,

    "Products.PloneFormGen.content.fields FGFileField": iface,
    "Products.PloneFormGen.content.fields HtmlTextField": iface,

    "Products.PloneFormGen.content.fields FGLinesField": iface,
    "Products.PloneFormGen.content.fields NRBooleanField": iface,

    "Products.Archetypes.BaseUnit BaseUnit": iface,

    "Products.PloneFormGen.content.formMailerAdapter FormMailerAdapter": iface,

    "Products.PloneFormGen.content.thanksPage FormThanksPage": iface,

    "Products.PloneFormGen.content.fieldset FieldsetFolder": iface,

    "Products.PloneFormGen.content.saveDataAdapter FormSaveDataAdapter": iface,
    "Products.PloneFormGen.interfaces.form IPloneFormGenForm": iface,

    "Products.ATContentTypes.interfaces.folder IATBTreeFolder": iface,
    "Products.ATContentTypes.interfaces.folder IATFolder": iface,

    "Products.ATContentTypes.tool.metadata MetadataElementPolicy": iface,
    "Products.PloneFormGen.content.formLikertField FGLikertField": iface,
    "Products.PloneFormGen.content.customScriptAdapter FormCustomScriptAdapter": iface,

    "Products.ATContentTypes.interfaces.interfaces IATContentType": iface,

    "Products.Archetypes.interfaces.referenceable IReferenceable": iface,
    "plone.app.folder.folder IATUnifiedFolder": iface,
    "archetypes.multilingual.interfaces IArchetypesTranslatable": iface,

    "Products.Archetypes.interfaces.base IBaseContent": iface,
    "Products.Archetypes.interfaces.base IBaseFolder": iface,
    "Products.Archetypes.interfaces.base IBaseObject": iface,

    "plone.app.imaging.interfaces IBaseObject": iface,

    "archetypes.schemaextender.interfaces IExtensible": iface,
    "Products.Archetypes.interfaces.metadata IExtensibleMetadata": iface,
    "Products.PloneFormGen.interfaces.thanksPage IPloneFormGenThanksPage": iface,

}
# I have seen zodbverify on Python 2 complain with a warning about various webdav.interfaces factories.
# Might be okay to keep them, because webdav will return in Zope 4.3.
# But for zodbverify on Python 3 it is a real error, even though the instance starts fine.
# It may be wise to rename them after all.
try:
    import webdav
except ImportError:
    # IFTPAccess is not there anyway in the new webdav:
    rename_dict["webdav.interfaces IFTPAccess"] = iface
    rename_dict["OFS.interfaces IFTPAccess"] = iface

    # The next two inherit from IWriteLock, so seems a logical replacement,
    # but that is only available since Zope 4.
    try:
        from OFS.interfaces import IWriteLock

        writelock = "OFS.interfaces IWriteLock"
    except ImportError:
        writelock = iface
    rename_dict.update(
        {
            "webdav.interfaces IDAVCollection": writelock,
            "webdav.interfaces IDAVResource": writelock,
        }
    )
else:
    # webdav is back in Zope 4.3.
    # See https://github.com/zestsoftware/zest.zodbupdate/issues/1
    try:
        from OFS.EtagSupport import EtagBaseInterface
        rename_dict["webdav.EtagSupport EtagBaseInterface"] = "OFS.EtagSupport EtagBaseInterface"
    except ImportError:
        rename_dict["webdav.EtagSupport EtagBaseInterface"] = iface
    # IFTPAccess is back in webdav.
    # Well, that depends on wheter you have webdav from Zope or from ZServer...
    # See https://github.com/zestsoftware/zest.zodbupdate/pull/2#issuecomment-663647294
    try:
        from webdav.interfaces import IFTPAccess
        rename_dict["OFS.interfaces IFTPAccess"] = "webdav.interfaces IFTPAccess"
    except ImportError:
        rename_dict["OFS.interfaces IFTPAccess"] = iface
        rename_dict["webdav.interfaces IFTPAccess"] = iface
