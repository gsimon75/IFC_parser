import sys

from ClassRegistry import ifc_class, ifc_abstract_class
from IfcBase import IfcEntity, BOOLEAN, REAL, BINARY, INTEGER, NUMBER, STRING, LOGICAL
from Misc import parse_uuid

reload(sys)
sys.setdefaultencoding('UTF8')


@ifc_class
class IfcStrippedOptional(BOOLEAN):
    pass


@ifc_class
class IfcAbsorbedDoseMeasure(REAL):
    pass


@ifc_class
class IfcAccelerationMeasure(REAL):
    pass


@ifc_class
class IfcAmountOfSubstanceMeasure(REAL):
    pass


@ifc_class
class IfcAngularVelocityMeasure(REAL):
    pass


@ifc_class
class IfcAreaDensityMeasure(REAL):
    pass


@ifc_class
class IfcAreaMeasure(REAL):
    pass


@ifc_class
class IfcBinary(BINARY):
    pass


@ifc_class
class IfcBoolean(BOOLEAN):
    pass


@ifc_class
class IfcCardinalPointReference(INTEGER):
    pass


@ifc_class
class IfcContextDependentMeasure(REAL):
    pass


@ifc_class
class IfcCountMeasure(NUMBER):
    pass


@ifc_class
class IfcCurvatureMeasure(REAL):
    pass


@ifc_class
class IfcDate(STRING):
    pass


@ifc_class
class IfcDateTime(STRING):
    pass


@ifc_class
class IfcDayInMonthNumber(INTEGER):
    pass


@ifc_class
class IfcDayInWeekNumber(INTEGER):
    pass


@ifc_class
class IfcDescriptiveMeasure(STRING):
    pass


@ifc_class
class IfcDimensionCount(INTEGER):
    pass


@ifc_class
class IfcDoseEquivalentMeasure(REAL):
    pass


@ifc_class
class IfcDuration(STRING):
    pass


@ifc_class
class IfcDynamicViscosityMeasure(REAL):
    pass


@ifc_class
class IfcElectricCapacitanceMeasure(REAL):
    pass


@ifc_class
class IfcElectricChargeMeasure(REAL):
    pass


@ifc_class
class IfcElectricConductanceMeasure(REAL):
    pass


@ifc_class
class IfcElectricCurrentMeasure(REAL):
    pass


@ifc_class
class IfcElectricResistanceMeasure(REAL):
    pass


@ifc_class
class IfcElectricVoltageMeasure(REAL):
    pass


@ifc_class
class IfcEnergyMeasure(REAL):
    pass


@ifc_class
class IfcFontStyle(STRING):
    pass


@ifc_class
class IfcFontVariant(STRING):
    pass


@ifc_class
class IfcFontWeight(STRING):
    pass


@ifc_class
class IfcForceMeasure(REAL):
    pass


@ifc_class
class IfcFrequencyMeasure(REAL):
    pass


@ifc_class
class IfcGloballyUniqueId(STRING):
    pass


@ifc_class
class IfcHeatFluxDensityMeasure(REAL):
    pass


@ifc_class
class IfcHeatingValueMeasure(REAL):
    pass


@ifc_class
class IfcIdentifier(STRING):
    pass


@ifc_class
class IfcIlluminanceMeasure(REAL):
    pass


@ifc_class
class IfcInductanceMeasure(REAL):
    pass


@ifc_class
class IfcInteger(INTEGER):
    pass


@ifc_class
class IfcIntegerCountRateMeasure(INTEGER):
    pass


@ifc_class
class IfcIonConcentrationMeasure(REAL):
    pass


@ifc_class
class IfcIsothermalMoistureCapacityMeasure(REAL):
    pass


@ifc_class
class IfcKinematicViscosityMeasure(REAL):
    pass


@ifc_class
class IfcLabel(STRING):
    pass


@ifc_class
class IfcLanguageId(IfcIdentifier):
    pass


@ifc_class
class IfcLengthMeasure(REAL):
    pass


@ifc_class
class IfcLinearForceMeasure(REAL):
    pass


@ifc_class
class IfcLinearMomentMeasure(REAL):
    pass


@ifc_class
class IfcLinearStiffnessMeasure(REAL):
    pass


@ifc_class
class IfcLinearVelocityMeasure(REAL):
    pass


@ifc_class
class IfcLogical(LOGICAL):
    pass


@ifc_class
class IfcLuminousFluxMeasure(REAL):
    pass


@ifc_class
class IfcLuminousIntensityDistributionMeasure(REAL):
    pass


@ifc_class
class IfcLuminousIntensityMeasure(REAL):
    pass


@ifc_class
class IfcMagneticFluxDensityMeasure(REAL):
    pass


@ifc_class
class IfcMagneticFluxMeasure(REAL):
    pass


@ifc_class
class IfcMassDensityMeasure(REAL):
    pass


@ifc_class
class IfcMassFlowRateMeasure(REAL):
    pass


@ifc_class
class IfcMassMeasure(REAL):
    pass


@ifc_class
class IfcMassPerLengthMeasure(REAL):
    pass


@ifc_class
class IfcModulusOfElasticityMeasure(REAL):
    pass


@ifc_class
class IfcModulusOfLinearSubgradeReactionMeasure(REAL):
    pass


@ifc_class
class IfcModulusOfRotationalSubgradeReactionMeasure(REAL):
    pass


@ifc_class
class IfcModulusOfSubgradeReactionMeasure(REAL):
    pass


@ifc_class
class IfcMoistureDiffusivityMeasure(REAL):
    pass


@ifc_class
class IfcMolecularWeightMeasure(REAL):
    pass


@ifc_class
class IfcMomentOfInertiaMeasure(REAL):
    pass


@ifc_class
class IfcMonetaryMeasure(REAL):
    pass


@ifc_class
class IfcMonthInYearNumber(INTEGER):
    pass


@ifc_class
class IfcNonNegativeLengthMeasure(IfcLengthMeasure):
    pass


@ifc_class
class IfcNumericMeasure(NUMBER):
    pass


@ifc_class
class IfcPHMeasure(REAL):
    pass


@ifc_class
class IfcParameterValue(REAL):
    pass


@ifc_class
class IfcPlanarForceMeasure(REAL):
    pass


@ifc_class
class IfcPlaneAngleMeasure(REAL):
    pass


@ifc_class
class IfcPositiveInteger(IfcInteger):
    pass


@ifc_class
class IfcPositiveLengthMeasure(IfcLengthMeasure):
    pass


@ifc_class
class IfcPositivePlaneAngleMeasure(IfcPlaneAngleMeasure):
    pass


@ifc_class
class IfcPowerMeasure(REAL):
    pass


@ifc_class
class IfcPresentableText(STRING):
    pass


@ifc_class
class IfcPressureMeasure(REAL):
    pass


@ifc_class
class IfcRadioActivityMeasure(REAL):
    pass


@ifc_class
class IfcRatioMeasure(REAL):
    pass


@ifc_class
class IfcReal(REAL):
    pass


@ifc_class
class IfcRotationalFrequencyMeasure(REAL):
    pass


@ifc_class
class IfcRotationalMassMeasure(REAL):
    pass


@ifc_class
class IfcRotationalStiffnessMeasure(REAL):
    pass


@ifc_class
class IfcSectionModulusMeasure(REAL):
    pass


@ifc_class
class IfcSectionalAreaIntegralMeasure(REAL):
    pass


@ifc_class
class IfcShearModulusMeasure(REAL):
    pass


@ifc_class
class IfcSolidAngleMeasure(REAL):
    pass


@ifc_class
class IfcSoundPowerLevelMeasure(REAL):
    pass


@ifc_class
class IfcSoundPowerMeasure(REAL):
    pass


@ifc_class
class IfcSoundPressureLevelMeasure(REAL):
    pass


@ifc_class
class IfcSoundPressureMeasure(REAL):
    pass


@ifc_class
class IfcSpecificHeatCapacityMeasure(REAL):
    pass


@ifc_class
class IfcSpecularExponent(REAL):
    pass


@ifc_class
class IfcSpecularRoughness(REAL):
    pass


@ifc_class
class IfcTemperatureGradientMeasure(REAL):
    pass


@ifc_class
class IfcTemperatureRateOfChangeMeasure(REAL):
    pass


@ifc_class
class IfcText(STRING):
    pass


@ifc_class
class IfcTextAlignment(STRING):
    pass


@ifc_class
class IfcTextDecoration(STRING):
    pass


@ifc_class
class IfcTextFontName(STRING):
    pass


@ifc_class
class IfcTextTransformation(STRING):
    pass


@ifc_class
class IfcThermalAdmittanceMeasure(REAL):
    pass


@ifc_class
class IfcThermalConductivityMeasure(REAL):
    pass


@ifc_class
class IfcThermalExpansionCoefficientMeasure(REAL):
    pass


@ifc_class
class IfcThermalResistanceMeasure(REAL):
    pass


@ifc_class
class IfcThermalTransmittanceMeasure(REAL):
    pass


@ifc_class
class IfcThermodynamicTemperatureMeasure(REAL):
    pass


@ifc_class
class IfcTime(STRING):
    pass


@ifc_class
class IfcTimeMeasure(REAL):
    pass


@ifc_class
class IfcTimeStamp(INTEGER):
    pass


@ifc_class
class IfcTorqueMeasure(REAL):
    pass


@ifc_class
class IfcURIReference(STRING):
    pass


@ifc_class
class IfcVaporPermeabilityMeasure(REAL):
    pass


@ifc_class
class IfcVolumeMeasure(REAL):
    pass


@ifc_class
class IfcVolumetricFlowRateMeasure(REAL):
    pass


@ifc_class
class IfcWarpingConstantMeasure(REAL):
    pass


@ifc_class
class IfcWarpingMomentMeasure(REAL):
    pass


@ifc_class
class IfcBoxAlignment(IfcLabel):
    pass


@ifc_class
class IfcNormalisedRatioMeasure(IfcRatioMeasure):
    pass


@ifc_class
class IfcPositiveRatioMeasure(IfcRatioMeasure):
    pass


@ifc_class
class IfcActorRole(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Role = args.pop()
        self.UserDefinedRole = args.pop()
        self.Description = args.pop()

    def __str__(self):
        return "{sup}:Role:{Role}:UserDefinedRole:{UserDefinedRole}:Description:{Description}".format(
            sup=IfcEntity.__str__(self),
            Role=self.Role,
            UserDefinedRole=self.UserDefinedRole,
            Description=self.Description,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Role': self.Role, 'UserDefinedRole': self.UserDefinedRole, 'Description': self.Description}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcAddress(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Purpose = args.pop()
        self.Description = args.pop()
        self.UserDefinedPurpose = args.pop()

    def __str__(self):
        return "{sup}:Purpose:{Purpose}:Description:{Description}:UserDefinedPurpose:{UserDefinedPurpose}".format(
            sup=IfcEntity.__str__(self),
            Purpose=self.Purpose,
            Description=self.Description,
            UserDefinedPurpose=self.UserDefinedPurpose,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Purpose': self.Purpose, 'Description': self.Description,
                 'UserDefinedPurpose': self.UserDefinedPurpose}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcApplication(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.ApplicationDeveloper = args.pop()
        self.Version = args.pop()
        self.ApplicationFullName = args.pop()
        self.ApplicationIdentifier = args.pop()

    def __str__(self):
        return "{sup}:ApplicationDeveloper:{ApplicationDeveloper}:Version:{Version}:ApplicationFullName:{ApplicationFullName}:ApplicationIdentifier:{ApplicationIdentifier}".format(
            sup=IfcEntity.__str__(self),
            ApplicationDeveloper=self.ApplicationDeveloper,
            Version=self.Version,
            ApplicationFullName=self.ApplicationFullName,
            ApplicationIdentifier=self.ApplicationIdentifier,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'ApplicationDeveloper': self.ApplicationDeveloper, 'Version': self.Version,
                 'ApplicationFullName': self.ApplicationFullName, 'ApplicationIdentifier': self.ApplicationIdentifier}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAppliedValue(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Name = args.pop()
        self.Description = args.pop()
        self.AppliedValue = args.pop()
        self.UnitBasis = args.pop()
        self.ApplicableDate = args.pop()
        self.FixedUntilDate = args.pop()
        self.Category = args.pop()
        self.Condition = args.pop()
        self.ArithmeticOperator = args.pop()
        self.Components = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:Description:{Description}:AppliedValue:{AppliedValue}:UnitBasis:{UnitBasis}:ApplicableDate:{ApplicableDate}:FixedUntilDate:{FixedUntilDate}:Category:{Category}:Condition:{Condition}:ArithmeticOperator:{ArithmeticOperator}:Components:{Components}".format(
            sup=IfcEntity.__str__(self),
            Name=self.Name,
            Description=self.Description,
            AppliedValue=self.AppliedValue,
            UnitBasis=self.UnitBasis,
            ApplicableDate=self.ApplicableDate,
            FixedUntilDate=self.FixedUntilDate,
            Category=self.Category,
            Condition=self.Condition,
            ArithmeticOperator=self.ArithmeticOperator,
            Components=self.Components,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Name': self.Name, 'Description': self.Description, 'AppliedValue': self.AppliedValue,
                 'UnitBasis': self.UnitBasis, 'ApplicableDate': self.ApplicableDate,
                 'FixedUntilDate': self.FixedUntilDate, 'Category': self.Category, 'Condition': self.Condition,
                 'ArithmeticOperator': self.ArithmeticOperator, 'Components': self.Components}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcApproval(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Identifier = args.pop()
        self.Name = args.pop()
        self.Description = args.pop()
        self.TimeOfApproval = args.pop()
        self.Status = args.pop()
        self.Level = args.pop()
        self.Qualifier = args.pop()
        self.RequestingApproval = args.pop()
        self.GivingApproval = args.pop()

    def __str__(self):
        return "{sup}:Identifier:{Identifier}:Name:{Name}:Description:{Description}:TimeOfApproval:{TimeOfApproval}:Status:{Status}:Level:{Level}:Qualifier:{Qualifier}:RequestingApproval:{RequestingApproval}:GivingApproval:{GivingApproval}".format(
            sup=IfcEntity.__str__(self),
            Identifier=self.Identifier,
            Name=self.Name,
            Description=self.Description,
            TimeOfApproval=self.TimeOfApproval,
            Status=self.Status,
            Level=self.Level,
            Qualifier=self.Qualifier,
            RequestingApproval=self.RequestingApproval,
            GivingApproval=self.GivingApproval,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Identifier': self.Identifier, 'Name': self.Name, 'Description': self.Description,
                 'TimeOfApproval': self.TimeOfApproval, 'Status': self.Status, 'Level': self.Level,
                 'Qualifier': self.Qualifier, 'RequestingApproval': self.RequestingApproval,
                 'GivingApproval': self.GivingApproval}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcBoundaryCondition(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Name = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}".format(
            sup=IfcEntity.__str__(self),
            Name=self.Name,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Name': self.Name}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBoundaryEdgeCondition(IfcBoundaryCondition):
    def __init__(self, rtype, args):
        IfcBoundaryCondition.__init__(self, rtype, args)
        self.TranslationalStiffnessByLengthX = args.pop()
        self.TranslationalStiffnessByLengthY = args.pop()
        self.TranslationalStiffnessByLengthZ = args.pop()
        self.RotationalStiffnessByLengthX = args.pop()
        self.RotationalStiffnessByLengthY = args.pop()
        self.RotationalStiffnessByLengthZ = args.pop()

    def __str__(self):
        return "{sup}:TranslationalStiffnessByLengthX:{TranslationalStiffnessByLengthX}:TranslationalStiffnessByLengthY:{TranslationalStiffnessByLengthY}:TranslationalStiffnessByLengthZ:{TranslationalStiffnessByLengthZ}:RotationalStiffnessByLengthX:{RotationalStiffnessByLengthX}:RotationalStiffnessByLengthY:{RotationalStiffnessByLengthY}:RotationalStiffnessByLengthZ:{RotationalStiffnessByLengthZ}".format(
            sup=IfcBoundaryCondition.__str__(self),
            TranslationalStiffnessByLengthX=self.TranslationalStiffnessByLengthX,
            TranslationalStiffnessByLengthY=self.TranslationalStiffnessByLengthY,
            TranslationalStiffnessByLengthZ=self.TranslationalStiffnessByLengthZ,
            RotationalStiffnessByLengthX=self.RotationalStiffnessByLengthX,
            RotationalStiffnessByLengthY=self.RotationalStiffnessByLengthY,
            RotationalStiffnessByLengthZ=self.RotationalStiffnessByLengthZ,
        )

    def __json__(self):
        sup = IfcBoundaryCondition.__json__(self)
        attrs = {'TranslationalStiffnessByLengthX': self.TranslationalStiffnessByLengthX,
                 'TranslationalStiffnessByLengthY': self.TranslationalStiffnessByLengthY,
                 'TranslationalStiffnessByLengthZ': self.TranslationalStiffnessByLengthZ,
                 'RotationalStiffnessByLengthX': self.RotationalStiffnessByLengthX,
                 'RotationalStiffnessByLengthY': self.RotationalStiffnessByLengthY,
                 'RotationalStiffnessByLengthZ': self.RotationalStiffnessByLengthZ}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBoundaryFaceCondition(IfcBoundaryCondition):
    def __init__(self, rtype, args):
        IfcBoundaryCondition.__init__(self, rtype, args)
        self.TranslationalStiffnessByAreaX = args.pop()
        self.TranslationalStiffnessByAreaY = args.pop()
        self.TranslationalStiffnessByAreaZ = args.pop()

    def __str__(self):
        return "{sup}:TranslationalStiffnessByAreaX:{TranslationalStiffnessByAreaX}:TranslationalStiffnessByAreaY:{TranslationalStiffnessByAreaY}:TranslationalStiffnessByAreaZ:{TranslationalStiffnessByAreaZ}".format(
            sup=IfcBoundaryCondition.__str__(self),
            TranslationalStiffnessByAreaX=self.TranslationalStiffnessByAreaX,
            TranslationalStiffnessByAreaY=self.TranslationalStiffnessByAreaY,
            TranslationalStiffnessByAreaZ=self.TranslationalStiffnessByAreaZ,
        )

    def __json__(self):
        sup = IfcBoundaryCondition.__json__(self)
        attrs = {'TranslationalStiffnessByAreaX': self.TranslationalStiffnessByAreaX,
                 'TranslationalStiffnessByAreaY': self.TranslationalStiffnessByAreaY,
                 'TranslationalStiffnessByAreaZ': self.TranslationalStiffnessByAreaZ}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBoundaryNodeCondition(IfcBoundaryCondition):
    def __init__(self, rtype, args):
        IfcBoundaryCondition.__init__(self, rtype, args)
        self.TranslationalStiffnessX = args.pop()
        self.TranslationalStiffnessY = args.pop()
        self.TranslationalStiffnessZ = args.pop()
        self.RotationalStiffnessX = args.pop()
        self.RotationalStiffnessY = args.pop()
        self.RotationalStiffnessZ = args.pop()

    def __str__(self):
        return "{sup}:TranslationalStiffnessX:{TranslationalStiffnessX}:TranslationalStiffnessY:{TranslationalStiffnessY}:TranslationalStiffnessZ:{TranslationalStiffnessZ}:RotationalStiffnessX:{RotationalStiffnessX}:RotationalStiffnessY:{RotationalStiffnessY}:RotationalStiffnessZ:{RotationalStiffnessZ}".format(
            sup=IfcBoundaryCondition.__str__(self),
            TranslationalStiffnessX=self.TranslationalStiffnessX,
            TranslationalStiffnessY=self.TranslationalStiffnessY,
            TranslationalStiffnessZ=self.TranslationalStiffnessZ,
            RotationalStiffnessX=self.RotationalStiffnessX,
            RotationalStiffnessY=self.RotationalStiffnessY,
            RotationalStiffnessZ=self.RotationalStiffnessZ,
        )

    def __json__(self):
        sup = IfcBoundaryCondition.__json__(self)
        attrs = {'TranslationalStiffnessX': self.TranslationalStiffnessX,
                 'TranslationalStiffnessY': self.TranslationalStiffnessY,
                 'TranslationalStiffnessZ': self.TranslationalStiffnessZ,
                 'RotationalStiffnessX': self.RotationalStiffnessX, 'RotationalStiffnessY': self.RotationalStiffnessY,
                 'RotationalStiffnessZ': self.RotationalStiffnessZ}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBoundaryNodeConditionWarping(IfcBoundaryNodeCondition):
    def __init__(self, rtype, args):
        IfcBoundaryNodeCondition.__init__(self, rtype, args)
        self.WarpingStiffness = args.pop()

    def __str__(self):
        return "{sup}:WarpingStiffness:{WarpingStiffness}".format(
            sup=IfcBoundaryNodeCondition.__str__(self),
            WarpingStiffness=self.WarpingStiffness,
        )

    def __json__(self):
        sup = IfcBoundaryNodeCondition.__json__(self)
        attrs = {'WarpingStiffness': self.WarpingStiffness}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcConnectionGeometry(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcEntity.__str__(self),
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcConnectionPointGeometry(IfcConnectionGeometry):
    def __init__(self, rtype, args):
        IfcConnectionGeometry.__init__(self, rtype, args)
        self.PointOnRelatingElement = args.pop()
        self.PointOnRelatedElement = args.pop()

    def __str__(self):
        return "{sup}:PointOnRelatingElement:{PointOnRelatingElement}:PointOnRelatedElement:{PointOnRelatedElement}".format(
            sup=IfcConnectionGeometry.__str__(self),
            PointOnRelatingElement=self.PointOnRelatingElement,
            PointOnRelatedElement=self.PointOnRelatedElement,
        )

    def __json__(self):
        sup = IfcConnectionGeometry.__json__(self)
        attrs = {'PointOnRelatingElement': self.PointOnRelatingElement,
                 'PointOnRelatedElement': self.PointOnRelatedElement}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcConnectionSurfaceGeometry(IfcConnectionGeometry):
    def __init__(self, rtype, args):
        IfcConnectionGeometry.__init__(self, rtype, args)
        self.SurfaceOnRelatingElement = args.pop()
        self.SurfaceOnRelatedElement = args.pop()

    def __str__(self):
        return "{sup}:SurfaceOnRelatingElement:{SurfaceOnRelatingElement}:SurfaceOnRelatedElement:{SurfaceOnRelatedElement}".format(
            sup=IfcConnectionGeometry.__str__(self),
            SurfaceOnRelatingElement=self.SurfaceOnRelatingElement,
            SurfaceOnRelatedElement=self.SurfaceOnRelatedElement,
        )

    def __json__(self):
        sup = IfcConnectionGeometry.__json__(self)
        attrs = {'SurfaceOnRelatingElement': self.SurfaceOnRelatingElement,
                 'SurfaceOnRelatedElement': self.SurfaceOnRelatedElement}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcConnectionVolumeGeometry(IfcConnectionGeometry):
    def __init__(self, rtype, args):
        IfcConnectionGeometry.__init__(self, rtype, args)
        self.VolumeOnRelatingElement = args.pop()
        self.VolumeOnRelatedElement = args.pop()

    def __str__(self):
        return "{sup}:VolumeOnRelatingElement:{VolumeOnRelatingElement}:VolumeOnRelatedElement:{VolumeOnRelatedElement}".format(
            sup=IfcConnectionGeometry.__str__(self),
            VolumeOnRelatingElement=self.VolumeOnRelatingElement,
            VolumeOnRelatedElement=self.VolumeOnRelatedElement,
        )

    def __json__(self):
        sup = IfcConnectionGeometry.__json__(self)
        attrs = {'VolumeOnRelatingElement': self.VolumeOnRelatingElement,
                 'VolumeOnRelatedElement': self.VolumeOnRelatedElement}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcConstraint(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Name = args.pop()
        self.Description = args.pop()
        self.ConstraintGrade = args.pop()
        self.ConstraintSource = args.pop()
        self.CreatingActor = args.pop()
        self.CreationTime = args.pop()
        self.UserDefinedGrade = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:Description:{Description}:ConstraintGrade:{ConstraintGrade}:ConstraintSource:{ConstraintSource}:CreatingActor:{CreatingActor}:CreationTime:{CreationTime}:UserDefinedGrade:{UserDefinedGrade}".format(
            sup=IfcEntity.__str__(self),
            Name=self.Name,
            Description=self.Description,
            ConstraintGrade=self.ConstraintGrade,
            ConstraintSource=self.ConstraintSource,
            CreatingActor=self.CreatingActor,
            CreationTime=self.CreationTime,
            UserDefinedGrade=self.UserDefinedGrade,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Name': self.Name, 'Description': self.Description, 'ConstraintGrade': self.ConstraintGrade,
                 'ConstraintSource': self.ConstraintSource, 'CreatingActor': self.CreatingActor,
                 'CreationTime': self.CreationTime, 'UserDefinedGrade': self.UserDefinedGrade}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcCoordinateOperation(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.SourceCRS = args.pop()
        self.TargetCRS = args.pop()

    def __str__(self):
        return "{sup}:SourceCRS:{SourceCRS}:TargetCRS:{TargetCRS}".format(
            sup=IfcEntity.__str__(self),
            SourceCRS=self.SourceCRS,
            TargetCRS=self.TargetCRS,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'SourceCRS': self.SourceCRS, 'TargetCRS': self.TargetCRS}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcCoordinateReferenceSystem(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Name = args.pop()
        self.Description = args.pop()
        self.GeodeticDatum = args.pop()
        self.VerticalDatum = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:Description:{Description}:GeodeticDatum:{GeodeticDatum}:VerticalDatum:{VerticalDatum}".format(
            sup=IfcEntity.__str__(self),
            Name=self.Name,
            Description=self.Description,
            GeodeticDatum=self.GeodeticDatum,
            VerticalDatum=self.VerticalDatum,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Name': self.Name, 'Description': self.Description, 'GeodeticDatum': self.GeodeticDatum,
                 'VerticalDatum': self.VerticalDatum}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCostValue(IfcAppliedValue):
    def __init__(self, rtype, args):
        IfcAppliedValue.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcAppliedValue.__str__(self),
        )

    def __json__(self):
        sup = IfcAppliedValue.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDerivedUnit(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Elements = args.pop()
        self.UnitType = args.pop()
        self.UserDefinedType = args.pop()

    def __str__(self):
        return "{sup}:Elements:{Elements}:UnitType:{UnitType}:UserDefinedType:{UserDefinedType}".format(
            sup=IfcEntity.__str__(self),
            Elements=self.Elements,
            UnitType=self.UnitType,
            UserDefinedType=self.UserDefinedType,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Elements': self.Elements, 'UnitType': self.UnitType, 'UserDefinedType': self.UserDefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDerivedUnitElement(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Unit = args.pop()
        self.Exponent = args.pop()

    def __str__(self):
        return "{sup}:Unit:{Unit}:Exponent:{Exponent}".format(
            sup=IfcEntity.__str__(self),
            Unit=self.Unit,
            Exponent=self.Exponent,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Unit': self.Unit, 'Exponent': self.Exponent}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDimensionalExponents(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.LengthExponent = args.pop()
        self.MassExponent = args.pop()
        self.TimeExponent = args.pop()
        self.ElectricCurrentExponent = args.pop()
        self.ThermodynamicTemperatureExponent = args.pop()
        self.AmountOfSubstanceExponent = args.pop()
        self.LuminousIntensityExponent = args.pop()

    def __str__(self):
        return "{sup}:LengthExponent:{LengthExponent}:MassExponent:{MassExponent}:TimeExponent:{TimeExponent}:ElectricCurrentExponent:{ElectricCurrentExponent}:ThermodynamicTemperatureExponent:{ThermodynamicTemperatureExponent}:AmountOfSubstanceExponent:{AmountOfSubstanceExponent}:LuminousIntensityExponent:{LuminousIntensityExponent}".format(
            sup=IfcEntity.__str__(self),
            LengthExponent=self.LengthExponent,
            MassExponent=self.MassExponent,
            TimeExponent=self.TimeExponent,
            ElectricCurrentExponent=self.ElectricCurrentExponent,
            ThermodynamicTemperatureExponent=self.ThermodynamicTemperatureExponent,
            AmountOfSubstanceExponent=self.AmountOfSubstanceExponent,
            LuminousIntensityExponent=self.LuminousIntensityExponent,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'LengthExponent': self.LengthExponent, 'MassExponent': self.MassExponent,
                 'TimeExponent': self.TimeExponent, 'ElectricCurrentExponent': self.ElectricCurrentExponent,
                 'ThermodynamicTemperatureExponent': self.ThermodynamicTemperatureExponent,
                 'AmountOfSubstanceExponent': self.AmountOfSubstanceExponent,
                 'LuminousIntensityExponent': self.LuminousIntensityExponent}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcExternalInformation(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcEntity.__str__(self),
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcExternalReference(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Location = args.pop()
        self.Identification = args.pop()
        self.Name = args.pop()

    def __str__(self):
        return "{sup}:Location:{Location}:Identification:{Identification}:Name:{Name}".format(
            sup=IfcEntity.__str__(self),
            Location=self.Location,
            Identification=self.Identification,
            Name=self.Name,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Location': self.Location, 'Identification': self.Identification, 'Name': self.Name}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcExternallyDefinedHatchStyle(IfcExternalReference):
    def __init__(self, rtype, args):
        IfcExternalReference.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcExternalReference.__str__(self),
        )

    def __json__(self):
        sup = IfcExternalReference.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcExternallyDefinedSurfaceStyle(IfcExternalReference):
    def __init__(self, rtype, args):
        IfcExternalReference.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcExternalReference.__str__(self),
        )

    def __json__(self):
        sup = IfcExternalReference.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcExternallyDefinedTextFont(IfcExternalReference):
    def __init__(self, rtype, args):
        IfcExternalReference.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcExternalReference.__str__(self),
        )

    def __json__(self):
        sup = IfcExternalReference.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcGridAxis(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.AxisTag = args.pop()
        self.AxisCurve = args.pop()
        self.SameSense = args.pop()

    def __str__(self):
        return "{sup}:AxisTag:{AxisTag}:AxisCurve:{AxisCurve}:SameSense:{SameSense}".format(
            sup=IfcEntity.__str__(self),
            AxisTag=self.AxisTag,
            AxisCurve=self.AxisCurve,
            SameSense=self.SameSense,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'AxisTag': self.AxisTag, 'AxisCurve': self.AxisCurve, 'SameSense': self.SameSense}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcIrregularTimeSeriesValue(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.TimeStamp = args.pop()
        self.ListValues = args.pop()

    def __str__(self):
        return "{sup}:TimeStamp:{TimeStamp}:ListValues:{ListValues}".format(
            sup=IfcEntity.__str__(self),
            TimeStamp=self.TimeStamp,
            ListValues=self.ListValues,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'TimeStamp': self.TimeStamp, 'ListValues': self.ListValues}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLibraryInformation(IfcExternalInformation):
    def __init__(self, rtype, args):
        IfcExternalInformation.__init__(self, rtype, args)
        self.Name = args.pop()
        self.Version = args.pop()
        self.Publisher = args.pop()
        self.VersionDate = args.pop()
        self.Location = args.pop()
        self.Description = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:Version:{Version}:Publisher:{Publisher}:VersionDate:{VersionDate}:Location:{Location}:Description:{Description}".format(
            sup=IfcExternalInformation.__str__(self),
            Name=self.Name,
            Version=self.Version,
            Publisher=self.Publisher,
            VersionDate=self.VersionDate,
            Location=self.Location,
            Description=self.Description,
        )

    def __json__(self):
        sup = IfcExternalInformation.__json__(self)
        attrs = {'Name': self.Name, 'Version': self.Version, 'Publisher': self.Publisher,
                 'VersionDate': self.VersionDate, 'Location': self.Location, 'Description': self.Description}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLibraryReference(IfcExternalReference):
    def __init__(self, rtype, args):
        IfcExternalReference.__init__(self, rtype, args)
        self.Description = args.pop()
        self.Language = args.pop()
        self.ReferencedLibrary = args.pop()

    def __str__(self):
        return "{sup}:Description:{Description}:Language:{Language}:ReferencedLibrary:{ReferencedLibrary}".format(
            sup=IfcExternalReference.__str__(self),
            Description=self.Description,
            Language=self.Language,
            ReferencedLibrary=self.ReferencedLibrary,
        )

    def __json__(self):
        sup = IfcExternalReference.__json__(self)
        attrs = {'Description': self.Description, 'Language': self.Language,
                 'ReferencedLibrary': self.ReferencedLibrary}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLightDistributionData(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.MainPlaneAngle = args.pop()
        self.SecondaryPlaneAngle = args.pop()
        self.LuminousIntensity = args.pop()

    def __str__(self):
        return "{sup}:MainPlaneAngle:{MainPlaneAngle}:SecondaryPlaneAngle:{SecondaryPlaneAngle}:LuminousIntensity:{LuminousIntensity}".format(
            sup=IfcEntity.__str__(self),
            MainPlaneAngle=self.MainPlaneAngle,
            SecondaryPlaneAngle=self.SecondaryPlaneAngle,
            LuminousIntensity=self.LuminousIntensity,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'MainPlaneAngle': self.MainPlaneAngle, 'SecondaryPlaneAngle': self.SecondaryPlaneAngle,
                 'LuminousIntensity': self.LuminousIntensity}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLightIntensityDistribution(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.LightDistributionCurve = args.pop()
        self.DistributionData = args.pop()

    def __str__(self):
        return "{sup}:LightDistributionCurve:{LightDistributionCurve}:DistributionData:{DistributionData}".format(
            sup=IfcEntity.__str__(self),
            LightDistributionCurve=self.LightDistributionCurve,
            DistributionData=self.DistributionData,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'LightDistributionCurve': self.LightDistributionCurve, 'DistributionData': self.DistributionData}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMapConversion(IfcCoordinateOperation):
    def __init__(self, rtype, args):
        IfcCoordinateOperation.__init__(self, rtype, args)
        self.Eastings = args.pop()
        self.Northings = args.pop()
        self.OrthogonalHeight = args.pop()
        self.XAxisAbscissa = args.pop()
        self.XAxisOrdinate = args.pop()
        self.Scale = args.pop()

    def __str__(self):
        return "{sup}:Eastings:{Eastings}:Northings:{Northings}:OrthogonalHeight:{OrthogonalHeight}:XAxisAbscissa:{XAxisAbscissa}:XAxisOrdinate:{XAxisOrdinate}:Scale:{Scale}".format(
            sup=IfcCoordinateOperation.__str__(self),
            Eastings=self.Eastings,
            Northings=self.Northings,
            OrthogonalHeight=self.OrthogonalHeight,
            XAxisAbscissa=self.XAxisAbscissa,
            XAxisOrdinate=self.XAxisOrdinate,
            Scale=self.Scale,
        )

    def __json__(self):
        sup = IfcCoordinateOperation.__json__(self)
        attrs = {'Eastings': self.Eastings, 'Northings': self.Northings, 'OrthogonalHeight': self.OrthogonalHeight,
                 'XAxisAbscissa': self.XAxisAbscissa, 'XAxisOrdinate': self.XAxisOrdinate, 'Scale': self.Scale}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMaterialClassificationRelationship(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.MaterialClassifications = args.pop()
        self.ClassifiedMaterial = args.pop()

    def __str__(self):
        return "{sup}:MaterialClassifications:{MaterialClassifications}:ClassifiedMaterial:{ClassifiedMaterial}".format(
            sup=IfcEntity.__str__(self),
            MaterialClassifications=self.MaterialClassifications,
            ClassifiedMaterial=self.ClassifiedMaterial,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'MaterialClassifications': self.MaterialClassifications, 'ClassifiedMaterial': self.ClassifiedMaterial}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcMaterialDefinition(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcEntity.__str__(self),
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMaterialLayer(IfcMaterialDefinition):
    def __init__(self, rtype, args):
        IfcMaterialDefinition.__init__(self, rtype, args)
        self.Material = args.pop()
        self.LayerThickness = args.pop()
        self.IsVentilated = args.pop()
        self.Name = args.pop()
        self.Description = args.pop()
        self.Category = args.pop()
        self.Priority = args.pop()

    def __str__(self):
        return "{sup}:Material:{Material}:LayerThickness:{LayerThickness}:IsVentilated:{IsVentilated}:Name:{Name}:Description:{Description}:Category:{Category}:Priority:{Priority}".format(
            sup=IfcMaterialDefinition.__str__(self),
            Material=self.Material,
            LayerThickness=self.LayerThickness,
            IsVentilated=self.IsVentilated,
            Name=self.Name,
            Description=self.Description,
            Category=self.Category,
            Priority=self.Priority,
        )

    def __json__(self):
        sup = IfcMaterialDefinition.__json__(self)
        attrs = {'Material': self.Material, 'LayerThickness': self.LayerThickness, 'IsVentilated': self.IsVentilated,
                 'Name': self.Name, 'Description': self.Description, 'Category': self.Category,
                 'Priority': self.Priority}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMaterialLayerSet(IfcMaterialDefinition):
    def __init__(self, rtype, args):
        IfcMaterialDefinition.__init__(self, rtype, args)
        self.MaterialLayers = args.pop()
        self.LayerSetName = args.pop()
        self.Description = args.pop()

    def __str__(self):
        return "{sup}:MaterialLayers:{MaterialLayers}:LayerSetName:{LayerSetName}:Description:{Description}".format(
            sup=IfcMaterialDefinition.__str__(self),
            MaterialLayers=self.MaterialLayers,
            LayerSetName=self.LayerSetName,
            Description=self.Description,
        )

    def __json__(self):
        sup = IfcMaterialDefinition.__json__(self)
        attrs = {'MaterialLayers': self.MaterialLayers, 'LayerSetName': self.LayerSetName,
                 'Description': self.Description}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMaterialLayerWithOffsets(IfcMaterialLayer):
    def __init__(self, rtype, args):
        IfcMaterialLayer.__init__(self, rtype, args)
        self.OffsetDirection = args.pop()
        self.OffsetValues = args.pop()

    def __str__(self):
        return "{sup}:OffsetDirection:{OffsetDirection}:OffsetValues:{OffsetValues}".format(
            sup=IfcMaterialLayer.__str__(self),
            OffsetDirection=self.OffsetDirection,
            OffsetValues=self.OffsetValues,
        )

    def __json__(self):
        sup = IfcMaterialLayer.__json__(self)
        attrs = {'OffsetDirection': self.OffsetDirection, 'OffsetValues': self.OffsetValues}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMaterialList(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Materials = args.pop()

    def __str__(self):
        return "{sup}:Materials:{Materials}".format(
            sup=IfcEntity.__str__(self),
            Materials=self.Materials,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Materials': self.Materials}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMaterialProfile(IfcMaterialDefinition):
    def __init__(self, rtype, args):
        IfcMaterialDefinition.__init__(self, rtype, args)
        self.Name = args.pop()
        self.Description = args.pop()
        self.Material = args.pop()
        self.Profile = args.pop()
        self.Priority = args.pop()
        self.Category = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:Description:{Description}:Material:{Material}:Profile:{Profile}:Priority:{Priority}:Category:{Category}".format(
            sup=IfcMaterialDefinition.__str__(self),
            Name=self.Name,
            Description=self.Description,
            Material=self.Material,
            Profile=self.Profile,
            Priority=self.Priority,
            Category=self.Category,
        )

    def __json__(self):
        sup = IfcMaterialDefinition.__json__(self)
        attrs = {'Name': self.Name, 'Description': self.Description, 'Material': self.Material, 'Profile': self.Profile,
                 'Priority': self.Priority, 'Category': self.Category}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMaterialProfileSet(IfcMaterialDefinition):
    def __init__(self, rtype, args):
        IfcMaterialDefinition.__init__(self, rtype, args)
        self.Name = args.pop()
        self.Description = args.pop()
        self.MaterialProfiles = args.pop()
        self.CompositeProfile = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:Description:{Description}:MaterialProfiles:{MaterialProfiles}:CompositeProfile:{CompositeProfile}".format(
            sup=IfcMaterialDefinition.__str__(self),
            Name=self.Name,
            Description=self.Description,
            MaterialProfiles=self.MaterialProfiles,
            CompositeProfile=self.CompositeProfile,
        )

    def __json__(self):
        sup = IfcMaterialDefinition.__json__(self)
        attrs = {'Name': self.Name, 'Description': self.Description, 'MaterialProfiles': self.MaterialProfiles,
                 'CompositeProfile': self.CompositeProfile}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMaterialProfileWithOffsets(IfcMaterialProfile):
    def __init__(self, rtype, args):
        IfcMaterialProfile.__init__(self, rtype, args)
        self.OffsetValues = args.pop()

    def __str__(self):
        return "{sup}:OffsetValues:{OffsetValues}".format(
            sup=IfcMaterialProfile.__str__(self),
            OffsetValues=self.OffsetValues,
        )

    def __json__(self):
        sup = IfcMaterialProfile.__json__(self)
        attrs = {'OffsetValues': self.OffsetValues}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcMaterialUsageDefinition(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcEntity.__str__(self),
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMeasureWithUnit(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.ValueComponent = args.pop()
        self.UnitComponent = args.pop()

    def __str__(self):
        return "{sup}:ValueComponent:{ValueComponent}:UnitComponent:{UnitComponent}".format(
            sup=IfcEntity.__str__(self),
            ValueComponent=self.ValueComponent,
            UnitComponent=self.UnitComponent,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'ValueComponent': self.ValueComponent, 'UnitComponent': self.UnitComponent}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMetric(IfcConstraint):
    def __init__(self, rtype, args):
        IfcConstraint.__init__(self, rtype, args)
        self.Benchmark = args.pop()
        self.ValueSource = args.pop()
        self.DataValue = args.pop()
        self.ReferencePath = args.pop()

    def __str__(self):
        return "{sup}:Benchmark:{Benchmark}:ValueSource:{ValueSource}:DataValue:{DataValue}:ReferencePath:{ReferencePath}".format(
            sup=IfcConstraint.__str__(self),
            Benchmark=self.Benchmark,
            ValueSource=self.ValueSource,
            DataValue=self.DataValue,
            ReferencePath=self.ReferencePath,
        )

    def __json__(self):
        sup = IfcConstraint.__json__(self)
        attrs = {'Benchmark': self.Benchmark, 'ValueSource': self.ValueSource, 'DataValue': self.DataValue,
                 'ReferencePath': self.ReferencePath}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMonetaryUnit(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Currency = args.pop()

    def __str__(self):
        return "{sup}:Currency:{Currency}".format(
            sup=IfcEntity.__str__(self),
            Currency=self.Currency,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Currency': self.Currency}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcNamedUnit(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Dimensions = args.pop()
        self.UnitType = args.pop()

    def __str__(self):
        return "{sup}:Dimensions:{Dimensions}:UnitType:{UnitType}".format(
            sup=IfcEntity.__str__(self),
            Dimensions=self.Dimensions,
            UnitType=self.UnitType,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Dimensions': self.Dimensions, 'UnitType': self.UnitType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcObjectPlacement(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcEntity.__str__(self),
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcObjective(IfcConstraint):
    def __init__(self, rtype, args):
        IfcConstraint.__init__(self, rtype, args)
        self.BenchmarkValues = args.pop()
        self.LogicalAggregator = args.pop()
        self.ObjectiveQualifier = args.pop()
        self.UserDefinedQualifier = args.pop()

    def __str__(self):
        return "{sup}:BenchmarkValues:{BenchmarkValues}:LogicalAggregator:{LogicalAggregator}:ObjectiveQualifier:{ObjectiveQualifier}:UserDefinedQualifier:{UserDefinedQualifier}".format(
            sup=IfcConstraint.__str__(self),
            BenchmarkValues=self.BenchmarkValues,
            LogicalAggregator=self.LogicalAggregator,
            ObjectiveQualifier=self.ObjectiveQualifier,
            UserDefinedQualifier=self.UserDefinedQualifier,
        )

    def __json__(self):
        sup = IfcConstraint.__json__(self)
        attrs = {'BenchmarkValues': self.BenchmarkValues, 'LogicalAggregator': self.LogicalAggregator,
                 'ObjectiveQualifier': self.ObjectiveQualifier, 'UserDefinedQualifier': self.UserDefinedQualifier}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcOrganization(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Identification = args.pop()
        self.Name = args.pop()
        self.Description = args.pop()
        self.Roles = args.pop()
        self.Addresses = args.pop()

    def __str__(self):
        return "{sup}:Identification:{Identification}:Name:{Name}:Description:{Description}:Roles:{Roles}:Addresses:{Addresses}".format(
            sup=IfcEntity.__str__(self),
            Identification=self.Identification,
            Name=self.Name,
            Description=self.Description,
            Roles=self.Roles,
            Addresses=self.Addresses,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Identification': self.Identification, 'Name': self.Name, 'Description': self.Description,
                 'Roles': self.Roles, 'Addresses': self.Addresses}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcOwnerHistory(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.OwningUser = args.pop()
        self.OwningApplication = args.pop()
        self.State = args.pop()
        self.ChangeAction = args.pop()
        self.LastModifiedDate = args.pop()
        self.LastModifyingUser = args.pop()
        self.LastModifyingApplication = args.pop()
        self.CreationDate = args.pop()

    def __str__(self):
        return "{sup}:OwningUser:{OwningUser}:OwningApplication:{OwningApplication}:State:{State}:ChangeAction:{ChangeAction}:LastModifiedDate:{LastModifiedDate}:LastModifyingUser:{LastModifyingUser}:LastModifyingApplication:{LastModifyingApplication}:CreationDate:{CreationDate}".format(
            sup=IfcEntity.__str__(self),
            OwningUser=self.OwningUser,
            OwningApplication=self.OwningApplication,
            State=self.State,
            ChangeAction=self.ChangeAction,
            LastModifiedDate=self.LastModifiedDate,
            LastModifyingUser=self.LastModifyingUser,
            LastModifyingApplication=self.LastModifyingApplication,
            CreationDate=self.CreationDate,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'OwningUser': self.OwningUser, 'OwningApplication': self.OwningApplication, 'State': self.State,
                 'ChangeAction': self.ChangeAction, 'LastModifiedDate': self.LastModifiedDate,
                 'LastModifyingUser': self.LastModifyingUser, 'LastModifyingApplication': self.LastModifyingApplication,
                 'CreationDate': self.CreationDate}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPerson(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Identification = args.pop()
        self.FamilyName = args.pop()
        self.GivenName = args.pop()
        self.MiddleNames = args.pop()
        self.PrefixTitles = args.pop()
        self.SuffixTitles = args.pop()
        self.Roles = args.pop()
        self.Addresses = args.pop()

    def __str__(self):
        return "{sup}:Identification:{Identification}:FamilyName:{FamilyName}:GivenName:{GivenName}:MiddleNames:{MiddleNames}:PrefixTitles:{PrefixTitles}:SuffixTitles:{SuffixTitles}:Roles:{Roles}:Addresses:{Addresses}".format(
            sup=IfcEntity.__str__(self),
            Identification=self.Identification,
            FamilyName=self.FamilyName,
            GivenName=self.GivenName,
            MiddleNames=self.MiddleNames,
            PrefixTitles=self.PrefixTitles,
            SuffixTitles=self.SuffixTitles,
            Roles=self.Roles,
            Addresses=self.Addresses,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Identification': self.Identification, 'FamilyName': self.FamilyName, 'GivenName': self.GivenName,
                 'MiddleNames': self.MiddleNames, 'PrefixTitles': self.PrefixTitles, 'SuffixTitles': self.SuffixTitles,
                 'Roles': self.Roles, 'Addresses': self.Addresses}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPersonAndOrganization(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.ThePerson = args.pop()
        self.TheOrganization = args.pop()
        self.Roles = args.pop()

    def __str__(self):
        return "{sup}:ThePerson:{ThePerson}:TheOrganization:{TheOrganization}:Roles:{Roles}".format(
            sup=IfcEntity.__str__(self),
            ThePerson=self.ThePerson,
            TheOrganization=self.TheOrganization,
            Roles=self.Roles,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'ThePerson': self.ThePerson, 'TheOrganization': self.TheOrganization, 'Roles': self.Roles}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcPhysicalQuantity(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Name = args.pop()
        self.Description = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:Description:{Description}".format(
            sup=IfcEntity.__str__(self),
            Name=self.Name,
            Description=self.Description,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Name': self.Name, 'Description': self.Description}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcPhysicalSimpleQuantity(IfcPhysicalQuantity):
    def __init__(self, rtype, args):
        IfcPhysicalQuantity.__init__(self, rtype, args)
        self.Unit = args.pop()

    def __str__(self):
        return "{sup}:Unit:{Unit}".format(
            sup=IfcPhysicalQuantity.__str__(self),
            Unit=self.Unit,
        )

    def __json__(self):
        sup = IfcPhysicalQuantity.__json__(self)
        attrs = {'Unit': self.Unit}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPostalAddress(IfcAddress):
    def __init__(self, rtype, args):
        IfcAddress.__init__(self, rtype, args)
        self.InternalLocation = args.pop()
        self.AddressLines = args.pop()
        self.PostalBox = args.pop()
        self.Town = args.pop()
        self.Region = args.pop()
        self.PostalCode = args.pop()
        self.Country = args.pop()

    def __str__(self):
        return "{sup}:InternalLocation:{InternalLocation}:AddressLines:{AddressLines}:PostalBox:{PostalBox}:Town:{Town}:Region:{Region}:PostalCode:{PostalCode}:Country:{Country}".format(
            sup=IfcAddress.__str__(self),
            InternalLocation=self.InternalLocation,
            AddressLines=self.AddressLines,
            PostalBox=self.PostalBox,
            Town=self.Town,
            Region=self.Region,
            PostalCode=self.PostalCode,
            Country=self.Country,
        )

    def __json__(self):
        sup = IfcAddress.__json__(self)
        attrs = {'InternalLocation': self.InternalLocation, 'AddressLines': self.AddressLines,
                 'PostalBox': self.PostalBox, 'Town': self.Town, 'Region': self.Region, 'PostalCode': self.PostalCode,
                 'Country': self.Country}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcPresentationItem(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcEntity.__str__(self),
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPresentationLayerAssignment(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Name = args.pop()
        self.Description = args.pop()
        self.AssignedItems = args.pop()
        self.Identifier = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:Description:{Description}:AssignedItems:{AssignedItems}:Identifier:{Identifier}".format(
            sup=IfcEntity.__str__(self),
            Name=self.Name,
            Description=self.Description,
            AssignedItems=self.AssignedItems,
            Identifier=self.Identifier,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Name': self.Name, 'Description': self.Description, 'AssignedItems': self.AssignedItems,
                 'Identifier': self.Identifier}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPresentationLayerWithStyle(IfcPresentationLayerAssignment):
    def __init__(self, rtype, args):
        IfcPresentationLayerAssignment.__init__(self, rtype, args)
        self.LayerOn = args.pop()
        self.LayerFrozen = args.pop()
        self.LayerBlocked = args.pop()
        self.LayerStyles = args.pop()

    def __str__(self):
        return "{sup}:LayerOn:{LayerOn}:LayerFrozen:{LayerFrozen}:LayerBlocked:{LayerBlocked}:LayerStyles:{LayerStyles}".format(
            sup=IfcPresentationLayerAssignment.__str__(self),
            LayerOn=self.LayerOn,
            LayerFrozen=self.LayerFrozen,
            LayerBlocked=self.LayerBlocked,
            LayerStyles=self.LayerStyles,
        )

    def __json__(self):
        sup = IfcPresentationLayerAssignment.__json__(self)
        attrs = {'LayerOn': self.LayerOn, 'LayerFrozen': self.LayerFrozen, 'LayerBlocked': self.LayerBlocked,
                 'LayerStyles': self.LayerStyles}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcPresentationStyle(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Name = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}".format(
            sup=IfcEntity.__str__(self),
            Name=self.Name,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Name': self.Name}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPresentationStyleAssignment(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Styles = args.pop()

    def __str__(self):
        return "{sup}:Styles:{Styles}".format(
            sup=IfcEntity.__str__(self),
            Styles=self.Styles,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Styles': self.Styles}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcProductRepresentation(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Name = args.pop()
        self.Description = args.pop()
        self.Representations = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:Description:{Description}:Representations:{Representations}".format(
            sup=IfcEntity.__str__(self),
            Name=self.Name,
            Description=self.Description,
            Representations=self.Representations,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Name': self.Name, 'Description': self.Description, 'Representations': self.Representations}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcProfileDef(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.ProfileType = args.pop()
        self.ProfileName = args.pop()

    def __str__(self):
        return "{sup}:ProfileType:{ProfileType}:ProfileName:{ProfileName}".format(
            sup=IfcEntity.__str__(self),
            ProfileType=self.ProfileType,
            ProfileName=self.ProfileName,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'ProfileType': self.ProfileType, 'ProfileName': self.ProfileName}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcProjectedCRS(IfcCoordinateReferenceSystem):
    def __init__(self, rtype, args):
        IfcCoordinateReferenceSystem.__init__(self, rtype, args)
        self.MapProjection = args.pop()
        self.MapZone = args.pop()
        self.MapUnit = args.pop()

    def __str__(self):
        return "{sup}:MapProjection:{MapProjection}:MapZone:{MapZone}:MapUnit:{MapUnit}".format(
            sup=IfcCoordinateReferenceSystem.__str__(self),
            MapProjection=self.MapProjection,
            MapZone=self.MapZone,
            MapUnit=self.MapUnit,
        )

    def __json__(self):
        sup = IfcCoordinateReferenceSystem.__json__(self)
        attrs = {'MapProjection': self.MapProjection, 'MapZone': self.MapZone, 'MapUnit': self.MapUnit}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcPropertyAbstraction(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcEntity.__str__(self),
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPropertyEnumeration(IfcPropertyAbstraction):
    def __init__(self, rtype, args):
        IfcPropertyAbstraction.__init__(self, rtype, args)
        self.Name = args.pop()
        self.EnumerationValues = args.pop()
        self.Unit = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:EnumerationValues:{EnumerationValues}:Unit:{Unit}".format(
            sup=IfcPropertyAbstraction.__str__(self),
            Name=self.Name,
            EnumerationValues=self.EnumerationValues,
            Unit=self.Unit,
        )

    def __json__(self):
        sup = IfcPropertyAbstraction.__json__(self)
        attrs = {'Name': self.Name, 'EnumerationValues': self.EnumerationValues, 'Unit': self.Unit}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcQuantityArea(IfcPhysicalSimpleQuantity):
    def __init__(self, rtype, args):
        IfcPhysicalSimpleQuantity.__init__(self, rtype, args)
        self.AreaValue = args.pop()
        self.Formula = args.pop()

    def __str__(self):
        return "{sup}:AreaValue:{AreaValue}:Formula:{Formula}".format(
            sup=IfcPhysicalSimpleQuantity.__str__(self),
            AreaValue=self.AreaValue,
            Formula=self.Formula,
        )

    def __json__(self):
        sup = IfcPhysicalSimpleQuantity.__json__(self)
        attrs = {'AreaValue': self.AreaValue, 'Formula': self.Formula}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcQuantityCount(IfcPhysicalSimpleQuantity):
    def __init__(self, rtype, args):
        IfcPhysicalSimpleQuantity.__init__(self, rtype, args)
        self.CountValue = args.pop()
        self.Formula = args.pop()

    def __str__(self):
        return "{sup}:CountValue:{CountValue}:Formula:{Formula}".format(
            sup=IfcPhysicalSimpleQuantity.__str__(self),
            CountValue=self.CountValue,
            Formula=self.Formula,
        )

    def __json__(self):
        sup = IfcPhysicalSimpleQuantity.__json__(self)
        attrs = {'CountValue': self.CountValue, 'Formula': self.Formula}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcQuantityLength(IfcPhysicalSimpleQuantity):
    def __init__(self, rtype, args):
        IfcPhysicalSimpleQuantity.__init__(self, rtype, args)
        self.LengthValue = args.pop()
        self.Formula = args.pop()

    def __str__(self):
        return "{sup}:LengthValue:{LengthValue}:Formula:{Formula}".format(
            sup=IfcPhysicalSimpleQuantity.__str__(self),
            LengthValue=self.LengthValue,
            Formula=self.Formula,
        )

    def __json__(self):
        sup = IfcPhysicalSimpleQuantity.__json__(self)
        attrs = {'LengthValue': self.LengthValue, 'Formula': self.Formula}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcQuantityTime(IfcPhysicalSimpleQuantity):
    def __init__(self, rtype, args):
        IfcPhysicalSimpleQuantity.__init__(self, rtype, args)
        self.TimeValue = args.pop()
        self.Formula = args.pop()

    def __str__(self):
        return "{sup}:TimeValue:{TimeValue}:Formula:{Formula}".format(
            sup=IfcPhysicalSimpleQuantity.__str__(self),
            TimeValue=self.TimeValue,
            Formula=self.Formula,
        )

    def __json__(self):
        sup = IfcPhysicalSimpleQuantity.__json__(self)
        attrs = {'TimeValue': self.TimeValue, 'Formula': self.Formula}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcQuantityVolume(IfcPhysicalSimpleQuantity):
    def __init__(self, rtype, args):
        IfcPhysicalSimpleQuantity.__init__(self, rtype, args)
        self.VolumeValue = args.pop()
        self.Formula = args.pop()

    def __str__(self):
        return "{sup}:VolumeValue:{VolumeValue}:Formula:{Formula}".format(
            sup=IfcPhysicalSimpleQuantity.__str__(self),
            VolumeValue=self.VolumeValue,
            Formula=self.Formula,
        )

    def __json__(self):
        sup = IfcPhysicalSimpleQuantity.__json__(self)
        attrs = {'VolumeValue': self.VolumeValue, 'Formula': self.Formula}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcQuantityWeight(IfcPhysicalSimpleQuantity):
    def __init__(self, rtype, args):
        IfcPhysicalSimpleQuantity.__init__(self, rtype, args)
        self.WeightValue = args.pop()
        self.Formula = args.pop()

    def __str__(self):
        return "{sup}:WeightValue:{WeightValue}:Formula:{Formula}".format(
            sup=IfcPhysicalSimpleQuantity.__str__(self),
            WeightValue=self.WeightValue,
            Formula=self.Formula,
        )

    def __json__(self):
        sup = IfcPhysicalSimpleQuantity.__json__(self)
        attrs = {'WeightValue': self.WeightValue, 'Formula': self.Formula}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRecurrencePattern(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.RecurrenceType = args.pop()
        self.DayComponent = args.pop()
        self.WeekdayComponent = args.pop()
        self.MonthComponent = args.pop()
        self.Position = args.pop()
        self.Interval = args.pop()
        self.Occurrences = args.pop()
        self.TimePeriods = args.pop()

    def __str__(self):
        return "{sup}:RecurrenceType:{RecurrenceType}:DayComponent:{DayComponent}:WeekdayComponent:{WeekdayComponent}:MonthComponent:{MonthComponent}:Position:{Position}:Interval:{Interval}:Occurrences:{Occurrences}:TimePeriods:{TimePeriods}".format(
            sup=IfcEntity.__str__(self),
            RecurrenceType=self.RecurrenceType,
            DayComponent=self.DayComponent,
            WeekdayComponent=self.WeekdayComponent,
            MonthComponent=self.MonthComponent,
            Position=self.Position,
            Interval=self.Interval,
            Occurrences=self.Occurrences,
            TimePeriods=self.TimePeriods,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'RecurrenceType': self.RecurrenceType, 'DayComponent': self.DayComponent,
                 'WeekdayComponent': self.WeekdayComponent, 'MonthComponent': self.MonthComponent,
                 'Position': self.Position, 'Interval': self.Interval, 'Occurrences': self.Occurrences,
                 'TimePeriods': self.TimePeriods}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcReference(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.TypeIdentifier = args.pop()
        self.AttributeIdentifier = args.pop()
        self.InstanceName = args.pop()
        self.ListPositions = args.pop()
        self.InnerReference = args.pop()

    def __str__(self):
        return "{sup}:TypeIdentifier:{TypeIdentifier}:AttributeIdentifier:{AttributeIdentifier}:InstanceName:{InstanceName}:ListPositions:{ListPositions}:InnerReference:{InnerReference}".format(
            sup=IfcEntity.__str__(self),
            TypeIdentifier=self.TypeIdentifier,
            AttributeIdentifier=self.AttributeIdentifier,
            InstanceName=self.InstanceName,
            ListPositions=self.ListPositions,
            InnerReference=self.InnerReference,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'TypeIdentifier': self.TypeIdentifier, 'AttributeIdentifier': self.AttributeIdentifier,
                 'InstanceName': self.InstanceName, 'ListPositions': self.ListPositions,
                 'InnerReference': self.InnerReference}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcRepresentation(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.ContextOfItems = args.pop()
        self.RepresentationIdentifier = args.pop()
        self.RepresentationType = args.pop()
        self.Items = args.pop()

    def __str__(self):
        return "{sup}:ContextOfItems:{ContextOfItems}:RepresentationIdentifier:{RepresentationIdentifier}:RepresentationType:{RepresentationType}:Items:{Items}".format(
            sup=IfcEntity.__str__(self),
            ContextOfItems=self.ContextOfItems,
            RepresentationIdentifier=self.RepresentationIdentifier,
            RepresentationType=self.RepresentationType,
            Items=self.Items,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'ContextOfItems': self.ContextOfItems, 'RepresentationIdentifier': self.RepresentationIdentifier,
                 'RepresentationType': self.RepresentationType, 'Items': self.Items}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcRepresentationContext(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.ContextIdentifier = args.pop()
        self.ContextType = args.pop()

    def __str__(self):
        return "{sup}:ContextIdentifier:{ContextIdentifier}:ContextType:{ContextType}".format(
            sup=IfcEntity.__str__(self),
            ContextIdentifier=self.ContextIdentifier,
            ContextType=self.ContextType,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'ContextIdentifier': self.ContextIdentifier, 'ContextType': self.ContextType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcRepresentationItem(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcEntity.__str__(self),
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRepresentationMap(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.MappingOrigin = args.pop()
        self.MappedRepresentation = args.pop()

    def __str__(self):
        return "{sup}:MappingOrigin:{MappingOrigin}:MappedRepresentation:{MappedRepresentation}".format(
            sup=IfcEntity.__str__(self),
            MappingOrigin=self.MappingOrigin,
            MappedRepresentation=self.MappedRepresentation,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'MappingOrigin': self.MappingOrigin, 'MappedRepresentation': self.MappedRepresentation}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcResourceLevelRelationship(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Name = args.pop()
        self.Description = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:Description:{Description}".format(
            sup=IfcEntity.__str__(self),
            Name=self.Name,
            Description=self.Description,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Name': self.Name, 'Description': self.Description}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcRoot(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.GlobalId = parse_uuid(args.pop())
        self.OwnerHistory = args.pop()
        self.Name = args.pop()
        self.Description = args.pop()

    def __str__(self):
        return "{sup}:GlobalId:{GlobalId}:OwnerHistory:{OwnerHistory}:Name:{Name}:Description:{Description}".format(
            sup=IfcEntity.__str__(self),
            GlobalId=self.GlobalId,
            OwnerHistory=self.OwnerHistory,
            Name=self.Name,
            Description=self.Description,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'GlobalId': self.GlobalId, 'OwnerHistory': self.OwnerHistory, 'Name': self.Name,
                 'Description': self.Description}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSIUnit(IfcNamedUnit):
    def __init__(self, rtype, args):
        IfcNamedUnit.__init__(self, rtype, args)
        self.Prefix = args.pop()
        self.Name = args.pop()

    def __str__(self):
        return "{sup}:Prefix:{Prefix}:Name:{Name}".format(
            sup=IfcNamedUnit.__str__(self),
            Prefix=self.Prefix,
            Name=self.Name,
        )

    def __json__(self):
        sup = IfcNamedUnit.__json__(self)
        attrs = {'Prefix': self.Prefix, 'Name': self.Name}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcSchedulingTime(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Name = args.pop()
        self.DataOrigin = args.pop()
        self.UserDefinedDataOrigin = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:DataOrigin:{DataOrigin}:UserDefinedDataOrigin:{UserDefinedDataOrigin}".format(
            sup=IfcEntity.__str__(self),
            Name=self.Name,
            DataOrigin=self.DataOrigin,
            UserDefinedDataOrigin=self.UserDefinedDataOrigin,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Name': self.Name, 'DataOrigin': self.DataOrigin, 'UserDefinedDataOrigin': self.UserDefinedDataOrigin}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcShapeAspect(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.ShapeRepresentations = args.pop()
        self.Name = args.pop()
        self.Description = args.pop()
        self.ProductDefinitional = args.pop()
        self.PartOfProductDefinitionShape = args.pop()

    def __str__(self):
        return "{sup}:ShapeRepresentations:{ShapeRepresentations}:Name:{Name}:Description:{Description}:ProductDefinitional:{ProductDefinitional}:PartOfProductDefinitionShape:{PartOfProductDefinitionShape}".format(
            sup=IfcEntity.__str__(self),
            ShapeRepresentations=self.ShapeRepresentations,
            Name=self.Name,
            Description=self.Description,
            ProductDefinitional=self.ProductDefinitional,
            PartOfProductDefinitionShape=self.PartOfProductDefinitionShape,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'ShapeRepresentations': self.ShapeRepresentations, 'Name': self.Name, 'Description': self.Description,
                 'ProductDefinitional': self.ProductDefinitional,
                 'PartOfProductDefinitionShape': self.PartOfProductDefinitionShape}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcShapeModel(IfcRepresentation):
    def __init__(self, rtype, args):
        IfcRepresentation.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcRepresentation.__str__(self),
        )

    def __json__(self):
        sup = IfcRepresentation.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcShapeRepresentation(IfcShapeModel):
    def __init__(self, rtype, args):
        IfcShapeModel.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcShapeModel.__str__(self),
        )

    def __json__(self):
        sup = IfcShapeModel.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcStructuralConnectionCondition(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Name = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}".format(
            sup=IfcEntity.__str__(self),
            Name=self.Name,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Name': self.Name}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcStructuralLoad(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Name = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}".format(
            sup=IfcEntity.__str__(self),
            Name=self.Name,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Name': self.Name}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralLoadConfiguration(IfcStructuralLoad):
    def __init__(self, rtype, args):
        IfcStructuralLoad.__init__(self, rtype, args)
        self.Values = args.pop()
        self.Locations = args.pop()

    def __str__(self):
        return "{sup}:Values:{Values}:Locations:{Locations}".format(
            sup=IfcStructuralLoad.__str__(self),
            Values=self.Values,
            Locations=self.Locations,
        )

    def __json__(self):
        sup = IfcStructuralLoad.__json__(self)
        attrs = {'Values': self.Values, 'Locations': self.Locations}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcStructuralLoadOrResult(IfcStructuralLoad):
    def __init__(self, rtype, args):
        IfcStructuralLoad.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcStructuralLoad.__str__(self),
        )

    def __json__(self):
        sup = IfcStructuralLoad.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcStructuralLoadStatic(IfcStructuralLoadOrResult):
    def __init__(self, rtype, args):
        IfcStructuralLoadOrResult.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcStructuralLoadOrResult.__str__(self),
        )

    def __json__(self):
        sup = IfcStructuralLoadOrResult.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralLoadTemperature(IfcStructuralLoadStatic):
    def __init__(self, rtype, args):
        IfcStructuralLoadStatic.__init__(self, rtype, args)
        self.DeltaTConstant = args.pop()
        self.DeltaTY = args.pop()
        self.DeltaTZ = args.pop()

    def __str__(self):
        return "{sup}:DeltaTConstant:{DeltaTConstant}:DeltaTY:{DeltaTY}:DeltaTZ:{DeltaTZ}".format(
            sup=IfcStructuralLoadStatic.__str__(self),
            DeltaTConstant=self.DeltaTConstant,
            DeltaTY=self.DeltaTY,
            DeltaTZ=self.DeltaTZ,
        )

    def __json__(self):
        sup = IfcStructuralLoadStatic.__json__(self)
        attrs = {'DeltaTConstant': self.DeltaTConstant, 'DeltaTY': self.DeltaTY, 'DeltaTZ': self.DeltaTZ}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcStyleModel(IfcRepresentation):
    def __init__(self, rtype, args):
        IfcRepresentation.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcRepresentation.__str__(self),
        )

    def __json__(self):
        sup = IfcRepresentation.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStyledItem(IfcRepresentationItem):
    def __init__(self, rtype, args):
        IfcRepresentationItem.__init__(self, rtype, args)
        self.Item = args.pop()
        self.Styles = args.pop()
        self.Name = args.pop()

    def __str__(self):
        return "{sup}:Item:{Item}:Styles:{Styles}:Name:{Name}".format(
            sup=IfcRepresentationItem.__str__(self),
            Item=self.Item,
            Styles=self.Styles,
            Name=self.Name,
        )

    def __json__(self):
        sup = IfcRepresentationItem.__json__(self)
        attrs = {'Item': self.Item, 'Styles': self.Styles, 'Name': self.Name}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStyledRepresentation(IfcStyleModel):
    def __init__(self, rtype, args):
        IfcStyleModel.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcStyleModel.__str__(self),
        )

    def __json__(self):
        sup = IfcStyleModel.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSurfaceReinforcementArea(IfcStructuralLoadOrResult):
    def __init__(self, rtype, args):
        IfcStructuralLoadOrResult.__init__(self, rtype, args)
        self.SurfaceReinforcement1 = args.pop()
        self.SurfaceReinforcement2 = args.pop()
        self.ShearReinforcement = args.pop()

    def __str__(self):
        return "{sup}:SurfaceReinforcement1:{SurfaceReinforcement1}:SurfaceReinforcement2:{SurfaceReinforcement2}:ShearReinforcement:{ShearReinforcement}".format(
            sup=IfcStructuralLoadOrResult.__str__(self),
            SurfaceReinforcement1=self.SurfaceReinforcement1,
            SurfaceReinforcement2=self.SurfaceReinforcement2,
            ShearReinforcement=self.ShearReinforcement,
        )

    def __json__(self):
        sup = IfcStructuralLoadOrResult.__json__(self)
        attrs = {'SurfaceReinforcement1': self.SurfaceReinforcement1,
                 'SurfaceReinforcement2': self.SurfaceReinforcement2, 'ShearReinforcement': self.ShearReinforcement}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSurfaceStyle(IfcPresentationStyle):
    def __init__(self, rtype, args):
        IfcPresentationStyle.__init__(self, rtype, args)
        self.Side = args.pop()
        self.Styles = args.pop()

    def __str__(self):
        return "{sup}:Side:{Side}:Styles:{Styles}".format(
            sup=IfcPresentationStyle.__str__(self),
            Side=self.Side,
            Styles=self.Styles,
        )

    def __json__(self):
        sup = IfcPresentationStyle.__json__(self)
        attrs = {'Side': self.Side, 'Styles': self.Styles}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSurfaceStyleLighting(IfcPresentationItem):
    def __init__(self, rtype, args):
        IfcPresentationItem.__init__(self, rtype, args)
        self.DiffuseTransmissionColour = args.pop()
        self.DiffuseReflectionColour = args.pop()
        self.TransmissionColour = args.pop()
        self.ReflectanceColour = args.pop()

    def __str__(self):
        return "{sup}:DiffuseTransmissionColour:{DiffuseTransmissionColour}:DiffuseReflectionColour:{DiffuseReflectionColour}:TransmissionColour:{TransmissionColour}:ReflectanceColour:{ReflectanceColour}".format(
            sup=IfcPresentationItem.__str__(self),
            DiffuseTransmissionColour=self.DiffuseTransmissionColour,
            DiffuseReflectionColour=self.DiffuseReflectionColour,
            TransmissionColour=self.TransmissionColour,
            ReflectanceColour=self.ReflectanceColour,
        )

    def __json__(self):
        sup = IfcPresentationItem.__json__(self)
        attrs = {'DiffuseTransmissionColour': self.DiffuseTransmissionColour,
                 'DiffuseReflectionColour': self.DiffuseReflectionColour, 'TransmissionColour': self.TransmissionColour,
                 'ReflectanceColour': self.ReflectanceColour}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSurfaceStyleRefraction(IfcPresentationItem):
    def __init__(self, rtype, args):
        IfcPresentationItem.__init__(self, rtype, args)
        self.RefractionIndex = args.pop()
        self.DispersionFactor = args.pop()

    def __str__(self):
        return "{sup}:RefractionIndex:{RefractionIndex}:DispersionFactor:{DispersionFactor}".format(
            sup=IfcPresentationItem.__str__(self),
            RefractionIndex=self.RefractionIndex,
            DispersionFactor=self.DispersionFactor,
        )

    def __json__(self):
        sup = IfcPresentationItem.__json__(self)
        attrs = {'RefractionIndex': self.RefractionIndex, 'DispersionFactor': self.DispersionFactor}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSurfaceStyleShading(IfcPresentationItem):
    def __init__(self, rtype, args):
        IfcPresentationItem.__init__(self, rtype, args)
        self.SurfaceColour = args.pop()
        self.Transparency = args.pop()

    def __str__(self):
        return "{sup}:SurfaceColour:{SurfaceColour}:Transparency:{Transparency}".format(
            sup=IfcPresentationItem.__str__(self),
            SurfaceColour=self.SurfaceColour,
            Transparency=self.Transparency,
        )

    def __json__(self):
        sup = IfcPresentationItem.__json__(self)
        attrs = {'SurfaceColour': self.SurfaceColour, 'Transparency': self.Transparency}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSurfaceStyleWithTextures(IfcPresentationItem):
    def __init__(self, rtype, args):
        IfcPresentationItem.__init__(self, rtype, args)
        self.Textures = args.pop()

    def __str__(self):
        return "{sup}:Textures:{Textures}".format(
            sup=IfcPresentationItem.__str__(self),
            Textures=self.Textures,
        )

    def __json__(self):
        sup = IfcPresentationItem.__json__(self)
        attrs = {'Textures': self.Textures}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcSurfaceTexture(IfcPresentationItem):
    def __init__(self, rtype, args):
        IfcPresentationItem.__init__(self, rtype, args)
        self.RepeatS = args.pop()
        self.RepeatT = args.pop()
        self.Mode = args.pop()
        self.TextureTransform = args.pop()
        self.Parameter = args.pop()

    def __str__(self):
        return "{sup}:RepeatS:{RepeatS}:RepeatT:{RepeatT}:Mode:{Mode}:TextureTransform:{TextureTransform}:Parameter:{Parameter}".format(
            sup=IfcPresentationItem.__str__(self),
            RepeatS=self.RepeatS,
            RepeatT=self.RepeatT,
            Mode=self.Mode,
            TextureTransform=self.TextureTransform,
            Parameter=self.Parameter,
        )

    def __json__(self):
        sup = IfcPresentationItem.__json__(self)
        attrs = {'RepeatS': self.RepeatS, 'RepeatT': self.RepeatT, 'Mode': self.Mode,
                 'TextureTransform': self.TextureTransform, 'Parameter': self.Parameter}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTable(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Name = args.pop()
        self.Rows = args.pop()
        self.Columns = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:Rows:{Rows}:Columns:{Columns}".format(
            sup=IfcEntity.__str__(self),
            Name=self.Name,
            Rows=self.Rows,
            Columns=self.Columns,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Name': self.Name, 'Rows': self.Rows, 'Columns': self.Columns}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTableColumn(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Identifier = args.pop()
        self.Name = args.pop()
        self.Description = args.pop()
        self.Unit = args.pop()
        self.ReferencePath = args.pop()

    def __str__(self):
        return "{sup}:Identifier:{Identifier}:Name:{Name}:Description:{Description}:Unit:{Unit}:ReferencePath:{ReferencePath}".format(
            sup=IfcEntity.__str__(self),
            Identifier=self.Identifier,
            Name=self.Name,
            Description=self.Description,
            Unit=self.Unit,
            ReferencePath=self.ReferencePath,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Identifier': self.Identifier, 'Name': self.Name, 'Description': self.Description, 'Unit': self.Unit,
                 'ReferencePath': self.ReferencePath}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTableRow(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.RowCells = args.pop()
        self.IsHeading = args.pop()

    def __str__(self):
        return "{sup}:RowCells:{RowCells}:IsHeading:{IsHeading}".format(
            sup=IfcEntity.__str__(self),
            RowCells=self.RowCells,
            IsHeading=self.IsHeading,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'RowCells': self.RowCells, 'IsHeading': self.IsHeading}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTaskTime(IfcSchedulingTime):
    def __init__(self, rtype, args):
        IfcSchedulingTime.__init__(self, rtype, args)
        self.DurationType = args.pop()
        self.ScheduleDuration = args.pop()
        self.ScheduleStart = args.pop()
        self.ScheduleFinish = args.pop()
        self.EarlyStart = args.pop()
        self.EarlyFinish = args.pop()
        self.LateStart = args.pop()
        self.LateFinish = args.pop()
        self.FreeFloat = args.pop()
        self.TotalFloat = args.pop()
        self.IsCritical = args.pop()
        self.StatusTime = args.pop()
        self.ActualDuration = args.pop()
        self.ActualStart = args.pop()
        self.ActualFinish = args.pop()
        self.RemainingTime = args.pop()
        self.Completion = args.pop()

    def __str__(self):
        return "{sup}:DurationType:{DurationType}:ScheduleDuration:{ScheduleDuration}:ScheduleStart:{ScheduleStart}:ScheduleFinish:{ScheduleFinish}:EarlyStart:{EarlyStart}:EarlyFinish:{EarlyFinish}:LateStart:{LateStart}:LateFinish:{LateFinish}:FreeFloat:{FreeFloat}:TotalFloat:{TotalFloat}:IsCritical:{IsCritical}:StatusTime:{StatusTime}:ActualDuration:{ActualDuration}:ActualStart:{ActualStart}:ActualFinish:{ActualFinish}:RemainingTime:{RemainingTime}:Completion:{Completion}".format(
            sup=IfcSchedulingTime.__str__(self),
            DurationType=self.DurationType,
            ScheduleDuration=self.ScheduleDuration,
            ScheduleStart=self.ScheduleStart,
            ScheduleFinish=self.ScheduleFinish,
            EarlyStart=self.EarlyStart,
            EarlyFinish=self.EarlyFinish,
            LateStart=self.LateStart,
            LateFinish=self.LateFinish,
            FreeFloat=self.FreeFloat,
            TotalFloat=self.TotalFloat,
            IsCritical=self.IsCritical,
            StatusTime=self.StatusTime,
            ActualDuration=self.ActualDuration,
            ActualStart=self.ActualStart,
            ActualFinish=self.ActualFinish,
            RemainingTime=self.RemainingTime,
            Completion=self.Completion,
        )

    def __json__(self):
        sup = IfcSchedulingTime.__json__(self)
        attrs = {'DurationType': self.DurationType, 'ScheduleDuration': self.ScheduleDuration,
                 'ScheduleStart': self.ScheduleStart, 'ScheduleFinish': self.ScheduleFinish,
                 'EarlyStart': self.EarlyStart, 'EarlyFinish': self.EarlyFinish, 'LateStart': self.LateStart,
                 'LateFinish': self.LateFinish, 'FreeFloat': self.FreeFloat, 'TotalFloat': self.TotalFloat,
                 'IsCritical': self.IsCritical, 'StatusTime': self.StatusTime, 'ActualDuration': self.ActualDuration,
                 'ActualStart': self.ActualStart, 'ActualFinish': self.ActualFinish,
                 'RemainingTime': self.RemainingTime, 'Completion': self.Completion}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTaskTimeRecurring(IfcTaskTime):
    def __init__(self, rtype, args):
        IfcTaskTime.__init__(self, rtype, args)
        self.Recurrence = args.pop()

    def __str__(self):
        return "{sup}:Recurrence:{Recurrence}".format(
            sup=IfcTaskTime.__str__(self),
            Recurrence=self.Recurrence,
        )

    def __json__(self):
        sup = IfcTaskTime.__json__(self)
        attrs = {'Recurrence': self.Recurrence}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTelecomAddress(IfcAddress):
    def __init__(self, rtype, args):
        IfcAddress.__init__(self, rtype, args)
        self.TelephoneNumbers = args.pop()
        self.FacsimileNumbers = args.pop()
        self.PagerNumber = args.pop()
        self.ElectronicMailAddresses = args.pop()
        self.WWWHomePageURL = args.pop()
        self.MessagingIDs = args.pop()

    def __str__(self):
        return "{sup}:TelephoneNumbers:{TelephoneNumbers}:FacsimileNumbers:{FacsimileNumbers}:PagerNumber:{PagerNumber}:ElectronicMailAddresses:{ElectronicMailAddresses}:WWWHomePageURL:{WWWHomePageURL}:MessagingIDs:{MessagingIDs}".format(
            sup=IfcAddress.__str__(self),
            TelephoneNumbers=self.TelephoneNumbers,
            FacsimileNumbers=self.FacsimileNumbers,
            PagerNumber=self.PagerNumber,
            ElectronicMailAddresses=self.ElectronicMailAddresses,
            WWWHomePageURL=self.WWWHomePageURL,
            MessagingIDs=self.MessagingIDs,
        )

    def __json__(self):
        sup = IfcAddress.__json__(self)
        attrs = {'TelephoneNumbers': self.TelephoneNumbers, 'FacsimileNumbers': self.FacsimileNumbers,
                 'PagerNumber': self.PagerNumber, 'ElectronicMailAddresses': self.ElectronicMailAddresses,
                 'WWWHomePageURL': self.WWWHomePageURL, 'MessagingIDs': self.MessagingIDs}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTextStyle(IfcPresentationStyle):
    def __init__(self, rtype, args):
        IfcPresentationStyle.__init__(self, rtype, args)
        self.TextCharacterAppearance = args.pop()
        self.TextStyle = args.pop()
        self.TextFontStyle = args.pop()
        self.ModelOrDraughting = args.pop()

    def __str__(self):
        return "{sup}:TextCharacterAppearance:{TextCharacterAppearance}:TextStyle:{TextStyle}:TextFontStyle:{TextFontStyle}:ModelOrDraughting:{ModelOrDraughting}".format(
            sup=IfcPresentationStyle.__str__(self),
            TextCharacterAppearance=self.TextCharacterAppearance,
            TextStyle=self.TextStyle,
            TextFontStyle=self.TextFontStyle,
            ModelOrDraughting=self.ModelOrDraughting,
        )

    def __json__(self):
        sup = IfcPresentationStyle.__json__(self)
        attrs = {'TextCharacterAppearance': self.TextCharacterAppearance, 'TextStyle': self.TextStyle,
                 'TextFontStyle': self.TextFontStyle, 'ModelOrDraughting': self.ModelOrDraughting}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTextStyleForDefinedFont(IfcPresentationItem):
    def __init__(self, rtype, args):
        IfcPresentationItem.__init__(self, rtype, args)
        self.Colour = args.pop()
        self.BackgroundColour = args.pop()

    def __str__(self):
        return "{sup}:Colour:{Colour}:BackgroundColour:{BackgroundColour}".format(
            sup=IfcPresentationItem.__str__(self),
            Colour=self.Colour,
            BackgroundColour=self.BackgroundColour,
        )

    def __json__(self):
        sup = IfcPresentationItem.__json__(self)
        attrs = {'Colour': self.Colour, 'BackgroundColour': self.BackgroundColour}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTextStyleTextModel(IfcPresentationItem):
    def __init__(self, rtype, args):
        IfcPresentationItem.__init__(self, rtype, args)
        self.TextIndent = args.pop()
        self.TextAlign = args.pop()
        self.TextDecoration = args.pop()
        self.LetterSpacing = args.pop()
        self.WordSpacing = args.pop()
        self.TextTransform = args.pop()
        self.LineHeight = args.pop()

    def __str__(self):
        return "{sup}:TextIndent:{TextIndent}:TextAlign:{TextAlign}:TextDecoration:{TextDecoration}:LetterSpacing:{LetterSpacing}:WordSpacing:{WordSpacing}:TextTransform:{TextTransform}:LineHeight:{LineHeight}".format(
            sup=IfcPresentationItem.__str__(self),
            TextIndent=self.TextIndent,
            TextAlign=self.TextAlign,
            TextDecoration=self.TextDecoration,
            LetterSpacing=self.LetterSpacing,
            WordSpacing=self.WordSpacing,
            TextTransform=self.TextTransform,
            LineHeight=self.LineHeight,
        )

    def __json__(self):
        sup = IfcPresentationItem.__json__(self)
        attrs = {'TextIndent': self.TextIndent, 'TextAlign': self.TextAlign, 'TextDecoration': self.TextDecoration,
                 'LetterSpacing': self.LetterSpacing, 'WordSpacing': self.WordSpacing,
                 'TextTransform': self.TextTransform, 'LineHeight': self.LineHeight}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcTextureCoordinate(IfcPresentationItem):
    def __init__(self, rtype, args):
        IfcPresentationItem.__init__(self, rtype, args)
        self.Maps = args.pop()

    def __str__(self):
        return "{sup}:Maps:{Maps}".format(
            sup=IfcPresentationItem.__str__(self),
            Maps=self.Maps,
        )

    def __json__(self):
        sup = IfcPresentationItem.__json__(self)
        attrs = {'Maps': self.Maps}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTextureCoordinateGenerator(IfcTextureCoordinate):
    def __init__(self, rtype, args):
        IfcTextureCoordinate.__init__(self, rtype, args)
        self.Mode = args.pop()
        self.Parameter = args.pop()

    def __str__(self):
        return "{sup}:Mode:{Mode}:Parameter:{Parameter}".format(
            sup=IfcTextureCoordinate.__str__(self),
            Mode=self.Mode,
            Parameter=self.Parameter,
        )

    def __json__(self):
        sup = IfcTextureCoordinate.__json__(self)
        attrs = {'Mode': self.Mode, 'Parameter': self.Parameter}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTextureMap(IfcTextureCoordinate):
    def __init__(self, rtype, args):
        IfcTextureCoordinate.__init__(self, rtype, args)
        self.Vertices = args.pop()
        self.MappedTo = args.pop()

    def __str__(self):
        return "{sup}:Vertices:{Vertices}:MappedTo:{MappedTo}".format(
            sup=IfcTextureCoordinate.__str__(self),
            Vertices=self.Vertices,
            MappedTo=self.MappedTo,
        )

    def __json__(self):
        sup = IfcTextureCoordinate.__json__(self)
        attrs = {'Vertices': self.Vertices, 'MappedTo': self.MappedTo}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTextureVertex(IfcPresentationItem):
    def __init__(self, rtype, args):
        IfcPresentationItem.__init__(self, rtype, args)
        self.Coordinates = args.pop()

    def __str__(self):
        return "{sup}:Coordinates:{Coordinates}".format(
            sup=IfcPresentationItem.__str__(self),
            Coordinates=self.Coordinates,
        )

    def __json__(self):
        sup = IfcPresentationItem.__json__(self)
        attrs = {'Coordinates': self.Coordinates}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTextureVertexList(IfcPresentationItem):
    def __init__(self, rtype, args):
        IfcPresentationItem.__init__(self, rtype, args)
        self.TexCoordsList = args.pop()

    def __str__(self):
        return "{sup}:TexCoordsList:{TexCoordsList}".format(
            sup=IfcPresentationItem.__str__(self),
            TexCoordsList=self.TexCoordsList,
        )

    def __json__(self):
        sup = IfcPresentationItem.__json__(self)
        attrs = {'TexCoordsList': self.TexCoordsList}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTimePeriod(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.StartTime = args.pop()
        self.EndTime = args.pop()

    def __str__(self):
        return "{sup}:StartTime:{StartTime}:EndTime:{EndTime}".format(
            sup=IfcEntity.__str__(self),
            StartTime=self.StartTime,
            EndTime=self.EndTime,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'StartTime': self.StartTime, 'EndTime': self.EndTime}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcTimeSeries(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Name = args.pop()
        self.Description = args.pop()
        self.StartTime = args.pop()
        self.EndTime = args.pop()
        self.TimeSeriesDataType = args.pop()
        self.DataOrigin = args.pop()
        self.UserDefinedDataOrigin = args.pop()
        self.Unit = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:Description:{Description}:StartTime:{StartTime}:EndTime:{EndTime}:TimeSeriesDataType:{TimeSeriesDataType}:DataOrigin:{DataOrigin}:UserDefinedDataOrigin:{UserDefinedDataOrigin}:Unit:{Unit}".format(
            sup=IfcEntity.__str__(self),
            Name=self.Name,
            Description=self.Description,
            StartTime=self.StartTime,
            EndTime=self.EndTime,
            TimeSeriesDataType=self.TimeSeriesDataType,
            DataOrigin=self.DataOrigin,
            UserDefinedDataOrigin=self.UserDefinedDataOrigin,
            Unit=self.Unit,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Name': self.Name, 'Description': self.Description, 'StartTime': self.StartTime,
                 'EndTime': self.EndTime, 'TimeSeriesDataType': self.TimeSeriesDataType, 'DataOrigin': self.DataOrigin,
                 'UserDefinedDataOrigin': self.UserDefinedDataOrigin, 'Unit': self.Unit}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTimeSeriesValue(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.ListValues = args.pop()

    def __str__(self):
        return "{sup}:ListValues:{ListValues}".format(
            sup=IfcEntity.__str__(self),
            ListValues=self.ListValues,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'ListValues': self.ListValues}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcTopologicalRepresentationItem(IfcRepresentationItem):
    def __init__(self, rtype, args):
        IfcRepresentationItem.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcRepresentationItem.__str__(self),
        )

    def __json__(self):
        sup = IfcRepresentationItem.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTopologyRepresentation(IfcShapeModel):
    def __init__(self, rtype, args):
        IfcShapeModel.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcShapeModel.__str__(self),
        )

    def __json__(self):
        sup = IfcShapeModel.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcUnitAssignment(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.Units = args.pop()

    def __str__(self):
        return "{sup}:Units:{Units}".format(
            sup=IfcEntity.__str__(self),
            Units=self.Units,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'Units': self.Units}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcVertex(IfcTopologicalRepresentationItem):
    def __init__(self, rtype, args):
        IfcTopologicalRepresentationItem.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcTopologicalRepresentationItem.__str__(self),
        )

    def __json__(self):
        sup = IfcTopologicalRepresentationItem.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcVertexPoint(IfcVertex):
    def __init__(self, rtype, args):
        IfcVertex.__init__(self, rtype, args)
        self.VertexGeometry = args.pop()

    def __str__(self):
        return "{sup}:VertexGeometry:{VertexGeometry}".format(
            sup=IfcVertex.__str__(self),
            VertexGeometry=self.VertexGeometry,
        )

    def __json__(self):
        sup = IfcVertex.__json__(self)
        attrs = {'VertexGeometry': self.VertexGeometry}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcVirtualGridIntersection(IfcEntity):
    def __init__(self, rtype, args):
        IfcEntity.__init__(self, rtype, args)
        self.IntersectingAxes = args.pop()
        self.OffsetDistances = args.pop()

    def __str__(self):
        return "{sup}:IntersectingAxes:{IntersectingAxes}:OffsetDistances:{OffsetDistances}".format(
            sup=IfcEntity.__str__(self),
            IntersectingAxes=self.IntersectingAxes,
            OffsetDistances=self.OffsetDistances,
        )

    def __json__(self):
        sup = IfcEntity.__json__(self)
        attrs = {'IntersectingAxes': self.IntersectingAxes, 'OffsetDistances': self.OffsetDistances}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcWorkTime(IfcSchedulingTime):
    def __init__(self, rtype, args):
        IfcSchedulingTime.__init__(self, rtype, args)
        self.RecurrencePattern = args.pop()
        self.Start = args.pop()
        self.Finish = args.pop()

    def __str__(self):
        return "{sup}:RecurrencePattern:{RecurrencePattern}:Start:{Start}:Finish:{Finish}".format(
            sup=IfcSchedulingTime.__str__(self),
            RecurrencePattern=self.RecurrencePattern,
            Start=self.Start,
            Finish=self.Finish,
        )

    def __json__(self):
        sup = IfcSchedulingTime.__json__(self)
        attrs = {'RecurrencePattern': self.RecurrencePattern, 'Start': self.Start, 'Finish': self.Finish}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcApprovalRelationship(IfcResourceLevelRelationship):
    def __init__(self, rtype, args):
        IfcResourceLevelRelationship.__init__(self, rtype, args)
        self.RelatingApproval = args.pop()
        self.RelatedApprovals = args.pop()

    def __str__(self):
        return "{sup}:RelatingApproval:{RelatingApproval}:RelatedApprovals:{RelatedApprovals}".format(
            sup=IfcResourceLevelRelationship.__str__(self),
            RelatingApproval=self.RelatingApproval,
            RelatedApprovals=self.RelatedApprovals,
        )

    def __json__(self):
        sup = IfcResourceLevelRelationship.__json__(self)
        attrs = {'RelatingApproval': self.RelatingApproval, 'RelatedApprovals': self.RelatedApprovals}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcArbitraryClosedProfileDef(IfcProfileDef):
    def __init__(self, rtype, args):
        IfcProfileDef.__init__(self, rtype, args)
        self.OuterCurve = args.pop()

    def __str__(self):
        return "{sup}:OuterCurve:{OuterCurve}".format(
            sup=IfcProfileDef.__str__(self),
            OuterCurve=self.OuterCurve,
        )

    def __json__(self):
        sup = IfcProfileDef.__json__(self)
        attrs = {'OuterCurve': self.OuterCurve}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcArbitraryOpenProfileDef(IfcProfileDef):
    def __init__(self, rtype, args):
        IfcProfileDef.__init__(self, rtype, args)
        self.Curve = args.pop()

    def __str__(self):
        return "{sup}:Curve:{Curve}".format(
            sup=IfcProfileDef.__str__(self),
            Curve=self.Curve,
        )

    def __json__(self):
        sup = IfcProfileDef.__json__(self)
        attrs = {'Curve': self.Curve}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcArbitraryProfileDefWithVoids(IfcArbitraryClosedProfileDef):
    def __init__(self, rtype, args):
        IfcArbitraryClosedProfileDef.__init__(self, rtype, args)
        self.InnerCurves = args.pop()

    def __str__(self):
        return "{sup}:InnerCurves:{InnerCurves}".format(
            sup=IfcArbitraryClosedProfileDef.__str__(self),
            InnerCurves=self.InnerCurves,
        )

    def __json__(self):
        sup = IfcArbitraryClosedProfileDef.__json__(self)
        attrs = {'InnerCurves': self.InnerCurves}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBlobTexture(IfcSurfaceTexture):
    def __init__(self, rtype, args):
        IfcSurfaceTexture.__init__(self, rtype, args)
        self.RasterFormat = args.pop()
        self.RasterCode = args.pop()

    def __str__(self):
        return "{sup}:RasterFormat:{RasterFormat}:RasterCode:{RasterCode}".format(
            sup=IfcSurfaceTexture.__str__(self),
            RasterFormat=self.RasterFormat,
            RasterCode=self.RasterCode,
        )

    def __json__(self):
        sup = IfcSurfaceTexture.__json__(self)
        attrs = {'RasterFormat': self.RasterFormat, 'RasterCode': self.RasterCode}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCenterLineProfileDef(IfcArbitraryOpenProfileDef):
    def __init__(self, rtype, args):
        IfcArbitraryOpenProfileDef.__init__(self, rtype, args)
        self.Thickness = args.pop()

    def __str__(self):
        return "{sup}:Thickness:{Thickness}".format(
            sup=IfcArbitraryOpenProfileDef.__str__(self),
            Thickness=self.Thickness,
        )

    def __json__(self):
        sup = IfcArbitraryOpenProfileDef.__json__(self)
        attrs = {'Thickness': self.Thickness}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcClassification(IfcExternalInformation):
    def __init__(self, rtype, args):
        IfcExternalInformation.__init__(self, rtype, args)
        self.Source = args.pop()
        self.Edition = args.pop()
        self.EditionDate = args.pop()
        self.Name = args.pop()
        self.Description = args.pop()
        self.Location = args.pop()
        self.ReferenceTokens = args.pop()

    def __str__(self):
        return "{sup}:Source:{Source}:Edition:{Edition}:EditionDate:{EditionDate}:Name:{Name}:Description:{Description}:Location:{Location}:ReferenceTokens:{ReferenceTokens}".format(
            sup=IfcExternalInformation.__str__(self),
            Source=self.Source,
            Edition=self.Edition,
            EditionDate=self.EditionDate,
            Name=self.Name,
            Description=self.Description,
            Location=self.Location,
            ReferenceTokens=self.ReferenceTokens,
        )

    def __json__(self):
        sup = IfcExternalInformation.__json__(self)
        attrs = {'Source': self.Source, 'Edition': self.Edition, 'EditionDate': self.EditionDate, 'Name': self.Name,
                 'Description': self.Description, 'Location': self.Location, 'ReferenceTokens': self.ReferenceTokens}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcClassificationReference(IfcExternalReference):
    def __init__(self, rtype, args):
        IfcExternalReference.__init__(self, rtype, args)
        self.ReferencedSource = args.pop()
        self.Description = args.pop()
        self.Sort = args.pop()

    def __str__(self):
        return "{sup}:ReferencedSource:{ReferencedSource}:Description:{Description}:Sort:{Sort}".format(
            sup=IfcExternalReference.__str__(self),
            ReferencedSource=self.ReferencedSource,
            Description=self.Description,
            Sort=self.Sort,
        )

    def __json__(self):
        sup = IfcExternalReference.__json__(self)
        attrs = {'ReferencedSource': self.ReferencedSource, 'Description': self.Description, 'Sort': self.Sort}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcColourRgbList(IfcPresentationItem):
    def __init__(self, rtype, args):
        IfcPresentationItem.__init__(self, rtype, args)
        self.ColourList = args.pop()

    def __str__(self):
        return "{sup}:ColourList:{ColourList}".format(
            sup=IfcPresentationItem.__str__(self),
            ColourList=self.ColourList,
        )

    def __json__(self):
        sup = IfcPresentationItem.__json__(self)
        attrs = {'ColourList': self.ColourList}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcColourSpecification(IfcPresentationItem):
    def __init__(self, rtype, args):
        IfcPresentationItem.__init__(self, rtype, args)
        self.Name = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}".format(
            sup=IfcPresentationItem.__str__(self),
            Name=self.Name,
        )

    def __json__(self):
        sup = IfcPresentationItem.__json__(self)
        attrs = {'Name': self.Name}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCompositeProfileDef(IfcProfileDef):
    def __init__(self, rtype, args):
        IfcProfileDef.__init__(self, rtype, args)
        self.Profiles = args.pop()
        self.Label = args.pop()

    def __str__(self):
        return "{sup}:Profiles:{Profiles}:Label:{Label}".format(
            sup=IfcProfileDef.__str__(self),
            Profiles=self.Profiles,
            Label=self.Label,
        )

    def __json__(self):
        sup = IfcProfileDef.__json__(self)
        attrs = {'Profiles': self.Profiles, 'Label': self.Label}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcConnectedFaceSet(IfcTopologicalRepresentationItem):
    def __init__(self, rtype, args):
        IfcTopologicalRepresentationItem.__init__(self, rtype, args)
        self.CfsFaces = args.pop()

    def __str__(self):
        return "{sup}:CfsFaces:{CfsFaces}".format(
            sup=IfcTopologicalRepresentationItem.__str__(self),
            CfsFaces=self.CfsFaces,
        )

    def __json__(self):
        sup = IfcTopologicalRepresentationItem.__json__(self)
        attrs = {'CfsFaces': self.CfsFaces}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcConnectionCurveGeometry(IfcConnectionGeometry):
    def __init__(self, rtype, args):
        IfcConnectionGeometry.__init__(self, rtype, args)
        self.CurveOnRelatingElement = args.pop()
        self.CurveOnRelatedElement = args.pop()

    def __str__(self):
        return "{sup}:CurveOnRelatingElement:{CurveOnRelatingElement}:CurveOnRelatedElement:{CurveOnRelatedElement}".format(
            sup=IfcConnectionGeometry.__str__(self),
            CurveOnRelatingElement=self.CurveOnRelatingElement,
            CurveOnRelatedElement=self.CurveOnRelatedElement,
        )

    def __json__(self):
        sup = IfcConnectionGeometry.__json__(self)
        attrs = {'CurveOnRelatingElement': self.CurveOnRelatingElement,
                 'CurveOnRelatedElement': self.CurveOnRelatedElement}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcConnectionPointEccentricity(IfcConnectionPointGeometry):
    def __init__(self, rtype, args):
        IfcConnectionPointGeometry.__init__(self, rtype, args)
        self.EccentricityInX = args.pop()
        self.EccentricityInY = args.pop()
        self.EccentricityInZ = args.pop()

    def __str__(self):
        return "{sup}:EccentricityInX:{EccentricityInX}:EccentricityInY:{EccentricityInY}:EccentricityInZ:{EccentricityInZ}".format(
            sup=IfcConnectionPointGeometry.__str__(self),
            EccentricityInX=self.EccentricityInX,
            EccentricityInY=self.EccentricityInY,
            EccentricityInZ=self.EccentricityInZ,
        )

    def __json__(self):
        sup = IfcConnectionPointGeometry.__json__(self)
        attrs = {'EccentricityInX': self.EccentricityInX, 'EccentricityInY': self.EccentricityInY,
                 'EccentricityInZ': self.EccentricityInZ}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcContextDependentUnit(IfcNamedUnit):
    def __init__(self, rtype, args):
        IfcNamedUnit.__init__(self, rtype, args)
        self.Name = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}".format(
            sup=IfcNamedUnit.__str__(self),
            Name=self.Name,
        )

    def __json__(self):
        sup = IfcNamedUnit.__json__(self)
        attrs = {'Name': self.Name}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcConversionBasedUnit(IfcNamedUnit):
    def __init__(self, rtype, args):
        IfcNamedUnit.__init__(self, rtype, args)
        self.Name = args.pop()
        self.ConversionFactor = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:ConversionFactor:{ConversionFactor}".format(
            sup=IfcNamedUnit.__str__(self),
            Name=self.Name,
            ConversionFactor=self.ConversionFactor,
        )

    def __json__(self):
        sup = IfcNamedUnit.__json__(self)
        attrs = {'Name': self.Name, 'ConversionFactor': self.ConversionFactor}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcConversionBasedUnitWithOffset(IfcConversionBasedUnit):
    def __init__(self, rtype, args):
        IfcConversionBasedUnit.__init__(self, rtype, args)
        self.ConversionOffset = args.pop()

    def __str__(self):
        return "{sup}:ConversionOffset:{ConversionOffset}".format(
            sup=IfcConversionBasedUnit.__str__(self),
            ConversionOffset=self.ConversionOffset,
        )

    def __json__(self):
        sup = IfcConversionBasedUnit.__json__(self)
        attrs = {'ConversionOffset': self.ConversionOffset}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCurrencyRelationship(IfcResourceLevelRelationship):
    def __init__(self, rtype, args):
        IfcResourceLevelRelationship.__init__(self, rtype, args)
        self.RelatingMonetaryUnit = args.pop()
        self.RelatedMonetaryUnit = args.pop()
        self.ExchangeRate = args.pop()
        self.RateDateTime = args.pop()
        self.RateSource = args.pop()

    def __str__(self):
        return "{sup}:RelatingMonetaryUnit:{RelatingMonetaryUnit}:RelatedMonetaryUnit:{RelatedMonetaryUnit}:ExchangeRate:{ExchangeRate}:RateDateTime:{RateDateTime}:RateSource:{RateSource}".format(
            sup=IfcResourceLevelRelationship.__str__(self),
            RelatingMonetaryUnit=self.RelatingMonetaryUnit,
            RelatedMonetaryUnit=self.RelatedMonetaryUnit,
            ExchangeRate=self.ExchangeRate,
            RateDateTime=self.RateDateTime,
            RateSource=self.RateSource,
        )

    def __json__(self):
        sup = IfcResourceLevelRelationship.__json__(self)
        attrs = {'RelatingMonetaryUnit': self.RelatingMonetaryUnit, 'RelatedMonetaryUnit': self.RelatedMonetaryUnit,
                 'ExchangeRate': self.ExchangeRate, 'RateDateTime': self.RateDateTime, 'RateSource': self.RateSource}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCurveStyle(IfcPresentationStyle):
    def __init__(self, rtype, args):
        IfcPresentationStyle.__init__(self, rtype, args)
        self.CurveFont = args.pop()
        self.CurveWidth = args.pop()
        self.CurveColour = args.pop()
        self.ModelOrDraughting = args.pop()

    def __str__(self):
        return "{sup}:CurveFont:{CurveFont}:CurveWidth:{CurveWidth}:CurveColour:{CurveColour}:ModelOrDraughting:{ModelOrDraughting}".format(
            sup=IfcPresentationStyle.__str__(self),
            CurveFont=self.CurveFont,
            CurveWidth=self.CurveWidth,
            CurveColour=self.CurveColour,
            ModelOrDraughting=self.ModelOrDraughting,
        )

    def __json__(self):
        sup = IfcPresentationStyle.__json__(self)
        attrs = {'CurveFont': self.CurveFont, 'CurveWidth': self.CurveWidth, 'CurveColour': self.CurveColour,
                 'ModelOrDraughting': self.ModelOrDraughting}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCurveStyleFont(IfcPresentationItem):
    def __init__(self, rtype, args):
        IfcPresentationItem.__init__(self, rtype, args)
        self.Name = args.pop()
        self.PatternList = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:PatternList:{PatternList}".format(
            sup=IfcPresentationItem.__str__(self),
            Name=self.Name,
            PatternList=self.PatternList,
        )

    def __json__(self):
        sup = IfcPresentationItem.__json__(self)
        attrs = {'Name': self.Name, 'PatternList': self.PatternList}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCurveStyleFontAndScaling(IfcPresentationItem):
    def __init__(self, rtype, args):
        IfcPresentationItem.__init__(self, rtype, args)
        self.Name = args.pop()
        self.CurveFont = args.pop()
        self.CurveFontScaling = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:CurveFont:{CurveFont}:CurveFontScaling:{CurveFontScaling}".format(
            sup=IfcPresentationItem.__str__(self),
            Name=self.Name,
            CurveFont=self.CurveFont,
            CurveFontScaling=self.CurveFontScaling,
        )

    def __json__(self):
        sup = IfcPresentationItem.__json__(self)
        attrs = {'Name': self.Name, 'CurveFont': self.CurveFont, 'CurveFontScaling': self.CurveFontScaling}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCurveStyleFontPattern(IfcPresentationItem):
    def __init__(self, rtype, args):
        IfcPresentationItem.__init__(self, rtype, args)
        self.VisibleSegmentLength = args.pop()
        self.InvisibleSegmentLength = args.pop()

    def __str__(self):
        return "{sup}:VisibleSegmentLength:{VisibleSegmentLength}:InvisibleSegmentLength:{InvisibleSegmentLength}".format(
            sup=IfcPresentationItem.__str__(self),
            VisibleSegmentLength=self.VisibleSegmentLength,
            InvisibleSegmentLength=self.InvisibleSegmentLength,
        )

    def __json__(self):
        sup = IfcPresentationItem.__json__(self)
        attrs = {'VisibleSegmentLength': self.VisibleSegmentLength,
                 'InvisibleSegmentLength': self.InvisibleSegmentLength}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDerivedProfileDef(IfcProfileDef):
    def __init__(self, rtype, args):
        IfcProfileDef.__init__(self, rtype, args)
        self.ParentProfile = args.pop()
        self.Operator = args.pop()
        self.Label = args.pop()

    def __str__(self):
        return "{sup}:ParentProfile:{ParentProfile}:Operator:{Operator}:Label:{Label}".format(
            sup=IfcProfileDef.__str__(self),
            ParentProfile=self.ParentProfile,
            Operator=self.Operator,
            Label=self.Label,
        )

    def __json__(self):
        sup = IfcProfileDef.__json__(self)
        attrs = {'ParentProfile': self.ParentProfile, 'Operator': self.Operator, 'Label': self.Label}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDocumentInformation(IfcExternalInformation):
    def __init__(self, rtype, args):
        IfcExternalInformation.__init__(self, rtype, args)
        self.Identification = args.pop()
        self.Name = args.pop()
        self.Description = args.pop()
        self.Location = args.pop()
        self.Purpose = args.pop()
        self.IntendedUse = args.pop()
        self.Scope = args.pop()
        self.Revision = args.pop()
        self.DocumentOwner = args.pop()
        self.Editors = args.pop()
        self.CreationTime = args.pop()
        self.LastRevisionTime = args.pop()
        self.ElectronicFormat = args.pop()
        self.ValidFrom = args.pop()
        self.ValidUntil = args.pop()
        self.Confidentiality = args.pop()
        self.Status = args.pop()

    def __str__(self):
        return "{sup}:Identification:{Identification}:Name:{Name}:Description:{Description}:Location:{Location}:Purpose:{Purpose}:IntendedUse:{IntendedUse}:Scope:{Scope}:Revision:{Revision}:DocumentOwner:{DocumentOwner}:Editors:{Editors}:CreationTime:{CreationTime}:LastRevisionTime:{LastRevisionTime}:ElectronicFormat:{ElectronicFormat}:ValidFrom:{ValidFrom}:ValidUntil:{ValidUntil}:Confidentiality:{Confidentiality}:Status:{Status}".format(
            sup=IfcExternalInformation.__str__(self),
            Identification=self.Identification,
            Name=self.Name,
            Description=self.Description,
            Location=self.Location,
            Purpose=self.Purpose,
            IntendedUse=self.IntendedUse,
            Scope=self.Scope,
            Revision=self.Revision,
            DocumentOwner=self.DocumentOwner,
            Editors=self.Editors,
            CreationTime=self.CreationTime,
            LastRevisionTime=self.LastRevisionTime,
            ElectronicFormat=self.ElectronicFormat,
            ValidFrom=self.ValidFrom,
            ValidUntil=self.ValidUntil,
            Confidentiality=self.Confidentiality,
            Status=self.Status,
        )

    def __json__(self):
        sup = IfcExternalInformation.__json__(self)
        attrs = {'Identification': self.Identification, 'Name': self.Name, 'Description': self.Description,
                 'Location': self.Location, 'Purpose': self.Purpose, 'IntendedUse': self.IntendedUse,
                 'Scope': self.Scope, 'Revision': self.Revision, 'DocumentOwner': self.DocumentOwner,
                 'Editors': self.Editors, 'CreationTime': self.CreationTime, 'LastRevisionTime': self.LastRevisionTime,
                 'ElectronicFormat': self.ElectronicFormat, 'ValidFrom': self.ValidFrom, 'ValidUntil': self.ValidUntil,
                 'Confidentiality': self.Confidentiality, 'Status': self.Status}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDocumentInformationRelationship(IfcResourceLevelRelationship):
    def __init__(self, rtype, args):
        IfcResourceLevelRelationship.__init__(self, rtype, args)
        self.RelatingDocument = args.pop()
        self.RelatedDocuments = args.pop()
        self.RelationshipType = args.pop()

    def __str__(self):
        return "{sup}:RelatingDocument:{RelatingDocument}:RelatedDocuments:{RelatedDocuments}:RelationshipType:{RelationshipType}".format(
            sup=IfcResourceLevelRelationship.__str__(self),
            RelatingDocument=self.RelatingDocument,
            RelatedDocuments=self.RelatedDocuments,
            RelationshipType=self.RelationshipType,
        )

    def __json__(self):
        sup = IfcResourceLevelRelationship.__json__(self)
        attrs = {'RelatingDocument': self.RelatingDocument, 'RelatedDocuments': self.RelatedDocuments,
                 'RelationshipType': self.RelationshipType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDocumentReference(IfcExternalReference):
    def __init__(self, rtype, args):
        IfcExternalReference.__init__(self, rtype, args)
        self.Description = args.pop()
        self.ReferencedDocument = args.pop()

    def __str__(self):
        return "{sup}:Description:{Description}:ReferencedDocument:{ReferencedDocument}".format(
            sup=IfcExternalReference.__str__(self),
            Description=self.Description,
            ReferencedDocument=self.ReferencedDocument,
        )

    def __json__(self):
        sup = IfcExternalReference.__json__(self)
        attrs = {'Description': self.Description, 'ReferencedDocument': self.ReferencedDocument}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcEdge(IfcTopologicalRepresentationItem):
    def __init__(self, rtype, args):
        IfcTopologicalRepresentationItem.__init__(self, rtype, args)
        self.EdgeStart = args.pop()
        self.EdgeEnd = args.pop()

    def __str__(self):
        return "{sup}:EdgeStart:{EdgeStart}:EdgeEnd:{EdgeEnd}".format(
            sup=IfcTopologicalRepresentationItem.__str__(self),
            EdgeStart=self.EdgeStart,
            EdgeEnd=self.EdgeEnd,
        )

    def __json__(self):
        sup = IfcTopologicalRepresentationItem.__json__(self)
        attrs = {'EdgeStart': self.EdgeStart, 'EdgeEnd': self.EdgeEnd}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcEdgeCurve(IfcEdge):
    def __init__(self, rtype, args):
        IfcEdge.__init__(self, rtype, args)
        self.EdgeGeometry = args.pop()
        self.SameSense = args.pop()

    def __str__(self):
        return "{sup}:EdgeGeometry:{EdgeGeometry}:SameSense:{SameSense}".format(
            sup=IfcEdge.__str__(self),
            EdgeGeometry=self.EdgeGeometry,
            SameSense=self.SameSense,
        )

    def __json__(self):
        sup = IfcEdge.__json__(self)
        attrs = {'EdgeGeometry': self.EdgeGeometry, 'SameSense': self.SameSense}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcEventTime(IfcSchedulingTime):
    def __init__(self, rtype, args):
        IfcSchedulingTime.__init__(self, rtype, args)
        self.ActualDate = args.pop()
        self.EarlyDate = args.pop()
        self.LateDate = args.pop()
        self.ScheduleDate = args.pop()

    def __str__(self):
        return "{sup}:ActualDate:{ActualDate}:EarlyDate:{EarlyDate}:LateDate:{LateDate}:ScheduleDate:{ScheduleDate}".format(
            sup=IfcSchedulingTime.__str__(self),
            ActualDate=self.ActualDate,
            EarlyDate=self.EarlyDate,
            LateDate=self.LateDate,
            ScheduleDate=self.ScheduleDate,
        )

    def __json__(self):
        sup = IfcSchedulingTime.__json__(self)
        attrs = {'ActualDate': self.ActualDate, 'EarlyDate': self.EarlyDate, 'LateDate': self.LateDate,
                 'ScheduleDate': self.ScheduleDate}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcExtendedProperties(IfcPropertyAbstraction):
    def __init__(self, rtype, args):
        IfcPropertyAbstraction.__init__(self, rtype, args)
        self.Name = args.pop()
        self.Description = args.pop()
        self.Properties = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:Description:{Description}:Properties:{Properties}".format(
            sup=IfcPropertyAbstraction.__str__(self),
            Name=self.Name,
            Description=self.Description,
            Properties=self.Properties,
        )

    def __json__(self):
        sup = IfcPropertyAbstraction.__json__(self)
        attrs = {'Name': self.Name, 'Description': self.Description, 'Properties': self.Properties}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcExternalReferenceRelationship(IfcResourceLevelRelationship):
    def __init__(self, rtype, args):
        IfcResourceLevelRelationship.__init__(self, rtype, args)
        self.RelatingReference = args.pop()
        self.RelatedResourceObjects = args.pop()

    def __str__(self):
        return "{sup}:RelatingReference:{RelatingReference}:RelatedResourceObjects:{RelatedResourceObjects}".format(
            sup=IfcResourceLevelRelationship.__str__(self),
            RelatingReference=self.RelatingReference,
            RelatedResourceObjects=self.RelatedResourceObjects,
        )

    def __json__(self):
        sup = IfcResourceLevelRelationship.__json__(self)
        attrs = {'RelatingReference': self.RelatingReference, 'RelatedResourceObjects': self.RelatedResourceObjects}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFace(IfcTopologicalRepresentationItem):
    def __init__(self, rtype, args):
        IfcTopologicalRepresentationItem.__init__(self, rtype, args)
        self.Bounds = args.pop()

    def __str__(self):
        return "{sup}:Bounds:{Bounds}".format(
            sup=IfcTopologicalRepresentationItem.__str__(self),
            Bounds=self.Bounds,
        )

    def __json__(self):
        sup = IfcTopologicalRepresentationItem.__json__(self)
        attrs = {'Bounds': self.Bounds}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFaceBound(IfcTopologicalRepresentationItem):
    def __init__(self, rtype, args):
        IfcTopologicalRepresentationItem.__init__(self, rtype, args)
        self.Bound = args.pop()
        self.Orientation = args.pop()

    def __str__(self):
        return "{sup}:Bound:{Bound}:Orientation:{Orientation}".format(
            sup=IfcTopologicalRepresentationItem.__str__(self),
            Bound=self.Bound,
            Orientation=self.Orientation,
        )

    def __json__(self):
        sup = IfcTopologicalRepresentationItem.__json__(self)
        attrs = {'Bound': self.Bound, 'Orientation': self.Orientation}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFaceOuterBound(IfcFaceBound):
    def __init__(self, rtype, args):
        IfcFaceBound.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcFaceBound.__str__(self),
        )

    def __json__(self):
        sup = IfcFaceBound.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFaceSurface(IfcFace):
    def __init__(self, rtype, args):
        IfcFace.__init__(self, rtype, args)
        self.FaceSurface = args.pop()
        self.SameSense = args.pop()

    def __str__(self):
        return "{sup}:FaceSurface:{FaceSurface}:SameSense:{SameSense}".format(
            sup=IfcFace.__str__(self),
            FaceSurface=self.FaceSurface,
            SameSense=self.SameSense,
        )

    def __json__(self):
        sup = IfcFace.__json__(self)
        attrs = {'FaceSurface': self.FaceSurface, 'SameSense': self.SameSense}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFailureConnectionCondition(IfcStructuralConnectionCondition):
    def __init__(self, rtype, args):
        IfcStructuralConnectionCondition.__init__(self, rtype, args)
        self.TensionFailureX = args.pop()
        self.TensionFailureY = args.pop()
        self.TensionFailureZ = args.pop()
        self.CompressionFailureX = args.pop()
        self.CompressionFailureY = args.pop()
        self.CompressionFailureZ = args.pop()

    def __str__(self):
        return "{sup}:TensionFailureX:{TensionFailureX}:TensionFailureY:{TensionFailureY}:TensionFailureZ:{TensionFailureZ}:CompressionFailureX:{CompressionFailureX}:CompressionFailureY:{CompressionFailureY}:CompressionFailureZ:{CompressionFailureZ}".format(
            sup=IfcStructuralConnectionCondition.__str__(self),
            TensionFailureX=self.TensionFailureX,
            TensionFailureY=self.TensionFailureY,
            TensionFailureZ=self.TensionFailureZ,
            CompressionFailureX=self.CompressionFailureX,
            CompressionFailureY=self.CompressionFailureY,
            CompressionFailureZ=self.CompressionFailureZ,
        )

    def __json__(self):
        sup = IfcStructuralConnectionCondition.__json__(self)
        attrs = {'TensionFailureX': self.TensionFailureX, 'TensionFailureY': self.TensionFailureY,
                 'TensionFailureZ': self.TensionFailureZ, 'CompressionFailureX': self.CompressionFailureX,
                 'CompressionFailureY': self.CompressionFailureY, 'CompressionFailureZ': self.CompressionFailureZ}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFillAreaStyle(IfcPresentationStyle):
    def __init__(self, rtype, args):
        IfcPresentationStyle.__init__(self, rtype, args)
        self.FillStyles = args.pop()
        self.ModelorDraughting = args.pop()

    def __str__(self):
        return "{sup}:FillStyles:{FillStyles}:ModelorDraughting:{ModelorDraughting}".format(
            sup=IfcPresentationStyle.__str__(self),
            FillStyles=self.FillStyles,
            ModelorDraughting=self.ModelorDraughting,
        )

    def __json__(self):
        sup = IfcPresentationStyle.__json__(self)
        attrs = {'FillStyles': self.FillStyles, 'ModelorDraughting': self.ModelorDraughting}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcGeometricRepresentationContext(IfcRepresentationContext):
    def __init__(self, rtype, args):
        IfcRepresentationContext.__init__(self, rtype, args)
        self.CoordinateSpaceDimension = args.pop()
        self.Precision = args.pop()
        self.WorldCoordinateSystem = args.pop()
        self.TrueNorth = args.pop()

    def __str__(self):
        return "{sup}:CoordinateSpaceDimension:{CoordinateSpaceDimension}:Precision:{Precision}:WorldCoordinateSystem:{WorldCoordinateSystem}:TrueNorth:{TrueNorth}".format(
            sup=IfcRepresentationContext.__str__(self),
            CoordinateSpaceDimension=self.CoordinateSpaceDimension,
            Precision=self.Precision,
            WorldCoordinateSystem=self.WorldCoordinateSystem,
            TrueNorth=self.TrueNorth,
        )

    def __json__(self):
        sup = IfcRepresentationContext.__json__(self)
        attrs = {'CoordinateSpaceDimension': self.CoordinateSpaceDimension, 'Precision': self.Precision,
                 'WorldCoordinateSystem': self.WorldCoordinateSystem, 'TrueNorth': self.TrueNorth}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcGeometricRepresentationItem(IfcRepresentationItem):
    def __init__(self, rtype, args):
        IfcRepresentationItem.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcRepresentationItem.__str__(self),
        )

    def __json__(self):
        sup = IfcRepresentationItem.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcGeometricRepresentationSubContext(IfcGeometricRepresentationContext):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationContext.__init__(self, rtype, args)
        self.ParentContext = args.pop()
        self.TargetScale = args.pop()
        self.TargetView = args.pop()
        self.UserDefinedTargetView = args.pop()

    def __str__(self):
        return "{sup}:ParentContext:{ParentContext}:TargetScale:{TargetScale}:TargetView:{TargetView}:UserDefinedTargetView:{UserDefinedTargetView}".format(
            sup=IfcGeometricRepresentationContext.__str__(self),
            ParentContext=self.ParentContext,
            TargetScale=self.TargetScale,
            TargetView=self.TargetView,
            UserDefinedTargetView=self.UserDefinedTargetView,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationContext.__json__(self)
        attrs = {'ParentContext': self.ParentContext, 'TargetScale': self.TargetScale, 'TargetView': self.TargetView,
                 'UserDefinedTargetView': self.UserDefinedTargetView}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcGeometricSet(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.Elements = args.pop()

    def __str__(self):
        return "{sup}:Elements:{Elements}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            Elements=self.Elements,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'Elements': self.Elements}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcGridPlacement(IfcObjectPlacement):
    def __init__(self, rtype, args):
        IfcObjectPlacement.__init__(self, rtype, args)
        self.PlacementLocation = args.pop()
        self.PlacementRefDirection = args.pop()

    def __str__(self):
        return "{sup}:PlacementLocation:{PlacementLocation}:PlacementRefDirection:{PlacementRefDirection}".format(
            sup=IfcObjectPlacement.__str__(self),
            PlacementLocation=self.PlacementLocation,
            PlacementRefDirection=self.PlacementRefDirection,
        )

    def __json__(self):
        sup = IfcObjectPlacement.__json__(self)
        attrs = {'PlacementLocation': self.PlacementLocation, 'PlacementRefDirection': self.PlacementRefDirection}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcHalfSpaceSolid(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.BaseSurface = args.pop()
        self.AgreementFlag = args.pop()

    def __str__(self):
        return "{sup}:BaseSurface:{BaseSurface}:AgreementFlag:{AgreementFlag}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            BaseSurface=self.BaseSurface,
            AgreementFlag=self.AgreementFlag,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'BaseSurface': self.BaseSurface, 'AgreementFlag': self.AgreementFlag}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcImageTexture(IfcSurfaceTexture):
    def __init__(self, rtype, args):
        IfcSurfaceTexture.__init__(self, rtype, args)
        self.URLReference = args.pop()

    def __str__(self):
        return "{sup}:URLReference:{URLReference}".format(
            sup=IfcSurfaceTexture.__str__(self),
            URLReference=self.URLReference,
        )

    def __json__(self):
        sup = IfcSurfaceTexture.__json__(self)
        attrs = {'URLReference': self.URLReference}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcIndexedColourMap(IfcPresentationItem):
    def __init__(self, rtype, args):
        IfcPresentationItem.__init__(self, rtype, args)
        self.MappedTo = args.pop()
        self.Opacity = args.pop()
        self.Colours = args.pop()
        self.ColourIndex = args.pop()

    def __str__(self):
        return "{sup}:MappedTo:{MappedTo}:Opacity:{Opacity}:Colours:{Colours}:ColourIndex:{ColourIndex}".format(
            sup=IfcPresentationItem.__str__(self),
            MappedTo=self.MappedTo,
            Opacity=self.Opacity,
            Colours=self.Colours,
            ColourIndex=self.ColourIndex,
        )

    def __json__(self):
        sup = IfcPresentationItem.__json__(self)
        attrs = {'MappedTo': self.MappedTo, 'Opacity': self.Opacity, 'Colours': self.Colours,
                 'ColourIndex': self.ColourIndex}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcIndexedTextureMap(IfcTextureCoordinate):
    def __init__(self, rtype, args):
        IfcTextureCoordinate.__init__(self, rtype, args)
        self.MappedTo = args.pop()
        self.TexCoords = args.pop()

    def __str__(self):
        return "{sup}:MappedTo:{MappedTo}:TexCoords:{TexCoords}".format(
            sup=IfcTextureCoordinate.__str__(self),
            MappedTo=self.MappedTo,
            TexCoords=self.TexCoords,
        )

    def __json__(self):
        sup = IfcTextureCoordinate.__json__(self)
        attrs = {'MappedTo': self.MappedTo, 'TexCoords': self.TexCoords}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcIndexedTriangleTextureMap(IfcIndexedTextureMap):
    def __init__(self, rtype, args):
        IfcIndexedTextureMap.__init__(self, rtype, args)
        self.TexCoordIndex = args.pop()

    def __str__(self):
        return "{sup}:TexCoordIndex:{TexCoordIndex}".format(
            sup=IfcIndexedTextureMap.__str__(self),
            TexCoordIndex=self.TexCoordIndex,
        )

    def __json__(self):
        sup = IfcIndexedTextureMap.__json__(self)
        attrs = {'TexCoordIndex': self.TexCoordIndex}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcIrregularTimeSeries(IfcTimeSeries):
    def __init__(self, rtype, args):
        IfcTimeSeries.__init__(self, rtype, args)
        self.Values = args.pop()

    def __str__(self):
        return "{sup}:Values:{Values}".format(
            sup=IfcTimeSeries.__str__(self),
            Values=self.Values,
        )

    def __json__(self):
        sup = IfcTimeSeries.__json__(self)
        attrs = {'Values': self.Values}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLagTime(IfcSchedulingTime):
    def __init__(self, rtype, args):
        IfcSchedulingTime.__init__(self, rtype, args)
        self.LagValue = args.pop()
        self.DurationType = args.pop()

    def __str__(self):
        return "{sup}:LagValue:{LagValue}:DurationType:{DurationType}".format(
            sup=IfcSchedulingTime.__str__(self),
            LagValue=self.LagValue,
            DurationType=self.DurationType,
        )

    def __json__(self):
        sup = IfcSchedulingTime.__json__(self)
        attrs = {'LagValue': self.LagValue, 'DurationType': self.DurationType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcLightSource(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.Name = args.pop()
        self.LightColour = args.pop()
        self.AmbientIntensity = args.pop()
        self.Intensity = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:LightColour:{LightColour}:AmbientIntensity:{AmbientIntensity}:Intensity:{Intensity}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            Name=self.Name,
            LightColour=self.LightColour,
            AmbientIntensity=self.AmbientIntensity,
            Intensity=self.Intensity,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'Name': self.Name, 'LightColour': self.LightColour, 'AmbientIntensity': self.AmbientIntensity,
                 'Intensity': self.Intensity}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLightSourceAmbient(IfcLightSource):
    def __init__(self, rtype, args):
        IfcLightSource.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcLightSource.__str__(self),
        )

    def __json__(self):
        sup = IfcLightSource.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLightSourceDirectional(IfcLightSource):
    def __init__(self, rtype, args):
        IfcLightSource.__init__(self, rtype, args)
        self.Orientation = args.pop()

    def __str__(self):
        return "{sup}:Orientation:{Orientation}".format(
            sup=IfcLightSource.__str__(self),
            Orientation=self.Orientation,
        )

    def __json__(self):
        sup = IfcLightSource.__json__(self)
        attrs = {'Orientation': self.Orientation}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLightSourceGoniometric(IfcLightSource):
    def __init__(self, rtype, args):
        IfcLightSource.__init__(self, rtype, args)
        self.Position = args.pop()
        self.ColourAppearance = args.pop()
        self.ColourTemperature = args.pop()
        self.LuminousFlux = args.pop()
        self.LightEmissionSource = args.pop()
        self.LightDistributionDataSource = args.pop()

    def __str__(self):
        return "{sup}:Position:{Position}:ColourAppearance:{ColourAppearance}:ColourTemperature:{ColourTemperature}:LuminousFlux:{LuminousFlux}:LightEmissionSource:{LightEmissionSource}:LightDistributionDataSource:{LightDistributionDataSource}".format(
            sup=IfcLightSource.__str__(self),
            Position=self.Position,
            ColourAppearance=self.ColourAppearance,
            ColourTemperature=self.ColourTemperature,
            LuminousFlux=self.LuminousFlux,
            LightEmissionSource=self.LightEmissionSource,
            LightDistributionDataSource=self.LightDistributionDataSource,
        )

    def __json__(self):
        sup = IfcLightSource.__json__(self)
        attrs = {'Position': self.Position, 'ColourAppearance': self.ColourAppearance,
                 'ColourTemperature': self.ColourTemperature, 'LuminousFlux': self.LuminousFlux,
                 'LightEmissionSource': self.LightEmissionSource,
                 'LightDistributionDataSource': self.LightDistributionDataSource}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLightSourcePositional(IfcLightSource):
    def __init__(self, rtype, args):
        IfcLightSource.__init__(self, rtype, args)
        self.Position = args.pop()
        self.Radius = args.pop()
        self.ConstantAttenuation = args.pop()
        self.DistanceAttenuation = args.pop()
        self.QuadricAttenuation = args.pop()

    def __str__(self):
        return "{sup}:Position:{Position}:Radius:{Radius}:ConstantAttenuation:{ConstantAttenuation}:DistanceAttenuation:{DistanceAttenuation}:QuadricAttenuation:{QuadricAttenuation}".format(
            sup=IfcLightSource.__str__(self),
            Position=self.Position,
            Radius=self.Radius,
            ConstantAttenuation=self.ConstantAttenuation,
            DistanceAttenuation=self.DistanceAttenuation,
            QuadricAttenuation=self.QuadricAttenuation,
        )

    def __json__(self):
        sup = IfcLightSource.__json__(self)
        attrs = {'Position': self.Position, 'Radius': self.Radius, 'ConstantAttenuation': self.ConstantAttenuation,
                 'DistanceAttenuation': self.DistanceAttenuation, 'QuadricAttenuation': self.QuadricAttenuation}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLightSourceSpot(IfcLightSourcePositional):
    def __init__(self, rtype, args):
        IfcLightSourcePositional.__init__(self, rtype, args)
        self.Orientation = args.pop()
        self.ConcentrationExponent = args.pop()
        self.SpreadAngle = args.pop()
        self.BeamWidthAngle = args.pop()

    def __str__(self):
        return "{sup}:Orientation:{Orientation}:ConcentrationExponent:{ConcentrationExponent}:SpreadAngle:{SpreadAngle}:BeamWidthAngle:{BeamWidthAngle}".format(
            sup=IfcLightSourcePositional.__str__(self),
            Orientation=self.Orientation,
            ConcentrationExponent=self.ConcentrationExponent,
            SpreadAngle=self.SpreadAngle,
            BeamWidthAngle=self.BeamWidthAngle,
        )

    def __json__(self):
        sup = IfcLightSourcePositional.__json__(self)
        attrs = {'Orientation': self.Orientation, 'ConcentrationExponent': self.ConcentrationExponent,
                 'SpreadAngle': self.SpreadAngle, 'BeamWidthAngle': self.BeamWidthAngle}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLinearPlacement(IfcObjectPlacement):
    def __init__(self, rtype, args):
        IfcObjectPlacement.__init__(self, rtype, args)
        self.PlacementRelTo = args.pop()
        self.Distance = args.pop()
        self.Orientation = args.pop()
        self.CartesianPosition = args.pop()

    def __str__(self):
        return "{sup}:PlacementRelTo:{PlacementRelTo}:Distance:{Distance}:Orientation:{Orientation}:CartesianPosition:{CartesianPosition}".format(
            sup=IfcObjectPlacement.__str__(self),
            PlacementRelTo=self.PlacementRelTo,
            Distance=self.Distance,
            Orientation=self.Orientation,
            CartesianPosition=self.CartesianPosition,
        )

    def __json__(self):
        sup = IfcObjectPlacement.__json__(self)
        attrs = {'PlacementRelTo': self.PlacementRelTo, 'Distance': self.Distance, 'Orientation': self.Orientation,
                 'CartesianPosition': self.CartesianPosition}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLocalPlacement(IfcObjectPlacement):
    def __init__(self, rtype, args):
        IfcObjectPlacement.__init__(self, rtype, args)
        self.PlacementRelTo = args.pop()
        self.RelativePlacement = args.pop()

    def __str__(self):
        return "{sup}:PlacementRelTo:{PlacementRelTo}:RelativePlacement:{RelativePlacement}".format(
            sup=IfcObjectPlacement.__str__(self),
            PlacementRelTo=self.PlacementRelTo,
            RelativePlacement=self.RelativePlacement,
        )

    def __json__(self):
        sup = IfcObjectPlacement.__json__(self)
        attrs = {'PlacementRelTo': self.PlacementRelTo, 'RelativePlacement': self.RelativePlacement}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLoop(IfcTopologicalRepresentationItem):
    def __init__(self, rtype, args):
        IfcTopologicalRepresentationItem.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcTopologicalRepresentationItem.__str__(self),
        )

    def __json__(self):
        sup = IfcTopologicalRepresentationItem.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMappedItem(IfcRepresentationItem):
    def __init__(self, rtype, args):
        IfcRepresentationItem.__init__(self, rtype, args)
        self.MappingSource = args.pop()
        self.MappingTarget = args.pop()

    def __str__(self):
        return "{sup}:MappingSource:{MappingSource}:MappingTarget:{MappingTarget}".format(
            sup=IfcRepresentationItem.__str__(self),
            MappingSource=self.MappingSource,
            MappingTarget=self.MappingTarget,
        )

    def __json__(self):
        sup = IfcRepresentationItem.__json__(self)
        attrs = {'MappingSource': self.MappingSource, 'MappingTarget': self.MappingTarget}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMaterial(IfcMaterialDefinition):
    def __init__(self, rtype, args):
        IfcMaterialDefinition.__init__(self, rtype, args)
        self.Name = args.pop()
        self.Description = args.pop()
        self.Category = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:Description:{Description}:Category:{Category}".format(
            sup=IfcMaterialDefinition.__str__(self),
            Name=self.Name,
            Description=self.Description,
            Category=self.Category,
        )

    def __json__(self):
        sup = IfcMaterialDefinition.__json__(self)
        attrs = {'Name': self.Name, 'Description': self.Description, 'Category': self.Category}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMaterialConstituent(IfcMaterialDefinition):
    def __init__(self, rtype, args):
        IfcMaterialDefinition.__init__(self, rtype, args)
        self.Name = args.pop()
        self.Description = args.pop()
        self.Material = args.pop()
        self.Fraction = args.pop()
        self.Category = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:Description:{Description}:Material:{Material}:Fraction:{Fraction}:Category:{Category}".format(
            sup=IfcMaterialDefinition.__str__(self),
            Name=self.Name,
            Description=self.Description,
            Material=self.Material,
            Fraction=self.Fraction,
            Category=self.Category,
        )

    def __json__(self):
        sup = IfcMaterialDefinition.__json__(self)
        attrs = {'Name': self.Name, 'Description': self.Description, 'Material': self.Material,
                 'Fraction': self.Fraction, 'Category': self.Category}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMaterialConstituentSet(IfcMaterialDefinition):
    def __init__(self, rtype, args):
        IfcMaterialDefinition.__init__(self, rtype, args)
        self.Name = args.pop()
        self.Description = args.pop()
        self.MaterialConstituents = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:Description:{Description}:MaterialConstituents:{MaterialConstituents}".format(
            sup=IfcMaterialDefinition.__str__(self),
            Name=self.Name,
            Description=self.Description,
            MaterialConstituents=self.MaterialConstituents,
        )

    def __json__(self):
        sup = IfcMaterialDefinition.__json__(self)
        attrs = {'Name': self.Name, 'Description': self.Description, 'MaterialConstituents': self.MaterialConstituents}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMaterialDefinitionRepresentation(IfcProductRepresentation):
    def __init__(self, rtype, args):
        IfcProductRepresentation.__init__(self, rtype, args)
        self.RepresentedMaterial = args.pop()

    def __str__(self):
        return "{sup}:RepresentedMaterial:{RepresentedMaterial}".format(
            sup=IfcProductRepresentation.__str__(self),
            RepresentedMaterial=self.RepresentedMaterial,
        )

    def __json__(self):
        sup = IfcProductRepresentation.__json__(self)
        attrs = {'RepresentedMaterial': self.RepresentedMaterial}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMaterialLayerSetUsage(IfcMaterialUsageDefinition):
    def __init__(self, rtype, args):
        IfcMaterialUsageDefinition.__init__(self, rtype, args)
        self.ForLayerSet = args.pop()
        self.LayerSetDirection = args.pop()
        self.DirectionSense = args.pop()
        self.OffsetFromReferenceLine = args.pop()
        self.ReferenceExtent = args.pop()

    def __str__(self):
        return "{sup}:ForLayerSet:{ForLayerSet}:LayerSetDirection:{LayerSetDirection}:DirectionSense:{DirectionSense}:OffsetFromReferenceLine:{OffsetFromReferenceLine}:ReferenceExtent:{ReferenceExtent}".format(
            sup=IfcMaterialUsageDefinition.__str__(self),
            ForLayerSet=self.ForLayerSet,
            LayerSetDirection=self.LayerSetDirection,
            DirectionSense=self.DirectionSense,
            OffsetFromReferenceLine=self.OffsetFromReferenceLine,
            ReferenceExtent=self.ReferenceExtent,
        )

    def __json__(self):
        sup = IfcMaterialUsageDefinition.__json__(self)
        attrs = {'ForLayerSet': self.ForLayerSet, 'LayerSetDirection': self.LayerSetDirection,
                 'DirectionSense': self.DirectionSense, 'OffsetFromReferenceLine': self.OffsetFromReferenceLine,
                 'ReferenceExtent': self.ReferenceExtent}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMaterialProfileSetUsage(IfcMaterialUsageDefinition):
    def __init__(self, rtype, args):
        IfcMaterialUsageDefinition.__init__(self, rtype, args)
        self.ForProfileSet = args.pop()
        self.CardinalPoint = args.pop()
        self.ReferenceExtent = args.pop()

    def __str__(self):
        return "{sup}:ForProfileSet:{ForProfileSet}:CardinalPoint:{CardinalPoint}:ReferenceExtent:{ReferenceExtent}".format(
            sup=IfcMaterialUsageDefinition.__str__(self),
            ForProfileSet=self.ForProfileSet,
            CardinalPoint=self.CardinalPoint,
            ReferenceExtent=self.ReferenceExtent,
        )

    def __json__(self):
        sup = IfcMaterialUsageDefinition.__json__(self)
        attrs = {'ForProfileSet': self.ForProfileSet, 'CardinalPoint': self.CardinalPoint,
                 'ReferenceExtent': self.ReferenceExtent}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMaterialProfileSetUsageTapering(IfcMaterialProfileSetUsage):
    def __init__(self, rtype, args):
        IfcMaterialProfileSetUsage.__init__(self, rtype, args)
        self.ForProfileEndSet = args.pop()
        self.CardinalEndPoint = args.pop()

    def __str__(self):
        return "{sup}:ForProfileEndSet:{ForProfileEndSet}:CardinalEndPoint:{CardinalEndPoint}".format(
            sup=IfcMaterialProfileSetUsage.__str__(self),
            ForProfileEndSet=self.ForProfileEndSet,
            CardinalEndPoint=self.CardinalEndPoint,
        )

    def __json__(self):
        sup = IfcMaterialProfileSetUsage.__json__(self)
        attrs = {'ForProfileEndSet': self.ForProfileEndSet, 'CardinalEndPoint': self.CardinalEndPoint}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMaterialProperties(IfcExtendedProperties):
    def __init__(self, rtype, args):
        IfcExtendedProperties.__init__(self, rtype, args)
        self.Material = args.pop()

    def __str__(self):
        return "{sup}:Material:{Material}".format(
            sup=IfcExtendedProperties.__str__(self),
            Material=self.Material,
        )

    def __json__(self):
        sup = IfcExtendedProperties.__json__(self)
        attrs = {'Material': self.Material}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMaterialRelationship(IfcResourceLevelRelationship):
    def __init__(self, rtype, args):
        IfcResourceLevelRelationship.__init__(self, rtype, args)
        self.RelatingMaterial = args.pop()
        self.RelatedMaterials = args.pop()
        self.Expression = args.pop()

    def __str__(self):
        return "{sup}:RelatingMaterial:{RelatingMaterial}:RelatedMaterials:{RelatedMaterials}:Expression:{Expression}".format(
            sup=IfcResourceLevelRelationship.__str__(self),
            RelatingMaterial=self.RelatingMaterial,
            RelatedMaterials=self.RelatedMaterials,
            Expression=self.Expression,
        )

    def __json__(self):
        sup = IfcResourceLevelRelationship.__json__(self)
        attrs = {'RelatingMaterial': self.RelatingMaterial, 'RelatedMaterials': self.RelatedMaterials,
                 'Expression': self.Expression}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMirroredProfileDef(IfcDerivedProfileDef):
    def __init__(self, rtype, args):
        IfcDerivedProfileDef.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDerivedProfileDef.__str__(self),
        )

    def __json__(self):
        sup = IfcDerivedProfileDef.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcObjectDefinition(IfcRoot):
    def __init__(self, rtype, args):
        IfcRoot.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcRoot.__str__(self),
        )

    def __json__(self):
        sup = IfcRoot.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcOpenShell(IfcConnectedFaceSet):
    def __init__(self, rtype, args):
        IfcConnectedFaceSet.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcConnectedFaceSet.__str__(self),
        )

    def __json__(self):
        sup = IfcConnectedFaceSet.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcOrganizationRelationship(IfcResourceLevelRelationship):
    def __init__(self, rtype, args):
        IfcResourceLevelRelationship.__init__(self, rtype, args)
        self.RelatingOrganization = args.pop()
        self.RelatedOrganizations = args.pop()

    def __str__(self):
        return "{sup}:RelatingOrganization:{RelatingOrganization}:RelatedOrganizations:{RelatedOrganizations}".format(
            sup=IfcResourceLevelRelationship.__str__(self),
            RelatingOrganization=self.RelatingOrganization,
            RelatedOrganizations=self.RelatedOrganizations,
        )

    def __json__(self):
        sup = IfcResourceLevelRelationship.__json__(self)
        attrs = {'RelatingOrganization': self.RelatingOrganization, 'RelatedOrganizations': self.RelatedOrganizations}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcOrientationExpression(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.LateralAxisDirection = args.pop()
        self.VerticalAxisDirection = args.pop()

    def __str__(self):
        return "{sup}:LateralAxisDirection:{LateralAxisDirection}:VerticalAxisDirection:{VerticalAxisDirection}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            LateralAxisDirection=self.LateralAxisDirection,
            VerticalAxisDirection=self.VerticalAxisDirection,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'LateralAxisDirection': self.LateralAxisDirection, 'VerticalAxisDirection': self.VerticalAxisDirection}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcOrientedEdge(IfcEdge):
    def __init__(self, rtype, args):
        IfcEdge.__init__(self, rtype, args)
        self.EdgeElement = args.pop()
        self.Orientation = args.pop()

    def __str__(self):
        return "{sup}:EdgeElement:{EdgeElement}:Orientation:{Orientation}".format(
            sup=IfcEdge.__str__(self),
            EdgeElement=self.EdgeElement,
            Orientation=self.Orientation,
        )

    def __json__(self):
        sup = IfcEdge.__json__(self)
        attrs = {'EdgeElement': self.EdgeElement, 'Orientation': self.Orientation}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcParameterizedProfileDef(IfcProfileDef):
    def __init__(self, rtype, args):
        IfcProfileDef.__init__(self, rtype, args)
        self.Position = args.pop()

    def __str__(self):
        return "{sup}:Position:{Position}".format(
            sup=IfcProfileDef.__str__(self),
            Position=self.Position,
        )

    def __json__(self):
        sup = IfcProfileDef.__json__(self)
        attrs = {'Position': self.Position}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPath(IfcTopologicalRepresentationItem):
    def __init__(self, rtype, args):
        IfcTopologicalRepresentationItem.__init__(self, rtype, args)
        self.EdgeList = args.pop()

    def __str__(self):
        return "{sup}:EdgeList:{EdgeList}".format(
            sup=IfcTopologicalRepresentationItem.__str__(self),
            EdgeList=self.EdgeList,
        )

    def __json__(self):
        sup = IfcTopologicalRepresentationItem.__json__(self)
        attrs = {'EdgeList': self.EdgeList}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPhysicalComplexQuantity(IfcPhysicalQuantity):
    def __init__(self, rtype, args):
        IfcPhysicalQuantity.__init__(self, rtype, args)
        self.HasQuantities = args.pop()
        self.Discrimination = args.pop()
        self.Quality = args.pop()
        self.Usage = args.pop()

    def __str__(self):
        return "{sup}:HasQuantities:{HasQuantities}:Discrimination:{Discrimination}:Quality:{Quality}:Usage:{Usage}".format(
            sup=IfcPhysicalQuantity.__str__(self),
            HasQuantities=self.HasQuantities,
            Discrimination=self.Discrimination,
            Quality=self.Quality,
            Usage=self.Usage,
        )

    def __json__(self):
        sup = IfcPhysicalQuantity.__json__(self)
        attrs = {'HasQuantities': self.HasQuantities, 'Discrimination': self.Discrimination, 'Quality': self.Quality,
                 'Usage': self.Usage}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPixelTexture(IfcSurfaceTexture):
    def __init__(self, rtype, args):
        IfcSurfaceTexture.__init__(self, rtype, args)
        self.Width = args.pop()
        self.Height = args.pop()
        self.ColourComponents = args.pop()
        self.Pixel = args.pop()

    def __str__(self):
        return "{sup}:Width:{Width}:Height:{Height}:ColourComponents:{ColourComponents}:Pixel:{Pixel}".format(
            sup=IfcSurfaceTexture.__str__(self),
            Width=self.Width,
            Height=self.Height,
            ColourComponents=self.ColourComponents,
            Pixel=self.Pixel,
        )

    def __json__(self):
        sup = IfcSurfaceTexture.__json__(self)
        attrs = {'Width': self.Width, 'Height': self.Height, 'ColourComponents': self.ColourComponents,
                 'Pixel': self.Pixel}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcPlacement(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.Location = args.pop()

    def __str__(self):
        return "{sup}:Location:{Location}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            Location=self.Location,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'Location': self.Location}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPlanarExtent(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.SizeInX = args.pop()
        self.SizeInY = args.pop()

    def __str__(self):
        return "{sup}:SizeInX:{SizeInX}:SizeInY:{SizeInY}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            SizeInX=self.SizeInX,
            SizeInY=self.SizeInY,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'SizeInX': self.SizeInX, 'SizeInY': self.SizeInY}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcPoint(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPointOnCurve(IfcPoint):
    def __init__(self, rtype, args):
        IfcPoint.__init__(self, rtype, args)
        self.BasisCurve = args.pop()
        self.PointParameter = args.pop()

    def __str__(self):
        return "{sup}:BasisCurve:{BasisCurve}:PointParameter:{PointParameter}".format(
            sup=IfcPoint.__str__(self),
            BasisCurve=self.BasisCurve,
            PointParameter=self.PointParameter,
        )

    def __json__(self):
        sup = IfcPoint.__json__(self)
        attrs = {'BasisCurve': self.BasisCurve, 'PointParameter': self.PointParameter}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPointOnSurface(IfcPoint):
    def __init__(self, rtype, args):
        IfcPoint.__init__(self, rtype, args)
        self.BasisSurface = args.pop()
        self.PointParameterU = args.pop()
        self.PointParameterV = args.pop()

    def __str__(self):
        return "{sup}:BasisSurface:{BasisSurface}:PointParameterU:{PointParameterU}:PointParameterV:{PointParameterV}".format(
            sup=IfcPoint.__str__(self),
            BasisSurface=self.BasisSurface,
            PointParameterU=self.PointParameterU,
            PointParameterV=self.PointParameterV,
        )

    def __json__(self):
        sup = IfcPoint.__json__(self)
        attrs = {'BasisSurface': self.BasisSurface, 'PointParameterU': self.PointParameterU,
                 'PointParameterV': self.PointParameterV}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPolyLoop(IfcLoop):
    def __init__(self, rtype, args):
        IfcLoop.__init__(self, rtype, args)
        self.Polygon = args.pop()

    def __str__(self):
        return "{sup}:Polygon:{Polygon}".format(
            sup=IfcLoop.__str__(self),
            Polygon=self.Polygon,
        )

    def __json__(self):
        sup = IfcLoop.__json__(self)
        attrs = {'Polygon': self.Polygon}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPolygonalBoundedHalfSpace(IfcHalfSpaceSolid):
    def __init__(self, rtype, args):
        IfcHalfSpaceSolid.__init__(self, rtype, args)
        self.Position = args.pop()
        self.PolygonalBoundary = args.pop()

    def __str__(self):
        return "{sup}:Position:{Position}:PolygonalBoundary:{PolygonalBoundary}".format(
            sup=IfcHalfSpaceSolid.__str__(self),
            Position=self.Position,
            PolygonalBoundary=self.PolygonalBoundary,
        )

    def __json__(self):
        sup = IfcHalfSpaceSolid.__json__(self)
        attrs = {'Position': self.Position, 'PolygonalBoundary': self.PolygonalBoundary}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcPreDefinedItem(IfcPresentationItem):
    def __init__(self, rtype, args):
        IfcPresentationItem.__init__(self, rtype, args)
        self.Name = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}".format(
            sup=IfcPresentationItem.__str__(self),
            Name=self.Name,
        )

    def __json__(self):
        sup = IfcPresentationItem.__json__(self)
        attrs = {'Name': self.Name}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcPreDefinedProperties(IfcPropertyAbstraction):
    def __init__(self, rtype, args):
        IfcPropertyAbstraction.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcPropertyAbstraction.__str__(self),
        )

    def __json__(self):
        sup = IfcPropertyAbstraction.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcPreDefinedTextFont(IfcPreDefinedItem):
    def __init__(self, rtype, args):
        IfcPreDefinedItem.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcPreDefinedItem.__str__(self),
        )

    def __json__(self):
        sup = IfcPreDefinedItem.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcProductDefinitionShape(IfcProductRepresentation):
    def __init__(self, rtype, args):
        IfcProductRepresentation.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcProductRepresentation.__str__(self),
        )

    def __json__(self):
        sup = IfcProductRepresentation.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcProfileProperties(IfcExtendedProperties):
    def __init__(self, rtype, args):
        IfcExtendedProperties.__init__(self, rtype, args)
        self.ProfileDefinition = args.pop()

    def __str__(self):
        return "{sup}:ProfileDefinition:{ProfileDefinition}".format(
            sup=IfcExtendedProperties.__str__(self),
            ProfileDefinition=self.ProfileDefinition,
        )

    def __json__(self):
        sup = IfcExtendedProperties.__json__(self)
        attrs = {'ProfileDefinition': self.ProfileDefinition}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcProperty(IfcPropertyAbstraction):
    def __init__(self, rtype, args):
        IfcPropertyAbstraction.__init__(self, rtype, args)
        self.Name = args.pop()
        self.Description = args.pop()

    def __str__(self):
        return "{sup}:Name:{Name}:Description:{Description}".format(
            sup=IfcPropertyAbstraction.__str__(self),
            Name=self.Name,
            Description=self.Description,
        )

    def __json__(self):
        sup = IfcPropertyAbstraction.__json__(self)
        attrs = {'Name': self.Name, 'Description': self.Description}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcPropertyDefinition(IfcRoot):
    def __init__(self, rtype, args):
        IfcRoot.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcRoot.__str__(self),
        )

    def __json__(self):
        sup = IfcRoot.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPropertyDependencyRelationship(IfcResourceLevelRelationship):
    def __init__(self, rtype, args):
        IfcResourceLevelRelationship.__init__(self, rtype, args)
        self.DependingProperty = args.pop()
        self.DependantProperty = args.pop()
        self.Expression = args.pop()

    def __str__(self):
        return "{sup}:DependingProperty:{DependingProperty}:DependantProperty:{DependantProperty}:Expression:{Expression}".format(
            sup=IfcResourceLevelRelationship.__str__(self),
            DependingProperty=self.DependingProperty,
            DependantProperty=self.DependantProperty,
            Expression=self.Expression,
        )

    def __json__(self):
        sup = IfcResourceLevelRelationship.__json__(self)
        attrs = {'DependingProperty': self.DependingProperty, 'DependantProperty': self.DependantProperty,
                 'Expression': self.Expression}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcPropertySetDefinition(IfcPropertyDefinition):
    def __init__(self, rtype, args):
        IfcPropertyDefinition.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcPropertyDefinition.__str__(self),
        )

    def __json__(self):
        sup = IfcPropertyDefinition.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcPropertyTemplateDefinition(IfcPropertyDefinition):
    def __init__(self, rtype, args):
        IfcPropertyDefinition.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcPropertyDefinition.__str__(self),
        )

    def __json__(self):
        sup = IfcPropertyDefinition.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcQuantitySet(IfcPropertySetDefinition):
    def __init__(self, rtype, args):
        IfcPropertySetDefinition.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcPropertySetDefinition.__str__(self),
        )

    def __json__(self):
        sup = IfcPropertySetDefinition.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRectangleProfileDef(IfcParameterizedProfileDef):
    def __init__(self, rtype, args):
        IfcParameterizedProfileDef.__init__(self, rtype, args)
        self.XDim = args.pop()
        self.YDim = args.pop()

    def __str__(self):
        return "{sup}:XDim:{XDim}:YDim:{YDim}".format(
            sup=IfcParameterizedProfileDef.__str__(self),
            XDim=self.XDim,
            YDim=self.YDim,
        )

    def __json__(self):
        sup = IfcParameterizedProfileDef.__json__(self)
        attrs = {'XDim': self.XDim, 'YDim': self.YDim}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRegularTimeSeries(IfcTimeSeries):
    def __init__(self, rtype, args):
        IfcTimeSeries.__init__(self, rtype, args)
        self.TimeStep = args.pop()
        self.Values = args.pop()

    def __str__(self):
        return "{sup}:TimeStep:{TimeStep}:Values:{Values}".format(
            sup=IfcTimeSeries.__str__(self),
            TimeStep=self.TimeStep,
            Values=self.Values,
        )

    def __json__(self):
        sup = IfcTimeSeries.__json__(self)
        attrs = {'TimeStep': self.TimeStep, 'Values': self.Values}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcReinforcementBarProperties(IfcPreDefinedProperties):
    def __init__(self, rtype, args):
        IfcPreDefinedProperties.__init__(self, rtype, args)
        self.TotalCrossSectionArea = args.pop()
        self.SteelGrade = args.pop()
        self.BarSurface = args.pop()
        self.EffectiveDepth = args.pop()
        self.NominalBarDiameter = args.pop()
        self.BarCount = args.pop()

    def __str__(self):
        return "{sup}:TotalCrossSectionArea:{TotalCrossSectionArea}:SteelGrade:{SteelGrade}:BarSurface:{BarSurface}:EffectiveDepth:{EffectiveDepth}:NominalBarDiameter:{NominalBarDiameter}:BarCount:{BarCount}".format(
            sup=IfcPreDefinedProperties.__str__(self),
            TotalCrossSectionArea=self.TotalCrossSectionArea,
            SteelGrade=self.SteelGrade,
            BarSurface=self.BarSurface,
            EffectiveDepth=self.EffectiveDepth,
            NominalBarDiameter=self.NominalBarDiameter,
            BarCount=self.BarCount,
        )

    def __json__(self):
        sup = IfcPreDefinedProperties.__json__(self)
        attrs = {'TotalCrossSectionArea': self.TotalCrossSectionArea, 'SteelGrade': self.SteelGrade,
                 'BarSurface': self.BarSurface, 'EffectiveDepth': self.EffectiveDepth,
                 'NominalBarDiameter': self.NominalBarDiameter, 'BarCount': self.BarCount}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcRelationship(IfcRoot):
    def __init__(self, rtype, args):
        IfcRoot.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcRoot.__str__(self),
        )

    def __json__(self):
        sup = IfcRoot.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcResourceApprovalRelationship(IfcResourceLevelRelationship):
    def __init__(self, rtype, args):
        IfcResourceLevelRelationship.__init__(self, rtype, args)
        self.RelatedResourceObjects = args.pop()
        self.RelatingApproval = args.pop()

    def __str__(self):
        return "{sup}:RelatedResourceObjects:{RelatedResourceObjects}:RelatingApproval:{RelatingApproval}".format(
            sup=IfcResourceLevelRelationship.__str__(self),
            RelatedResourceObjects=self.RelatedResourceObjects,
            RelatingApproval=self.RelatingApproval,
        )

    def __json__(self):
        sup = IfcResourceLevelRelationship.__json__(self)
        attrs = {'RelatedResourceObjects': self.RelatedResourceObjects, 'RelatingApproval': self.RelatingApproval}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcResourceConstraintRelationship(IfcResourceLevelRelationship):
    def __init__(self, rtype, args):
        IfcResourceLevelRelationship.__init__(self, rtype, args)
        self.RelatingConstraint = args.pop()
        self.RelatedResourceObjects = args.pop()

    def __str__(self):
        return "{sup}:RelatingConstraint:{RelatingConstraint}:RelatedResourceObjects:{RelatedResourceObjects}".format(
            sup=IfcResourceLevelRelationship.__str__(self),
            RelatingConstraint=self.RelatingConstraint,
            RelatedResourceObjects=self.RelatedResourceObjects,
        )

    def __json__(self):
        sup = IfcResourceLevelRelationship.__json__(self)
        attrs = {'RelatingConstraint': self.RelatingConstraint, 'RelatedResourceObjects': self.RelatedResourceObjects}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcResourceTime(IfcSchedulingTime):
    def __init__(self, rtype, args):
        IfcSchedulingTime.__init__(self, rtype, args)
        self.ScheduleWork = args.pop()
        self.ScheduleUsage = args.pop()
        self.ScheduleStart = args.pop()
        self.ScheduleFinish = args.pop()
        self.ScheduleContour = args.pop()
        self.LevelingDelay = args.pop()
        self.IsOverAllocated = args.pop()
        self.StatusTime = args.pop()
        self.ActualWork = args.pop()
        self.ActualUsage = args.pop()
        self.ActualStart = args.pop()
        self.ActualFinish = args.pop()
        self.RemainingWork = args.pop()
        self.RemainingUsage = args.pop()
        self.Completion = args.pop()

    def __str__(self):
        return "{sup}:ScheduleWork:{ScheduleWork}:ScheduleUsage:{ScheduleUsage}:ScheduleStart:{ScheduleStart}:ScheduleFinish:{ScheduleFinish}:ScheduleContour:{ScheduleContour}:LevelingDelay:{LevelingDelay}:IsOverAllocated:{IsOverAllocated}:StatusTime:{StatusTime}:ActualWork:{ActualWork}:ActualUsage:{ActualUsage}:ActualStart:{ActualStart}:ActualFinish:{ActualFinish}:RemainingWork:{RemainingWork}:RemainingUsage:{RemainingUsage}:Completion:{Completion}".format(
            sup=IfcSchedulingTime.__str__(self),
            ScheduleWork=self.ScheduleWork,
            ScheduleUsage=self.ScheduleUsage,
            ScheduleStart=self.ScheduleStart,
            ScheduleFinish=self.ScheduleFinish,
            ScheduleContour=self.ScheduleContour,
            LevelingDelay=self.LevelingDelay,
            IsOverAllocated=self.IsOverAllocated,
            StatusTime=self.StatusTime,
            ActualWork=self.ActualWork,
            ActualUsage=self.ActualUsage,
            ActualStart=self.ActualStart,
            ActualFinish=self.ActualFinish,
            RemainingWork=self.RemainingWork,
            RemainingUsage=self.RemainingUsage,
            Completion=self.Completion,
        )

    def __json__(self):
        sup = IfcSchedulingTime.__json__(self)
        attrs = {'ScheduleWork': self.ScheduleWork, 'ScheduleUsage': self.ScheduleUsage,
                 'ScheduleStart': self.ScheduleStart, 'ScheduleFinish': self.ScheduleFinish,
                 'ScheduleContour': self.ScheduleContour, 'LevelingDelay': self.LevelingDelay,
                 'IsOverAllocated': self.IsOverAllocated, 'StatusTime': self.StatusTime, 'ActualWork': self.ActualWork,
                 'ActualUsage': self.ActualUsage, 'ActualStart': self.ActualStart, 'ActualFinish': self.ActualFinish,
                 'RemainingWork': self.RemainingWork, 'RemainingUsage': self.RemainingUsage,
                 'Completion': self.Completion}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRoundedRectangleProfileDef(IfcRectangleProfileDef):
    def __init__(self, rtype, args):
        IfcRectangleProfileDef.__init__(self, rtype, args)
        self.RoundingRadius = args.pop()

    def __str__(self):
        return "{sup}:RoundingRadius:{RoundingRadius}".format(
            sup=IfcRectangleProfileDef.__str__(self),
            RoundingRadius=self.RoundingRadius,
        )

    def __json__(self):
        sup = IfcRectangleProfileDef.__json__(self)
        attrs = {'RoundingRadius': self.RoundingRadius}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSectionProperties(IfcPreDefinedProperties):
    def __init__(self, rtype, args):
        IfcPreDefinedProperties.__init__(self, rtype, args)
        self.SectionType = args.pop()
        self.StartProfile = args.pop()
        self.EndProfile = args.pop()

    def __str__(self):
        return "{sup}:SectionType:{SectionType}:StartProfile:{StartProfile}:EndProfile:{EndProfile}".format(
            sup=IfcPreDefinedProperties.__str__(self),
            SectionType=self.SectionType,
            StartProfile=self.StartProfile,
            EndProfile=self.EndProfile,
        )

    def __json__(self):
        sup = IfcPreDefinedProperties.__json__(self)
        attrs = {'SectionType': self.SectionType, 'StartProfile': self.StartProfile, 'EndProfile': self.EndProfile}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSectionReinforcementProperties(IfcPreDefinedProperties):
    def __init__(self, rtype, args):
        IfcPreDefinedProperties.__init__(self, rtype, args)
        self.LongitudinalStartPosition = args.pop()
        self.LongitudinalEndPosition = args.pop()
        self.TransversePosition = args.pop()
        self.ReinforcementRole = args.pop()
        self.SectionDefinition = args.pop()
        self.CrossSectionReinforcementDefinitions = args.pop()

    def __str__(self):
        return "{sup}:LongitudinalStartPosition:{LongitudinalStartPosition}:LongitudinalEndPosition:{LongitudinalEndPosition}:TransversePosition:{TransversePosition}:ReinforcementRole:{ReinforcementRole}:SectionDefinition:{SectionDefinition}:CrossSectionReinforcementDefinitions:{CrossSectionReinforcementDefinitions}".format(
            sup=IfcPreDefinedProperties.__str__(self),
            LongitudinalStartPosition=self.LongitudinalStartPosition,
            LongitudinalEndPosition=self.LongitudinalEndPosition,
            TransversePosition=self.TransversePosition,
            ReinforcementRole=self.ReinforcementRole,
            SectionDefinition=self.SectionDefinition,
            CrossSectionReinforcementDefinitions=self.CrossSectionReinforcementDefinitions,
        )

    def __json__(self):
        sup = IfcPreDefinedProperties.__json__(self)
        attrs = {'LongitudinalStartPosition': self.LongitudinalStartPosition,
                 'LongitudinalEndPosition': self.LongitudinalEndPosition, 'TransversePosition': self.TransversePosition,
                 'ReinforcementRole': self.ReinforcementRole, 'SectionDefinition': self.SectionDefinition,
                 'CrossSectionReinforcementDefinitions': self.CrossSectionReinforcementDefinitions}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSectionedSpine(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.SpineCurve = args.pop()
        self.CrossSections = args.pop()
        self.CrossSectionPositions = args.pop()

    def __str__(self):
        return "{sup}:SpineCurve:{SpineCurve}:CrossSections:{CrossSections}:CrossSectionPositions:{CrossSectionPositions}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            SpineCurve=self.SpineCurve,
            CrossSections=self.CrossSections,
            CrossSectionPositions=self.CrossSectionPositions,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'SpineCurve': self.SpineCurve, 'CrossSections': self.CrossSections,
                 'CrossSectionPositions': self.CrossSectionPositions}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcShellBasedSurfaceModel(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.SbsmBoundary = args.pop()

    def __str__(self):
        return "{sup}:SbsmBoundary:{SbsmBoundary}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            SbsmBoundary=self.SbsmBoundary,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'SbsmBoundary': self.SbsmBoundary}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcSimpleProperty(IfcProperty):
    def __init__(self, rtype, args):
        IfcProperty.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcProperty.__str__(self),
        )

    def __json__(self):
        sup = IfcProperty.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSlippageConnectionCondition(IfcStructuralConnectionCondition):
    def __init__(self, rtype, args):
        IfcStructuralConnectionCondition.__init__(self, rtype, args)
        self.SlippageX = args.pop()
        self.SlippageY = args.pop()
        self.SlippageZ = args.pop()

    def __str__(self):
        return "{sup}:SlippageX:{SlippageX}:SlippageY:{SlippageY}:SlippageZ:{SlippageZ}".format(
            sup=IfcStructuralConnectionCondition.__str__(self),
            SlippageX=self.SlippageX,
            SlippageY=self.SlippageY,
            SlippageZ=self.SlippageZ,
        )

    def __json__(self):
        sup = IfcStructuralConnectionCondition.__json__(self)
        attrs = {'SlippageX': self.SlippageX, 'SlippageY': self.SlippageY, 'SlippageZ': self.SlippageZ}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcSolidModel(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralLoadLinearForce(IfcStructuralLoadStatic):
    def __init__(self, rtype, args):
        IfcStructuralLoadStatic.__init__(self, rtype, args)
        self.LinearForceX = args.pop()
        self.LinearForceY = args.pop()
        self.LinearForceZ = args.pop()
        self.LinearMomentX = args.pop()
        self.LinearMomentY = args.pop()
        self.LinearMomentZ = args.pop()

    def __str__(self):
        return "{sup}:LinearForceX:{LinearForceX}:LinearForceY:{LinearForceY}:LinearForceZ:{LinearForceZ}:LinearMomentX:{LinearMomentX}:LinearMomentY:{LinearMomentY}:LinearMomentZ:{LinearMomentZ}".format(
            sup=IfcStructuralLoadStatic.__str__(self),
            LinearForceX=self.LinearForceX,
            LinearForceY=self.LinearForceY,
            LinearForceZ=self.LinearForceZ,
            LinearMomentX=self.LinearMomentX,
            LinearMomentY=self.LinearMomentY,
            LinearMomentZ=self.LinearMomentZ,
        )

    def __json__(self):
        sup = IfcStructuralLoadStatic.__json__(self)
        attrs = {'LinearForceX': self.LinearForceX, 'LinearForceY': self.LinearForceY,
                 'LinearForceZ': self.LinearForceZ, 'LinearMomentX': self.LinearMomentX,
                 'LinearMomentY': self.LinearMomentY, 'LinearMomentZ': self.LinearMomentZ}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralLoadPlanarForce(IfcStructuralLoadStatic):
    def __init__(self, rtype, args):
        IfcStructuralLoadStatic.__init__(self, rtype, args)
        self.PlanarForceX = args.pop()
        self.PlanarForceY = args.pop()
        self.PlanarForceZ = args.pop()

    def __str__(self):
        return "{sup}:PlanarForceX:{PlanarForceX}:PlanarForceY:{PlanarForceY}:PlanarForceZ:{PlanarForceZ}".format(
            sup=IfcStructuralLoadStatic.__str__(self),
            PlanarForceX=self.PlanarForceX,
            PlanarForceY=self.PlanarForceY,
            PlanarForceZ=self.PlanarForceZ,
        )

    def __json__(self):
        sup = IfcStructuralLoadStatic.__json__(self)
        attrs = {'PlanarForceX': self.PlanarForceX, 'PlanarForceY': self.PlanarForceY,
                 'PlanarForceZ': self.PlanarForceZ}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralLoadSingleDisplacement(IfcStructuralLoadStatic):
    def __init__(self, rtype, args):
        IfcStructuralLoadStatic.__init__(self, rtype, args)
        self.DisplacementX = args.pop()
        self.DisplacementY = args.pop()
        self.DisplacementZ = args.pop()
        self.RotationalDisplacementRX = args.pop()
        self.RotationalDisplacementRY = args.pop()
        self.RotationalDisplacementRZ = args.pop()

    def __str__(self):
        return "{sup}:DisplacementX:{DisplacementX}:DisplacementY:{DisplacementY}:DisplacementZ:{DisplacementZ}:RotationalDisplacementRX:{RotationalDisplacementRX}:RotationalDisplacementRY:{RotationalDisplacementRY}:RotationalDisplacementRZ:{RotationalDisplacementRZ}".format(
            sup=IfcStructuralLoadStatic.__str__(self),
            DisplacementX=self.DisplacementX,
            DisplacementY=self.DisplacementY,
            DisplacementZ=self.DisplacementZ,
            RotationalDisplacementRX=self.RotationalDisplacementRX,
            RotationalDisplacementRY=self.RotationalDisplacementRY,
            RotationalDisplacementRZ=self.RotationalDisplacementRZ,
        )

    def __json__(self):
        sup = IfcStructuralLoadStatic.__json__(self)
        attrs = {'DisplacementX': self.DisplacementX, 'DisplacementY': self.DisplacementY,
                 'DisplacementZ': self.DisplacementZ, 'RotationalDisplacementRX': self.RotationalDisplacementRX,
                 'RotationalDisplacementRY': self.RotationalDisplacementRY,
                 'RotationalDisplacementRZ': self.RotationalDisplacementRZ}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralLoadSingleDisplacementDistortion(IfcStructuralLoadSingleDisplacement):
    def __init__(self, rtype, args):
        IfcStructuralLoadSingleDisplacement.__init__(self, rtype, args)
        self.Distortion = args.pop()

    def __str__(self):
        return "{sup}:Distortion:{Distortion}".format(
            sup=IfcStructuralLoadSingleDisplacement.__str__(self),
            Distortion=self.Distortion,
        )

    def __json__(self):
        sup = IfcStructuralLoadSingleDisplacement.__json__(self)
        attrs = {'Distortion': self.Distortion}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralLoadSingleForce(IfcStructuralLoadStatic):
    def __init__(self, rtype, args):
        IfcStructuralLoadStatic.__init__(self, rtype, args)
        self.ForceX = args.pop()
        self.ForceY = args.pop()
        self.ForceZ = args.pop()
        self.MomentX = args.pop()
        self.MomentY = args.pop()
        self.MomentZ = args.pop()

    def __str__(self):
        return "{sup}:ForceX:{ForceX}:ForceY:{ForceY}:ForceZ:{ForceZ}:MomentX:{MomentX}:MomentY:{MomentY}:MomentZ:{MomentZ}".format(
            sup=IfcStructuralLoadStatic.__str__(self),
            ForceX=self.ForceX,
            ForceY=self.ForceY,
            ForceZ=self.ForceZ,
            MomentX=self.MomentX,
            MomentY=self.MomentY,
            MomentZ=self.MomentZ,
        )

    def __json__(self):
        sup = IfcStructuralLoadStatic.__json__(self)
        attrs = {'ForceX': self.ForceX, 'ForceY': self.ForceY, 'ForceZ': self.ForceZ, 'MomentX': self.MomentX,
                 'MomentY': self.MomentY, 'MomentZ': self.MomentZ}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralLoadSingleForceWarping(IfcStructuralLoadSingleForce):
    def __init__(self, rtype, args):
        IfcStructuralLoadSingleForce.__init__(self, rtype, args)
        self.WarpingMoment = args.pop()

    def __str__(self):
        return "{sup}:WarpingMoment:{WarpingMoment}".format(
            sup=IfcStructuralLoadSingleForce.__str__(self),
            WarpingMoment=self.WarpingMoment,
        )

    def __json__(self):
        sup = IfcStructuralLoadSingleForce.__json__(self)
        attrs = {'WarpingMoment': self.WarpingMoment}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSubedge(IfcEdge):
    def __init__(self, rtype, args):
        IfcEdge.__init__(self, rtype, args)
        self.ParentEdge = args.pop()

    def __str__(self):
        return "{sup}:ParentEdge:{ParentEdge}".format(
            sup=IfcEdge.__str__(self),
            ParentEdge=self.ParentEdge,
        )

    def __json__(self):
        sup = IfcEdge.__json__(self)
        attrs = {'ParentEdge': self.ParentEdge}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcSurface(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSurfaceStyleRendering(IfcSurfaceStyleShading):
    def __init__(self, rtype, args):
        IfcSurfaceStyleShading.__init__(self, rtype, args)
        self.DiffuseColour = args.pop()
        self.TransmissionColour = args.pop()
        self.DiffuseTransmissionColour = args.pop()
        self.ReflectionColour = args.pop()
        self.SpecularColour = args.pop()
        self.SpecularHighlight = args.pop()
        self.ReflectanceMethod = args.pop()

    def __str__(self):
        return "{sup}:DiffuseColour:{DiffuseColour}:TransmissionColour:{TransmissionColour}:DiffuseTransmissionColour:{DiffuseTransmissionColour}:ReflectionColour:{ReflectionColour}:SpecularColour:{SpecularColour}:SpecularHighlight:{SpecularHighlight}:ReflectanceMethod:{ReflectanceMethod}".format(
            sup=IfcSurfaceStyleShading.__str__(self),
            DiffuseColour=self.DiffuseColour,
            TransmissionColour=self.TransmissionColour,
            DiffuseTransmissionColour=self.DiffuseTransmissionColour,
            ReflectionColour=self.ReflectionColour,
            SpecularColour=self.SpecularColour,
            SpecularHighlight=self.SpecularHighlight,
            ReflectanceMethod=self.ReflectanceMethod,
        )

    def __json__(self):
        sup = IfcSurfaceStyleShading.__json__(self)
        attrs = {'DiffuseColour': self.DiffuseColour, 'TransmissionColour': self.TransmissionColour,
                 'DiffuseTransmissionColour': self.DiffuseTransmissionColour, 'ReflectionColour': self.ReflectionColour,
                 'SpecularColour': self.SpecularColour, 'SpecularHighlight': self.SpecularHighlight,
                 'ReflectanceMethod': self.ReflectanceMethod}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcSweptAreaSolid(IfcSolidModel):
    def __init__(self, rtype, args):
        IfcSolidModel.__init__(self, rtype, args)
        self.SweptArea = args.pop()
        self.Position = args.pop()

    def __str__(self):
        return "{sup}:SweptArea:{SweptArea}:Position:{Position}".format(
            sup=IfcSolidModel.__str__(self),
            SweptArea=self.SweptArea,
            Position=self.Position,
        )

    def __json__(self):
        sup = IfcSolidModel.__json__(self)
        attrs = {'SweptArea': self.SweptArea, 'Position': self.Position}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSweptDiskSolid(IfcSolidModel):
    def __init__(self, rtype, args):
        IfcSolidModel.__init__(self, rtype, args)
        self.Directrix = args.pop()
        self.Radius = args.pop()
        self.InnerRadius = args.pop()
        self.StartParam = args.pop()
        self.EndParam = args.pop()

    def __str__(self):
        return "{sup}:Directrix:{Directrix}:Radius:{Radius}:InnerRadius:{InnerRadius}:StartParam:{StartParam}:EndParam:{EndParam}".format(
            sup=IfcSolidModel.__str__(self),
            Directrix=self.Directrix,
            Radius=self.Radius,
            InnerRadius=self.InnerRadius,
            StartParam=self.StartParam,
            EndParam=self.EndParam,
        )

    def __json__(self):
        sup = IfcSolidModel.__json__(self)
        attrs = {'Directrix': self.Directrix, 'Radius': self.Radius, 'InnerRadius': self.InnerRadius,
                 'StartParam': self.StartParam, 'EndParam': self.EndParam}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSweptDiskSolidPolygonal(IfcSweptDiskSolid):
    def __init__(self, rtype, args):
        IfcSweptDiskSolid.__init__(self, rtype, args)
        self.FilletRadius = args.pop()

    def __str__(self):
        return "{sup}:FilletRadius:{FilletRadius}".format(
            sup=IfcSweptDiskSolid.__str__(self),
            FilletRadius=self.FilletRadius,
        )

    def __json__(self):
        sup = IfcSweptDiskSolid.__json__(self)
        attrs = {'FilletRadius': self.FilletRadius}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcSweptSurface(IfcSurface):
    def __init__(self, rtype, args):
        IfcSurface.__init__(self, rtype, args)
        self.SweptCurve = args.pop()
        self.Position = args.pop()

    def __str__(self):
        return "{sup}:SweptCurve:{SweptCurve}:Position:{Position}".format(
            sup=IfcSurface.__str__(self),
            SweptCurve=self.SweptCurve,
            Position=self.Position,
        )

    def __json__(self):
        sup = IfcSurface.__json__(self)
        attrs = {'SweptCurve': self.SweptCurve, 'Position': self.Position}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTShapeProfileDef(IfcParameterizedProfileDef):
    def __init__(self, rtype, args):
        IfcParameterizedProfileDef.__init__(self, rtype, args)
        self.Depth = args.pop()
        self.FlangeWidth = args.pop()
        self.WebThickness = args.pop()
        self.FlangeThickness = args.pop()
        self.FilletRadius = args.pop()
        self.FlangeEdgeRadius = args.pop()
        self.WebEdgeRadius = args.pop()
        self.WebSlope = args.pop()
        self.FlangeSlope = args.pop()

    def __str__(self):
        return "{sup}:Depth:{Depth}:FlangeWidth:{FlangeWidth}:WebThickness:{WebThickness}:FlangeThickness:{FlangeThickness}:FilletRadius:{FilletRadius}:FlangeEdgeRadius:{FlangeEdgeRadius}:WebEdgeRadius:{WebEdgeRadius}:WebSlope:{WebSlope}:FlangeSlope:{FlangeSlope}".format(
            sup=IfcParameterizedProfileDef.__str__(self),
            Depth=self.Depth,
            FlangeWidth=self.FlangeWidth,
            WebThickness=self.WebThickness,
            FlangeThickness=self.FlangeThickness,
            FilletRadius=self.FilletRadius,
            FlangeEdgeRadius=self.FlangeEdgeRadius,
            WebEdgeRadius=self.WebEdgeRadius,
            WebSlope=self.WebSlope,
            FlangeSlope=self.FlangeSlope,
        )

    def __json__(self):
        sup = IfcParameterizedProfileDef.__json__(self)
        attrs = {'Depth': self.Depth, 'FlangeWidth': self.FlangeWidth, 'WebThickness': self.WebThickness,
                 'FlangeThickness': self.FlangeThickness, 'FilletRadius': self.FilletRadius,
                 'FlangeEdgeRadius': self.FlangeEdgeRadius, 'WebEdgeRadius': self.WebEdgeRadius,
                 'WebSlope': self.WebSlope, 'FlangeSlope': self.FlangeSlope}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcTessellatedItem(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTextLiteral(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.Literal = args.pop()
        self.Placement = args.pop()
        self.Path = args.pop()

    def __str__(self):
        return "{sup}:Literal:{Literal}:Placement:{Placement}:Path:{Path}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            Literal=self.Literal,
            Placement=self.Placement,
            Path=self.Path,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'Literal': self.Literal, 'Placement': self.Placement, 'Path': self.Path}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTextLiteralWithExtent(IfcTextLiteral):
    def __init__(self, rtype, args):
        IfcTextLiteral.__init__(self, rtype, args)
        self.Extent = args.pop()
        self.BoxAlignment = args.pop()

    def __str__(self):
        return "{sup}:Extent:{Extent}:BoxAlignment:{BoxAlignment}".format(
            sup=IfcTextLiteral.__str__(self),
            Extent=self.Extent,
            BoxAlignment=self.BoxAlignment,
        )

    def __json__(self):
        sup = IfcTextLiteral.__json__(self)
        attrs = {'Extent': self.Extent, 'BoxAlignment': self.BoxAlignment}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTextStyleFontModel(IfcPreDefinedTextFont):
    def __init__(self, rtype, args):
        IfcPreDefinedTextFont.__init__(self, rtype, args)
        self.FontFamily = args.pop()
        self.FontStyle = args.pop()
        self.FontVariant = args.pop()
        self.FontWeight = args.pop()
        self.FontSize = args.pop()

    def __str__(self):
        return "{sup}:FontFamily:{FontFamily}:FontStyle:{FontStyle}:FontVariant:{FontVariant}:FontWeight:{FontWeight}:FontSize:{FontSize}".format(
            sup=IfcPreDefinedTextFont.__str__(self),
            FontFamily=self.FontFamily,
            FontStyle=self.FontStyle,
            FontVariant=self.FontVariant,
            FontWeight=self.FontWeight,
            FontSize=self.FontSize,
        )

    def __json__(self):
        sup = IfcPreDefinedTextFont.__json__(self)
        attrs = {'FontFamily': self.FontFamily, 'FontStyle': self.FontStyle, 'FontVariant': self.FontVariant,
                 'FontWeight': self.FontWeight, 'FontSize': self.FontSize}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTrapeziumProfileDef(IfcParameterizedProfileDef):
    def __init__(self, rtype, args):
        IfcParameterizedProfileDef.__init__(self, rtype, args)
        self.BottomXDim = args.pop()
        self.TopXDim = args.pop()
        self.YDim = args.pop()
        self.TopXOffset = args.pop()

    def __str__(self):
        return "{sup}:BottomXDim:{BottomXDim}:TopXDim:{TopXDim}:YDim:{YDim}:TopXOffset:{TopXOffset}".format(
            sup=IfcParameterizedProfileDef.__str__(self),
            BottomXDim=self.BottomXDim,
            TopXDim=self.TopXDim,
            YDim=self.YDim,
            TopXOffset=self.TopXOffset,
        )

    def __json__(self):
        sup = IfcParameterizedProfileDef.__json__(self)
        attrs = {'BottomXDim': self.BottomXDim, 'TopXDim': self.TopXDim, 'YDim': self.YDim,
                 'TopXOffset': self.TopXOffset}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTypeObject(IfcObjectDefinition):
    def __init__(self, rtype, args):
        IfcObjectDefinition.__init__(self, rtype, args)
        self.ApplicableOccurrence = args.pop()
        self.HasPropertySets = args.pop()

    def __str__(self):
        return "{sup}:ApplicableOccurrence:{ApplicableOccurrence}:HasPropertySets:{HasPropertySets}".format(
            sup=IfcObjectDefinition.__str__(self),
            ApplicableOccurrence=self.ApplicableOccurrence,
            HasPropertySets=self.HasPropertySets,
        )

    def __json__(self):
        sup = IfcObjectDefinition.__json__(self)
        attrs = {'ApplicableOccurrence': self.ApplicableOccurrence, 'HasPropertySets': self.HasPropertySets}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcTypeProcess(IfcTypeObject):
    def __init__(self, rtype, args):
        IfcTypeObject.__init__(self, rtype, args)
        self.Identification = args.pop()
        self.LongDescription = args.pop()
        self.ProcessType = args.pop()

    def __str__(self):
        return "{sup}:Identification:{Identification}:LongDescription:{LongDescription}:ProcessType:{ProcessType}".format(
            sup=IfcTypeObject.__str__(self),
            Identification=self.Identification,
            LongDescription=self.LongDescription,
            ProcessType=self.ProcessType,
        )

    def __json__(self):
        sup = IfcTypeObject.__json__(self)
        attrs = {'Identification': self.Identification, 'LongDescription': self.LongDescription,
                 'ProcessType': self.ProcessType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTypeProduct(IfcTypeObject):
    def __init__(self, rtype, args):
        IfcTypeObject.__init__(self, rtype, args)
        self.RepresentationMaps = args.pop()
        self.Tag = args.pop()

    def __str__(self):
        return "{sup}:RepresentationMaps:{RepresentationMaps}:Tag:{Tag}".format(
            sup=IfcTypeObject.__str__(self),
            RepresentationMaps=self.RepresentationMaps,
            Tag=self.Tag,
        )

    def __json__(self):
        sup = IfcTypeObject.__json__(self)
        attrs = {'RepresentationMaps': self.RepresentationMaps, 'Tag': self.Tag}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcTypeResource(IfcTypeObject):
    def __init__(self, rtype, args):
        IfcTypeObject.__init__(self, rtype, args)
        self.Identification = args.pop()
        self.LongDescription = args.pop()
        self.ResourceType = args.pop()

    def __str__(self):
        return "{sup}:Identification:{Identification}:LongDescription:{LongDescription}:ResourceType:{ResourceType}".format(
            sup=IfcTypeObject.__str__(self),
            Identification=self.Identification,
            LongDescription=self.LongDescription,
            ResourceType=self.ResourceType,
        )

    def __json__(self):
        sup = IfcTypeObject.__json__(self)
        attrs = {'Identification': self.Identification, 'LongDescription': self.LongDescription,
                 'ResourceType': self.ResourceType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcUShapeProfileDef(IfcParameterizedProfileDef):
    def __init__(self, rtype, args):
        IfcParameterizedProfileDef.__init__(self, rtype, args)
        self.Depth = args.pop()
        self.FlangeWidth = args.pop()
        self.WebThickness = args.pop()
        self.FlangeThickness = args.pop()
        self.FilletRadius = args.pop()
        self.EdgeRadius = args.pop()
        self.FlangeSlope = args.pop()

    def __str__(self):
        return "{sup}:Depth:{Depth}:FlangeWidth:{FlangeWidth}:WebThickness:{WebThickness}:FlangeThickness:{FlangeThickness}:FilletRadius:{FilletRadius}:EdgeRadius:{EdgeRadius}:FlangeSlope:{FlangeSlope}".format(
            sup=IfcParameterizedProfileDef.__str__(self),
            Depth=self.Depth,
            FlangeWidth=self.FlangeWidth,
            WebThickness=self.WebThickness,
            FlangeThickness=self.FlangeThickness,
            FilletRadius=self.FilletRadius,
            EdgeRadius=self.EdgeRadius,
            FlangeSlope=self.FlangeSlope,
        )

    def __json__(self):
        sup = IfcParameterizedProfileDef.__json__(self)
        attrs = {'Depth': self.Depth, 'FlangeWidth': self.FlangeWidth, 'WebThickness': self.WebThickness,
                 'FlangeThickness': self.FlangeThickness, 'FilletRadius': self.FilletRadius,
                 'EdgeRadius': self.EdgeRadius, 'FlangeSlope': self.FlangeSlope}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcVector(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.Orientation = args.pop()
        self.Magnitude = args.pop()

    def __str__(self):
        return "{sup}:Orientation:{Orientation}:Magnitude:{Magnitude}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            Orientation=self.Orientation,
            Magnitude=self.Magnitude,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'Orientation': self.Orientation, 'Magnitude': self.Magnitude}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcVertexLoop(IfcLoop):
    def __init__(self, rtype, args):
        IfcLoop.__init__(self, rtype, args)
        self.LoopVertex = args.pop()

    def __str__(self):
        return "{sup}:LoopVertex:{LoopVertex}".format(
            sup=IfcLoop.__str__(self),
            LoopVertex=self.LoopVertex,
        )

    def __json__(self):
        sup = IfcLoop.__json__(self)
        attrs = {'LoopVertex': self.LoopVertex}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcWindowStyle(IfcTypeProduct):
    def __init__(self, rtype, args):
        IfcTypeProduct.__init__(self, rtype, args)
        self.ConstructionType = args.pop()
        self.OperationType = args.pop()
        self.ParameterTakesPrecedence = args.pop()
        self.Sizeable = args.pop()

    def __str__(self):
        return "{sup}:ConstructionType:{ConstructionType}:OperationType:{OperationType}:ParameterTakesPrecedence:{ParameterTakesPrecedence}:Sizeable:{Sizeable}".format(
            sup=IfcTypeProduct.__str__(self),
            ConstructionType=self.ConstructionType,
            OperationType=self.OperationType,
            ParameterTakesPrecedence=self.ParameterTakesPrecedence,
            Sizeable=self.Sizeable,
        )

    def __json__(self):
        sup = IfcTypeProduct.__json__(self)
        attrs = {'ConstructionType': self.ConstructionType, 'OperationType': self.OperationType,
                 'ParameterTakesPrecedence': self.ParameterTakesPrecedence, 'Sizeable': self.Sizeable}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcZShapeProfileDef(IfcParameterizedProfileDef):
    def __init__(self, rtype, args):
        IfcParameterizedProfileDef.__init__(self, rtype, args)
        self.Depth = args.pop()
        self.FlangeWidth = args.pop()
        self.WebThickness = args.pop()
        self.FlangeThickness = args.pop()
        self.FilletRadius = args.pop()
        self.EdgeRadius = args.pop()

    def __str__(self):
        return "{sup}:Depth:{Depth}:FlangeWidth:{FlangeWidth}:WebThickness:{WebThickness}:FlangeThickness:{FlangeThickness}:FilletRadius:{FilletRadius}:EdgeRadius:{EdgeRadius}".format(
            sup=IfcParameterizedProfileDef.__str__(self),
            Depth=self.Depth,
            FlangeWidth=self.FlangeWidth,
            WebThickness=self.WebThickness,
            FlangeThickness=self.FlangeThickness,
            FilletRadius=self.FilletRadius,
            EdgeRadius=self.EdgeRadius,
        )

    def __json__(self):
        sup = IfcParameterizedProfileDef.__json__(self)
        attrs = {'Depth': self.Depth, 'FlangeWidth': self.FlangeWidth, 'WebThickness': self.WebThickness,
                 'FlangeThickness': self.FlangeThickness, 'FilletRadius': self.FilletRadius,
                 'EdgeRadius': self.EdgeRadius}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAdvancedFace(IfcFaceSurface):
    def __init__(self, rtype, args):
        IfcFaceSurface.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcFaceSurface.__str__(self),
        )

    def __json__(self):
        sup = IfcFaceSurface.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAlignment2DHorizontal(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.StartDistAlong = args.pop()
        self.Segments = args.pop()

    def __str__(self):
        return "{sup}:StartDistAlong:{StartDistAlong}:Segments:{Segments}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            StartDistAlong=self.StartDistAlong,
            Segments=self.Segments,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'StartDistAlong': self.StartDistAlong, 'Segments': self.Segments}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcAlignment2DSegment(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.TangentialContinuity = args.pop()
        self.StartTag = args.pop()
        self.EndTag = args.pop()

    def __str__(self):
        return "{sup}:TangentialContinuity:{TangentialContinuity}:StartTag:{StartTag}:EndTag:{EndTag}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            TangentialContinuity=self.TangentialContinuity,
            StartTag=self.StartTag,
            EndTag=self.EndTag,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'TangentialContinuity': self.TangentialContinuity, 'StartTag': self.StartTag, 'EndTag': self.EndTag}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAlignment2DVertical(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.Segments = args.pop()

    def __str__(self):
        return "{sup}:Segments:{Segments}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            Segments=self.Segments,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'Segments': self.Segments}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcAlignment2DVerticalSegment(IfcAlignment2DSegment):
    def __init__(self, rtype, args):
        IfcAlignment2DSegment.__init__(self, rtype, args)
        self.StartDistAlong = args.pop()
        self.HorizontalLength = args.pop()
        self.StartHeight = args.pop()
        self.StartGradient = args.pop()

    def __str__(self):
        return "{sup}:StartDistAlong:{StartDistAlong}:HorizontalLength:{HorizontalLength}:StartHeight:{StartHeight}:StartGradient:{StartGradient}".format(
            sup=IfcAlignment2DSegment.__str__(self),
            StartDistAlong=self.StartDistAlong,
            HorizontalLength=self.HorizontalLength,
            StartHeight=self.StartHeight,
            StartGradient=self.StartGradient,
        )

    def __json__(self):
        sup = IfcAlignment2DSegment.__json__(self)
        attrs = {'StartDistAlong': self.StartDistAlong, 'HorizontalLength': self.HorizontalLength,
                 'StartHeight': self.StartHeight, 'StartGradient': self.StartGradient}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAnnotationFillArea(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.OuterBoundary = args.pop()
        self.InnerBoundaries = args.pop()

    def __str__(self):
        return "{sup}:OuterBoundary:{OuterBoundary}:InnerBoundaries:{InnerBoundaries}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            OuterBoundary=self.OuterBoundary,
            InnerBoundaries=self.InnerBoundaries,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'OuterBoundary': self.OuterBoundary, 'InnerBoundaries': self.InnerBoundaries}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAsymmetricIShapeProfileDef(IfcParameterizedProfileDef):
    def __init__(self, rtype, args):
        IfcParameterizedProfileDef.__init__(self, rtype, args)
        self.BottomFlangeWidth = args.pop()
        self.OverallDepth = args.pop()
        self.WebThickness = args.pop()
        self.BottomFlangeThickness = args.pop()
        self.BottomFlangeFilletRadius = args.pop()
        self.TopFlangeWidth = args.pop()
        self.TopFlangeThickness = args.pop()
        self.TopFlangeFilletRadius = args.pop()
        self.BottomFlangeEdgeRadius = args.pop()
        self.BottomFlangeSlope = args.pop()
        self.TopFlangeEdgeRadius = args.pop()
        self.TopFlangeSlope = args.pop()

    def __str__(self):
        return "{sup}:BottomFlangeWidth:{BottomFlangeWidth}:OverallDepth:{OverallDepth}:WebThickness:{WebThickness}:BottomFlangeThickness:{BottomFlangeThickness}:BottomFlangeFilletRadius:{BottomFlangeFilletRadius}:TopFlangeWidth:{TopFlangeWidth}:TopFlangeThickness:{TopFlangeThickness}:TopFlangeFilletRadius:{TopFlangeFilletRadius}:BottomFlangeEdgeRadius:{BottomFlangeEdgeRadius}:BottomFlangeSlope:{BottomFlangeSlope}:TopFlangeEdgeRadius:{TopFlangeEdgeRadius}:TopFlangeSlope:{TopFlangeSlope}".format(
            sup=IfcParameterizedProfileDef.__str__(self),
            BottomFlangeWidth=self.BottomFlangeWidth,
            OverallDepth=self.OverallDepth,
            WebThickness=self.WebThickness,
            BottomFlangeThickness=self.BottomFlangeThickness,
            BottomFlangeFilletRadius=self.BottomFlangeFilletRadius,
            TopFlangeWidth=self.TopFlangeWidth,
            TopFlangeThickness=self.TopFlangeThickness,
            TopFlangeFilletRadius=self.TopFlangeFilletRadius,
            BottomFlangeEdgeRadius=self.BottomFlangeEdgeRadius,
            BottomFlangeSlope=self.BottomFlangeSlope,
            TopFlangeEdgeRadius=self.TopFlangeEdgeRadius,
            TopFlangeSlope=self.TopFlangeSlope,
        )

    def __json__(self):
        sup = IfcParameterizedProfileDef.__json__(self)
        attrs = {'BottomFlangeWidth': self.BottomFlangeWidth, 'OverallDepth': self.OverallDepth,
                 'WebThickness': self.WebThickness, 'BottomFlangeThickness': self.BottomFlangeThickness,
                 'BottomFlangeFilletRadius': self.BottomFlangeFilletRadius, 'TopFlangeWidth': self.TopFlangeWidth,
                 'TopFlangeThickness': self.TopFlangeThickness, 'TopFlangeFilletRadius': self.TopFlangeFilletRadius,
                 'BottomFlangeEdgeRadius': self.BottomFlangeEdgeRadius, 'BottomFlangeSlope': self.BottomFlangeSlope,
                 'TopFlangeEdgeRadius': self.TopFlangeEdgeRadius, 'TopFlangeSlope': self.TopFlangeSlope}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAxis1Placement(IfcPlacement):
    def __init__(self, rtype, args):
        IfcPlacement.__init__(self, rtype, args)
        self.Axis = args.pop()

    def __str__(self):
        return "{sup}:Axis:{Axis}".format(
            sup=IfcPlacement.__str__(self),
            Axis=self.Axis,
        )

    def __json__(self):
        sup = IfcPlacement.__json__(self)
        attrs = {'Axis': self.Axis}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAxis2Placement2D(IfcPlacement):
    def __init__(self, rtype, args):
        IfcPlacement.__init__(self, rtype, args)
        self.RefDirection = args.pop()

    def __str__(self):
        return "{sup}:RefDirection:{RefDirection}".format(
            sup=IfcPlacement.__str__(self),
            RefDirection=self.RefDirection,
        )

    def __json__(self):
        sup = IfcPlacement.__json__(self)
        attrs = {'RefDirection': self.RefDirection}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAxis2Placement3D(IfcPlacement):
    def __init__(self, rtype, args):
        IfcPlacement.__init__(self, rtype, args)
        self.Axis = args.pop()
        self.RefDirection = args.pop()

    def __str__(self):
        return "{sup}:Axis:{Axis}:RefDirection:{RefDirection}".format(
            sup=IfcPlacement.__str__(self),
            Axis=self.Axis,
            RefDirection=self.RefDirection,
        )

    def __json__(self):
        sup = IfcPlacement.__json__(self)
        attrs = {'Axis': self.Axis, 'RefDirection': self.RefDirection}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBooleanResult(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.Operator = args.pop()
        self.FirstOperand = args.pop()
        self.SecondOperand = args.pop()

    def __str__(self):
        return "{sup}:Operator:{Operator}:FirstOperand:{FirstOperand}:SecondOperand:{SecondOperand}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            Operator=self.Operator,
            FirstOperand=self.FirstOperand,
            SecondOperand=self.SecondOperand,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'Operator': self.Operator, 'FirstOperand': self.FirstOperand, 'SecondOperand': self.SecondOperand}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcBoundedSurface(IfcSurface):
    def __init__(self, rtype, args):
        IfcSurface.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcSurface.__str__(self),
        )

    def __json__(self):
        sup = IfcSurface.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBoundingBox(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.Corner = args.pop()
        self.XDim = args.pop()
        self.YDim = args.pop()
        self.ZDim = args.pop()

    def __str__(self):
        return "{sup}:Corner:{Corner}:XDim:{XDim}:YDim:{YDim}:ZDim:{ZDim}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            Corner=self.Corner,
            XDim=self.XDim,
            YDim=self.YDim,
            ZDim=self.ZDim,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'Corner': self.Corner, 'XDim': self.XDim, 'YDim': self.YDim, 'ZDim': self.ZDim}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBoxedHalfSpace(IfcHalfSpaceSolid):
    def __init__(self, rtype, args):
        IfcHalfSpaceSolid.__init__(self, rtype, args)
        self.Enclosure = args.pop()

    def __str__(self):
        return "{sup}:Enclosure:{Enclosure}".format(
            sup=IfcHalfSpaceSolid.__str__(self),
            Enclosure=self.Enclosure,
        )

    def __json__(self):
        sup = IfcHalfSpaceSolid.__json__(self)
        attrs = {'Enclosure': self.Enclosure}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCShapeProfileDef(IfcParameterizedProfileDef):
    def __init__(self, rtype, args):
        IfcParameterizedProfileDef.__init__(self, rtype, args)
        self.Depth = args.pop()
        self.Width = args.pop()
        self.WallThickness = args.pop()
        self.Girth = args.pop()
        self.InternalFilletRadius = args.pop()

    def __str__(self):
        return "{sup}:Depth:{Depth}:Width:{Width}:WallThickness:{WallThickness}:Girth:{Girth}:InternalFilletRadius:{InternalFilletRadius}".format(
            sup=IfcParameterizedProfileDef.__str__(self),
            Depth=self.Depth,
            Width=self.Width,
            WallThickness=self.WallThickness,
            Girth=self.Girth,
            InternalFilletRadius=self.InternalFilletRadius,
        )

    def __json__(self):
        sup = IfcParameterizedProfileDef.__json__(self)
        attrs = {'Depth': self.Depth, 'Width': self.Width, 'WallThickness': self.WallThickness, 'Girth': self.Girth,
                 'InternalFilletRadius': self.InternalFilletRadius}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCartesianPoint(IfcPoint):
    def __init__(self, rtype, args):
        IfcPoint.__init__(self, rtype, args)
        self.Coordinates = args.pop()

    def __str__(self):
        return "{sup}:Coordinates:{Coordinates}".format(
            sup=IfcPoint.__str__(self),
            Coordinates=self.Coordinates,
        )

    def __json__(self):
        sup = IfcPoint.__json__(self)
        attrs = {'Coordinates': self.Coordinates}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcCartesianPointList(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCartesianPointList2D(IfcCartesianPointList):
    def __init__(self, rtype, args):
        IfcCartesianPointList.__init__(self, rtype, args)
        self.CoordList = args.pop()
        self.TagList = args.pop()

    def __str__(self):
        return "{sup}:CoordList:{CoordList}:TagList:{TagList}".format(
            sup=IfcCartesianPointList.__str__(self),
            CoordList=self.CoordList,
            TagList=self.TagList,
        )

    def __json__(self):
        sup = IfcCartesianPointList.__json__(self)
        attrs = {'CoordList': self.CoordList, 'TagList': self.TagList}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCartesianPointList3D(IfcCartesianPointList):
    def __init__(self, rtype, args):
        IfcCartesianPointList.__init__(self, rtype, args)
        self.CoordList = args.pop()
        self.TagList = args.pop()

    def __str__(self):
        return "{sup}:CoordList:{CoordList}:TagList:{TagList}".format(
            sup=IfcCartesianPointList.__str__(self),
            CoordList=self.CoordList,
            TagList=self.TagList,
        )

    def __json__(self):
        sup = IfcCartesianPointList.__json__(self)
        attrs = {'CoordList': self.CoordList, 'TagList': self.TagList}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcCartesianTransformationOperator(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.Axis1 = args.pop()
        self.Axis2 = args.pop()
        self.LocalOrigin = args.pop()
        self.Scale = args.pop()

    def __str__(self):
        return "{sup}:Axis1:{Axis1}:Axis2:{Axis2}:LocalOrigin:{LocalOrigin}:Scale:{Scale}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            Axis1=self.Axis1,
            Axis2=self.Axis2,
            LocalOrigin=self.LocalOrigin,
            Scale=self.Scale,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'Axis1': self.Axis1, 'Axis2': self.Axis2, 'LocalOrigin': self.LocalOrigin, 'Scale': self.Scale}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCartesianTransformationOperator2D(IfcCartesianTransformationOperator):
    def __init__(self, rtype, args):
        IfcCartesianTransformationOperator.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcCartesianTransformationOperator.__str__(self),
        )

    def __json__(self):
        sup = IfcCartesianTransformationOperator.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCartesianTransformationOperator2DnonUniform(IfcCartesianTransformationOperator2D):
    def __init__(self, rtype, args):
        IfcCartesianTransformationOperator2D.__init__(self, rtype, args)
        self.Scale2 = args.pop()

    def __str__(self):
        return "{sup}:Scale2:{Scale2}".format(
            sup=IfcCartesianTransformationOperator2D.__str__(self),
            Scale2=self.Scale2,
        )

    def __json__(self):
        sup = IfcCartesianTransformationOperator2D.__json__(self)
        attrs = {'Scale2': self.Scale2}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCartesianTransformationOperator3D(IfcCartesianTransformationOperator):
    def __init__(self, rtype, args):
        IfcCartesianTransformationOperator.__init__(self, rtype, args)
        self.Axis3 = args.pop()

    def __str__(self):
        return "{sup}:Axis3:{Axis3}".format(
            sup=IfcCartesianTransformationOperator.__str__(self),
            Axis3=self.Axis3,
        )

    def __json__(self):
        sup = IfcCartesianTransformationOperator.__json__(self)
        attrs = {'Axis3': self.Axis3}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCartesianTransformationOperator3DnonUniform(IfcCartesianTransformationOperator3D):
    def __init__(self, rtype, args):
        IfcCartesianTransformationOperator3D.__init__(self, rtype, args)
        self.Scale2 = args.pop()
        self.Scale3 = args.pop()

    def __str__(self):
        return "{sup}:Scale2:{Scale2}:Scale3:{Scale3}".format(
            sup=IfcCartesianTransformationOperator3D.__str__(self),
            Scale2=self.Scale2,
            Scale3=self.Scale3,
        )

    def __json__(self):
        sup = IfcCartesianTransformationOperator3D.__json__(self)
        attrs = {'Scale2': self.Scale2, 'Scale3': self.Scale3}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCircleProfileDef(IfcParameterizedProfileDef):
    def __init__(self, rtype, args):
        IfcParameterizedProfileDef.__init__(self, rtype, args)
        self.Radius = args.pop()

    def __str__(self):
        return "{sup}:Radius:{Radius}".format(
            sup=IfcParameterizedProfileDef.__str__(self),
            Radius=self.Radius,
        )

    def __json__(self):
        sup = IfcParameterizedProfileDef.__json__(self)
        attrs = {'Radius': self.Radius}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcClosedShell(IfcConnectedFaceSet):
    def __init__(self, rtype, args):
        IfcConnectedFaceSet.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcConnectedFaceSet.__str__(self),
        )

    def __json__(self):
        sup = IfcConnectedFaceSet.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcColourRgb(IfcColourSpecification):
    def __init__(self, rtype, args):
        IfcColourSpecification.__init__(self, rtype, args)
        self.Red = args.pop()
        self.Green = args.pop()
        self.Blue = args.pop()

    def __str__(self):
        return "{sup}:Red:{Red}:Green:{Green}:Blue:{Blue}".format(
            sup=IfcColourSpecification.__str__(self),
            Red=self.Red,
            Green=self.Green,
            Blue=self.Blue,
        )

    def __json__(self):
        sup = IfcColourSpecification.__json__(self)
        attrs = {'Red': self.Red, 'Green': self.Green, 'Blue': self.Blue}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcComplexProperty(IfcProperty):
    def __init__(self, rtype, args):
        IfcProperty.__init__(self, rtype, args)
        self.UsageName = args.pop()
        self.HasProperties = args.pop()

    def __str__(self):
        return "{sup}:UsageName:{UsageName}:HasProperties:{HasProperties}".format(
            sup=IfcProperty.__str__(self),
            UsageName=self.UsageName,
            HasProperties=self.HasProperties,
        )

    def __json__(self):
        sup = IfcProperty.__json__(self)
        attrs = {'UsageName': self.UsageName, 'HasProperties': self.HasProperties}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCompositeCurveSegment(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.Transition = args.pop()
        self.SameSense = args.pop()
        self.ParentCurve = args.pop()

    def __str__(self):
        return "{sup}:Transition:{Transition}:SameSense:{SameSense}:ParentCurve:{ParentCurve}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            Transition=self.Transition,
            SameSense=self.SameSense,
            ParentCurve=self.ParentCurve,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'Transition': self.Transition, 'SameSense': self.SameSense, 'ParentCurve': self.ParentCurve}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcConstructionResourceType(IfcTypeResource):
    def __init__(self, rtype, args):
        IfcTypeResource.__init__(self, rtype, args)
        self.BaseCosts = args.pop()
        self.BaseQuantity = args.pop()

    def __str__(self):
        return "{sup}:BaseCosts:{BaseCosts}:BaseQuantity:{BaseQuantity}".format(
            sup=IfcTypeResource.__str__(self),
            BaseCosts=self.BaseCosts,
            BaseQuantity=self.BaseQuantity,
        )

    def __json__(self):
        sup = IfcTypeResource.__json__(self)
        attrs = {'BaseCosts': self.BaseCosts, 'BaseQuantity': self.BaseQuantity}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcContext(IfcObjectDefinition):
    def __init__(self, rtype, args):
        IfcObjectDefinition.__init__(self, rtype, args)
        self.ObjectType = args.pop()
        self.LongName = args.pop()
        self.Phase = args.pop()
        self.RepresentationContexts = args.pop()
        self.UnitsInContext = args.pop()

    def __str__(self):
        return "{sup}:ObjectType:{ObjectType}:LongName:{LongName}:Phase:{Phase}:RepresentationContexts:{RepresentationContexts}:UnitsInContext:{UnitsInContext}".format(
            sup=IfcObjectDefinition.__str__(self),
            ObjectType=self.ObjectType,
            LongName=self.LongName,
            Phase=self.Phase,
            RepresentationContexts=self.RepresentationContexts,
            UnitsInContext=self.UnitsInContext,
        )

    def __json__(self):
        sup = IfcObjectDefinition.__json__(self)
        attrs = {'ObjectType': self.ObjectType, 'LongName': self.LongName, 'Phase': self.Phase,
                 'RepresentationContexts': self.RepresentationContexts, 'UnitsInContext': self.UnitsInContext}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCrewResourceType(IfcConstructionResourceType):
    def __init__(self, rtype, args):
        IfcConstructionResourceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcConstructionResourceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcConstructionResourceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcCsgPrimitive3D(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.Position = args.pop()

    def __str__(self):
        return "{sup}:Position:{Position}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            Position=self.Position,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'Position': self.Position}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCsgSolid(IfcSolidModel):
    def __init__(self, rtype, args):
        IfcSolidModel.__init__(self, rtype, args)
        self.TreeRootExpression = args.pop()

    def __str__(self):
        return "{sup}:TreeRootExpression:{TreeRootExpression}".format(
            sup=IfcSolidModel.__str__(self),
            TreeRootExpression=self.TreeRootExpression,
        )

    def __json__(self):
        sup = IfcSolidModel.__json__(self)
        attrs = {'TreeRootExpression': self.TreeRootExpression}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcCurve(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCurveBoundedPlane(IfcBoundedSurface):
    def __init__(self, rtype, args):
        IfcBoundedSurface.__init__(self, rtype, args)
        self.BasisSurface = args.pop()
        self.OuterBoundary = args.pop()
        self.InnerBoundaries = args.pop()

    def __str__(self):
        return "{sup}:BasisSurface:{BasisSurface}:OuterBoundary:{OuterBoundary}:InnerBoundaries:{InnerBoundaries}".format(
            sup=IfcBoundedSurface.__str__(self),
            BasisSurface=self.BasisSurface,
            OuterBoundary=self.OuterBoundary,
            InnerBoundaries=self.InnerBoundaries,
        )

    def __json__(self):
        sup = IfcBoundedSurface.__json__(self)
        attrs = {'BasisSurface': self.BasisSurface, 'OuterBoundary': self.OuterBoundary,
                 'InnerBoundaries': self.InnerBoundaries}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCurveBoundedSurface(IfcBoundedSurface):
    def __init__(self, rtype, args):
        IfcBoundedSurface.__init__(self, rtype, args)
        self.BasisSurface = args.pop()
        self.Boundaries = args.pop()
        self.ImplicitOuter = args.pop()

    def __str__(self):
        return "{sup}:BasisSurface:{BasisSurface}:Boundaries:{Boundaries}:ImplicitOuter:{ImplicitOuter}".format(
            sup=IfcBoundedSurface.__str__(self),
            BasisSurface=self.BasisSurface,
            Boundaries=self.Boundaries,
            ImplicitOuter=self.ImplicitOuter,
        )

    def __json__(self):
        sup = IfcBoundedSurface.__json__(self)
        attrs = {'BasisSurface': self.BasisSurface, 'Boundaries': self.Boundaries, 'ImplicitOuter': self.ImplicitOuter}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDirection(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.DirectionRatios = args.pop()

    def __str__(self):
        return "{sup}:DirectionRatios:{DirectionRatios}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            DirectionRatios=self.DirectionRatios,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'DirectionRatios': self.DirectionRatios}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDistanceExpression(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.DistanceAlong = args.pop()
        self.OffsetLateral = args.pop()
        self.OffsetVertical = args.pop()
        self.OffsetLongitudinal = args.pop()
        self.AlongHorizontal = args.pop()

    def __str__(self):
        return "{sup}:DistanceAlong:{DistanceAlong}:OffsetLateral:{OffsetLateral}:OffsetVertical:{OffsetVertical}:OffsetLongitudinal:{OffsetLongitudinal}:AlongHorizontal:{AlongHorizontal}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            DistanceAlong=self.DistanceAlong,
            OffsetLateral=self.OffsetLateral,
            OffsetVertical=self.OffsetVertical,
            OffsetLongitudinal=self.OffsetLongitudinal,
            AlongHorizontal=self.AlongHorizontal,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'DistanceAlong': self.DistanceAlong, 'OffsetLateral': self.OffsetLateral,
                 'OffsetVertical': self.OffsetVertical, 'OffsetLongitudinal': self.OffsetLongitudinal,
                 'AlongHorizontal': self.AlongHorizontal}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDoorStyle(IfcTypeProduct):
    def __init__(self, rtype, args):
        IfcTypeProduct.__init__(self, rtype, args)
        self.OperationType = args.pop()
        self.ConstructionType = args.pop()
        self.ParameterTakesPrecedence = args.pop()
        self.Sizeable = args.pop()

    def __str__(self):
        return "{sup}:OperationType:{OperationType}:ConstructionType:{ConstructionType}:ParameterTakesPrecedence:{ParameterTakesPrecedence}:Sizeable:{Sizeable}".format(
            sup=IfcTypeProduct.__str__(self),
            OperationType=self.OperationType,
            ConstructionType=self.ConstructionType,
            ParameterTakesPrecedence=self.ParameterTakesPrecedence,
            Sizeable=self.Sizeable,
        )

    def __json__(self):
        sup = IfcTypeProduct.__json__(self)
        attrs = {'OperationType': self.OperationType, 'ConstructionType': self.ConstructionType,
                 'ParameterTakesPrecedence': self.ParameterTakesPrecedence, 'Sizeable': self.Sizeable}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcEdgeLoop(IfcLoop):
    def __init__(self, rtype, args):
        IfcLoop.__init__(self, rtype, args)
        self.EdgeList = args.pop()

    def __str__(self):
        return "{sup}:EdgeList:{EdgeList}".format(
            sup=IfcLoop.__str__(self),
            EdgeList=self.EdgeList,
        )

    def __json__(self):
        sup = IfcLoop.__json__(self)
        attrs = {'EdgeList': self.EdgeList}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcElementQuantity(IfcQuantitySet):
    def __init__(self, rtype, args):
        IfcQuantitySet.__init__(self, rtype, args)
        self.MethodOfMeasurement = args.pop()
        self.Quantities = args.pop()

    def __str__(self):
        return "{sup}:MethodOfMeasurement:{MethodOfMeasurement}:Quantities:{Quantities}".format(
            sup=IfcQuantitySet.__str__(self),
            MethodOfMeasurement=self.MethodOfMeasurement,
            Quantities=self.Quantities,
        )

    def __json__(self):
        sup = IfcQuantitySet.__json__(self)
        attrs = {'MethodOfMeasurement': self.MethodOfMeasurement, 'Quantities': self.Quantities}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcElementType(IfcTypeProduct):
    def __init__(self, rtype, args):
        IfcTypeProduct.__init__(self, rtype, args)
        self.ElementType = args.pop()

    def __str__(self):
        return "{sup}:ElementType:{ElementType}".format(
            sup=IfcTypeProduct.__str__(self),
            ElementType=self.ElementType,
        )

    def __json__(self):
        sup = IfcTypeProduct.__json__(self)
        attrs = {'ElementType': self.ElementType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcElementarySurface(IfcSurface):
    def __init__(self, rtype, args):
        IfcSurface.__init__(self, rtype, args)
        self.Position = args.pop()

    def __str__(self):
        return "{sup}:Position:{Position}".format(
            sup=IfcSurface.__str__(self),
            Position=self.Position,
        )

    def __json__(self):
        sup = IfcSurface.__json__(self)
        attrs = {'Position': self.Position}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcEllipseProfileDef(IfcParameterizedProfileDef):
    def __init__(self, rtype, args):
        IfcParameterizedProfileDef.__init__(self, rtype, args)
        self.SemiAxis1 = args.pop()
        self.SemiAxis2 = args.pop()

    def __str__(self):
        return "{sup}:SemiAxis1:{SemiAxis1}:SemiAxis2:{SemiAxis2}".format(
            sup=IfcParameterizedProfileDef.__str__(self),
            SemiAxis1=self.SemiAxis1,
            SemiAxis2=self.SemiAxis2,
        )

    def __json__(self):
        sup = IfcParameterizedProfileDef.__json__(self)
        attrs = {'SemiAxis1': self.SemiAxis1, 'SemiAxis2': self.SemiAxis2}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcEventType(IfcTypeProcess):
    def __init__(self, rtype, args):
        IfcTypeProcess.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.EventTriggerType = args.pop()
        self.UserDefinedEventTriggerType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:EventTriggerType:{EventTriggerType}:UserDefinedEventTriggerType:{UserDefinedEventTriggerType}".format(
            sup=IfcTypeProcess.__str__(self),
            PredefinedType=self.PredefinedType,
            EventTriggerType=self.EventTriggerType,
            UserDefinedEventTriggerType=self.UserDefinedEventTriggerType,
        )

    def __json__(self):
        sup = IfcTypeProcess.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'EventTriggerType': self.EventTriggerType,
                 'UserDefinedEventTriggerType': self.UserDefinedEventTriggerType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcExtrudedAreaSolid(IfcSweptAreaSolid):
    def __init__(self, rtype, args):
        IfcSweptAreaSolid.__init__(self, rtype, args)
        self.ExtrudedDirection = args.pop()
        self.Depth = args.pop()

    def __str__(self):
        return "{sup}:ExtrudedDirection:{ExtrudedDirection}:Depth:{Depth}".format(
            sup=IfcSweptAreaSolid.__str__(self),
            ExtrudedDirection=self.ExtrudedDirection,
            Depth=self.Depth,
        )

    def __json__(self):
        sup = IfcSweptAreaSolid.__json__(self)
        attrs = {'ExtrudedDirection': self.ExtrudedDirection, 'Depth': self.Depth}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcExtrudedAreaSolidTapered(IfcExtrudedAreaSolid):
    def __init__(self, rtype, args):
        IfcExtrudedAreaSolid.__init__(self, rtype, args)
        self.EndSweptArea = args.pop()

    def __str__(self):
        return "{sup}:EndSweptArea:{EndSweptArea}".format(
            sup=IfcExtrudedAreaSolid.__str__(self),
            EndSweptArea=self.EndSweptArea,
        )

    def __json__(self):
        sup = IfcExtrudedAreaSolid.__json__(self)
        attrs = {'EndSweptArea': self.EndSweptArea}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFaceBasedSurfaceModel(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.FbsmFaces = args.pop()

    def __str__(self):
        return "{sup}:FbsmFaces:{FbsmFaces}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            FbsmFaces=self.FbsmFaces,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'FbsmFaces': self.FbsmFaces}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFillAreaStyleHatching(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.HatchLineAppearance = args.pop()
        self.StartOfNextHatchLine = args.pop()
        self.PointOfReferenceHatchLine = args.pop()
        self.PatternStart = args.pop()
        self.HatchLineAngle = args.pop()

    def __str__(self):
        return "{sup}:HatchLineAppearance:{HatchLineAppearance}:StartOfNextHatchLine:{StartOfNextHatchLine}:PointOfReferenceHatchLine:{PointOfReferenceHatchLine}:PatternStart:{PatternStart}:HatchLineAngle:{HatchLineAngle}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            HatchLineAppearance=self.HatchLineAppearance,
            StartOfNextHatchLine=self.StartOfNextHatchLine,
            PointOfReferenceHatchLine=self.PointOfReferenceHatchLine,
            PatternStart=self.PatternStart,
            HatchLineAngle=self.HatchLineAngle,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'HatchLineAppearance': self.HatchLineAppearance, 'StartOfNextHatchLine': self.StartOfNextHatchLine,
                 'PointOfReferenceHatchLine': self.PointOfReferenceHatchLine, 'PatternStart': self.PatternStart,
                 'HatchLineAngle': self.HatchLineAngle}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFillAreaStyleTiles(IfcGeometricRepresentationItem):
    def __init__(self, rtype, args):
        IfcGeometricRepresentationItem.__init__(self, rtype, args)
        self.TilingPattern = args.pop()
        self.Tiles = args.pop()
        self.TilingScale = args.pop()

    def __str__(self):
        return "{sup}:TilingPattern:{TilingPattern}:Tiles:{Tiles}:TilingScale:{TilingScale}".format(
            sup=IfcGeometricRepresentationItem.__str__(self),
            TilingPattern=self.TilingPattern,
            Tiles=self.Tiles,
            TilingScale=self.TilingScale,
        )

    def __json__(self):
        sup = IfcGeometricRepresentationItem.__json__(self)
        attrs = {'TilingPattern': self.TilingPattern, 'Tiles': self.Tiles, 'TilingScale': self.TilingScale}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFixedReferenceSweptAreaSolid(IfcSweptAreaSolid):
    def __init__(self, rtype, args):
        IfcSweptAreaSolid.__init__(self, rtype, args)
        self.Directrix = args.pop()
        self.StartParam = args.pop()
        self.EndParam = args.pop()
        self.FixedReference = args.pop()

    def __str__(self):
        return "{sup}:Directrix:{Directrix}:StartParam:{StartParam}:EndParam:{EndParam}:FixedReference:{FixedReference}".format(
            sup=IfcSweptAreaSolid.__str__(self),
            Directrix=self.Directrix,
            StartParam=self.StartParam,
            EndParam=self.EndParam,
            FixedReference=self.FixedReference,
        )

    def __json__(self):
        sup = IfcSweptAreaSolid.__json__(self)
        attrs = {'Directrix': self.Directrix, 'StartParam': self.StartParam, 'EndParam': self.EndParam,
                 'FixedReference': self.FixedReference}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFurnishingElementType(IfcElementType):
    def __init__(self, rtype, args):
        IfcElementType.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcElementType.__str__(self),
        )

    def __json__(self):
        sup = IfcElementType.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFurnitureType(IfcFurnishingElementType):
    def __init__(self, rtype, args):
        IfcFurnishingElementType.__init__(self, rtype, args)
        self.AssemblyPlace = args.pop()
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:AssemblyPlace:{AssemblyPlace}:PredefinedType:{PredefinedType}".format(
            sup=IfcFurnishingElementType.__str__(self),
            AssemblyPlace=self.AssemblyPlace,
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFurnishingElementType.__json__(self)
        attrs = {'AssemblyPlace': self.AssemblyPlace, 'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcGeographicElementType(IfcElementType):
    def __init__(self, rtype, args):
        IfcElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcGeometricCurveSet(IfcGeometricSet):
    def __init__(self, rtype, args):
        IfcGeometricSet.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcGeometricSet.__str__(self),
        )

    def __json__(self):
        sup = IfcGeometricSet.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcIShapeProfileDef(IfcParameterizedProfileDef):
    def __init__(self, rtype, args):
        IfcParameterizedProfileDef.__init__(self, rtype, args)
        self.OverallWidth = args.pop()
        self.OverallDepth = args.pop()
        self.WebThickness = args.pop()
        self.FlangeThickness = args.pop()
        self.FilletRadius = args.pop()
        self.FlangeEdgeRadius = args.pop()
        self.FlangeSlope = args.pop()

    def __str__(self):
        return "{sup}:OverallWidth:{OverallWidth}:OverallDepth:{OverallDepth}:WebThickness:{WebThickness}:FlangeThickness:{FlangeThickness}:FilletRadius:{FilletRadius}:FlangeEdgeRadius:{FlangeEdgeRadius}:FlangeSlope:{FlangeSlope}".format(
            sup=IfcParameterizedProfileDef.__str__(self),
            OverallWidth=self.OverallWidth,
            OverallDepth=self.OverallDepth,
            WebThickness=self.WebThickness,
            FlangeThickness=self.FlangeThickness,
            FilletRadius=self.FilletRadius,
            FlangeEdgeRadius=self.FlangeEdgeRadius,
            FlangeSlope=self.FlangeSlope,
        )

    def __json__(self):
        sup = IfcParameterizedProfileDef.__json__(self)
        attrs = {'OverallWidth': self.OverallWidth, 'OverallDepth': self.OverallDepth,
                 'WebThickness': self.WebThickness, 'FlangeThickness': self.FlangeThickness,
                 'FilletRadius': self.FilletRadius, 'FlangeEdgeRadius': self.FlangeEdgeRadius,
                 'FlangeSlope': self.FlangeSlope}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcIndexedPolygonalFace(IfcTessellatedItem):
    def __init__(self, rtype, args):
        IfcTessellatedItem.__init__(self, rtype, args)
        self.CoordIndex = args.pop()

    def __str__(self):
        return "{sup}:CoordIndex:{CoordIndex}".format(
            sup=IfcTessellatedItem.__str__(self),
            CoordIndex=self.CoordIndex,
        )

    def __json__(self):
        sup = IfcTessellatedItem.__json__(self)
        attrs = {'CoordIndex': self.CoordIndex}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcIndexedPolygonalFaceWithVoids(IfcIndexedPolygonalFace):
    def __init__(self, rtype, args):
        IfcIndexedPolygonalFace.__init__(self, rtype, args)
        self.InnerCoordIndices = args.pop()

    def __str__(self):
        return "{sup}:InnerCoordIndices:{InnerCoordIndices}".format(
            sup=IfcIndexedPolygonalFace.__str__(self),
            InnerCoordIndices=self.InnerCoordIndices,
        )

    def __json__(self):
        sup = IfcIndexedPolygonalFace.__json__(self)
        attrs = {'InnerCoordIndices': self.InnerCoordIndices}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLShapeProfileDef(IfcParameterizedProfileDef):
    def __init__(self, rtype, args):
        IfcParameterizedProfileDef.__init__(self, rtype, args)
        self.Depth = args.pop()
        self.Width = args.pop()
        self.Thickness = args.pop()
        self.FilletRadius = args.pop()
        self.EdgeRadius = args.pop()
        self.LegSlope = args.pop()

    def __str__(self):
        return "{sup}:Depth:{Depth}:Width:{Width}:Thickness:{Thickness}:FilletRadius:{FilletRadius}:EdgeRadius:{EdgeRadius}:LegSlope:{LegSlope}".format(
            sup=IfcParameterizedProfileDef.__str__(self),
            Depth=self.Depth,
            Width=self.Width,
            Thickness=self.Thickness,
            FilletRadius=self.FilletRadius,
            EdgeRadius=self.EdgeRadius,
            LegSlope=self.LegSlope,
        )

    def __json__(self):
        sup = IfcParameterizedProfileDef.__json__(self)
        attrs = {'Depth': self.Depth, 'Width': self.Width, 'Thickness': self.Thickness,
                 'FilletRadius': self.FilletRadius, 'EdgeRadius': self.EdgeRadius, 'LegSlope': self.LegSlope}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLaborResourceType(IfcConstructionResourceType):
    def __init__(self, rtype, args):
        IfcConstructionResourceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcConstructionResourceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcConstructionResourceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLine(IfcCurve):
    def __init__(self, rtype, args):
        IfcCurve.__init__(self, rtype, args)
        self.Pnt = args.pop()
        self.Dir = args.pop()

    def __str__(self):
        return "{sup}:Pnt:{Pnt}:Dir:{Dir}".format(
            sup=IfcCurve.__str__(self),
            Pnt=self.Pnt,
            Dir=self.Dir,
        )

    def __json__(self):
        sup = IfcCurve.__json__(self)
        attrs = {'Pnt': self.Pnt, 'Dir': self.Dir}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcManifoldSolidBrep(IfcSolidModel):
    def __init__(self, rtype, args):
        IfcSolidModel.__init__(self, rtype, args)
        self.Outer = args.pop()

    def __str__(self):
        return "{sup}:Outer:{Outer}".format(
            sup=IfcSolidModel.__str__(self),
            Outer=self.Outer,
        )

    def __json__(self):
        sup = IfcSolidModel.__json__(self)
        attrs = {'Outer': self.Outer}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcObject(IfcObjectDefinition):
    def __init__(self, rtype, args):
        IfcObjectDefinition.__init__(self, rtype, args)
        self.ObjectType = args.pop()

    def __str__(self):
        return "{sup}:ObjectType:{ObjectType}".format(
            sup=IfcObjectDefinition.__str__(self),
            ObjectType=self.ObjectType,
        )

    def __json__(self):
        sup = IfcObjectDefinition.__json__(self)
        attrs = {'ObjectType': self.ObjectType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcOffsetCurve(IfcCurve):
    def __init__(self, rtype, args):
        IfcCurve.__init__(self, rtype, args)
        self.BasisCurve = args.pop()

    def __str__(self):
        return "{sup}:BasisCurve:{BasisCurve}".format(
            sup=IfcCurve.__str__(self),
            BasisCurve=self.BasisCurve,
        )

    def __json__(self):
        sup = IfcCurve.__json__(self)
        attrs = {'BasisCurve': self.BasisCurve}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcOffsetCurve2D(IfcOffsetCurve):
    def __init__(self, rtype, args):
        IfcOffsetCurve.__init__(self, rtype, args)
        self.Distance = args.pop()
        self.SelfIntersect = args.pop()

    def __str__(self):
        return "{sup}:Distance:{Distance}:SelfIntersect:{SelfIntersect}".format(
            sup=IfcOffsetCurve.__str__(self),
            Distance=self.Distance,
            SelfIntersect=self.SelfIntersect,
        )

    def __json__(self):
        sup = IfcOffsetCurve.__json__(self)
        attrs = {'Distance': self.Distance, 'SelfIntersect': self.SelfIntersect}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcOffsetCurve3D(IfcOffsetCurve):
    def __init__(self, rtype, args):
        IfcOffsetCurve.__init__(self, rtype, args)
        self.Distance = args.pop()
        self.SelfIntersect = args.pop()
        self.RefDirection = args.pop()

    def __str__(self):
        return "{sup}:Distance:{Distance}:SelfIntersect:{SelfIntersect}:RefDirection:{RefDirection}".format(
            sup=IfcOffsetCurve.__str__(self),
            Distance=self.Distance,
            SelfIntersect=self.SelfIntersect,
            RefDirection=self.RefDirection,
        )

    def __json__(self):
        sup = IfcOffsetCurve.__json__(self)
        attrs = {'Distance': self.Distance, 'SelfIntersect': self.SelfIntersect, 'RefDirection': self.RefDirection}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcOffsetCurveByDistances(IfcOffsetCurve):
    def __init__(self, rtype, args):
        IfcOffsetCurve.__init__(self, rtype, args)
        self.OffsetValues = args.pop()
        self.Tag = args.pop()

    def __str__(self):
        return "{sup}:OffsetValues:{OffsetValues}:Tag:{Tag}".format(
            sup=IfcOffsetCurve.__str__(self),
            OffsetValues=self.OffsetValues,
            Tag=self.Tag,
        )

    def __json__(self):
        sup = IfcOffsetCurve.__json__(self)
        attrs = {'OffsetValues': self.OffsetValues, 'Tag': self.Tag}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPcurve(IfcCurve):
    def __init__(self, rtype, args):
        IfcCurve.__init__(self, rtype, args)
        self.BasisSurface = args.pop()
        self.ReferenceCurve = args.pop()

    def __str__(self):
        return "{sup}:BasisSurface:{BasisSurface}:ReferenceCurve:{ReferenceCurve}".format(
            sup=IfcCurve.__str__(self),
            BasisSurface=self.BasisSurface,
            ReferenceCurve=self.ReferenceCurve,
        )

    def __json__(self):
        sup = IfcCurve.__json__(self)
        attrs = {'BasisSurface': self.BasisSurface, 'ReferenceCurve': self.ReferenceCurve}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPlanarBox(IfcPlanarExtent):
    def __init__(self, rtype, args):
        IfcPlanarExtent.__init__(self, rtype, args)
        self.Placement = args.pop()

    def __str__(self):
        return "{sup}:Placement:{Placement}".format(
            sup=IfcPlanarExtent.__str__(self),
            Placement=self.Placement,
        )

    def __json__(self):
        sup = IfcPlanarExtent.__json__(self)
        attrs = {'Placement': self.Placement}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPlane(IfcElementarySurface):
    def __init__(self, rtype, args):
        IfcElementarySurface.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcElementarySurface.__str__(self),
        )

    def __json__(self):
        sup = IfcElementarySurface.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcPreDefinedColour(IfcPreDefinedItem):
    def __init__(self, rtype, args):
        IfcPreDefinedItem.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcPreDefinedItem.__str__(self),
        )

    def __json__(self):
        sup = IfcPreDefinedItem.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcPreDefinedCurveFont(IfcPreDefinedItem):
    def __init__(self, rtype, args):
        IfcPreDefinedItem.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcPreDefinedItem.__str__(self),
        )

    def __json__(self):
        sup = IfcPreDefinedItem.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcPreDefinedPropertySet(IfcPropertySetDefinition):
    def __init__(self, rtype, args):
        IfcPropertySetDefinition.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcPropertySetDefinition.__str__(self),
        )

    def __json__(self):
        sup = IfcPropertySetDefinition.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcProcedureType(IfcTypeProcess):
    def __init__(self, rtype, args):
        IfcTypeProcess.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcTypeProcess.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcTypeProcess.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcProcess(IfcObject):
    def __init__(self, rtype, args):
        IfcObject.__init__(self, rtype, args)
        self.Identification = args.pop()
        self.LongDescription = args.pop()

    def __str__(self):
        return "{sup}:Identification:{Identification}:LongDescription:{LongDescription}".format(
            sup=IfcObject.__str__(self),
            Identification=self.Identification,
            LongDescription=self.LongDescription,
        )

    def __json__(self):
        sup = IfcObject.__json__(self)
        attrs = {'Identification': self.Identification, 'LongDescription': self.LongDescription}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcProduct(IfcObject):
    def __init__(self, rtype, args):
        IfcObject.__init__(self, rtype, args)
        self.ObjectPlacement = args.pop()
        self.Representation = args.pop()

    def __str__(self):
        return "{sup}:ObjectPlacement:{ObjectPlacement}:Representation:{Representation}".format(
            sup=IfcObject.__str__(self),
            ObjectPlacement=self.ObjectPlacement,
            Representation=self.Representation,
        )

    def __json__(self):
        sup = IfcObject.__json__(self)
        attrs = {'ObjectPlacement': self.ObjectPlacement, 'Representation': self.Representation}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcProject(IfcContext):
    def __init__(self, rtype, args):
        IfcContext.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcContext.__str__(self),
        )

    def __json__(self):
        sup = IfcContext.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcProjectLibrary(IfcContext):
    def __init__(self, rtype, args):
        IfcContext.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcContext.__str__(self),
        )

    def __json__(self):
        sup = IfcContext.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPropertyBoundedValue(IfcSimpleProperty):
    def __init__(self, rtype, args):
        IfcSimpleProperty.__init__(self, rtype, args)
        self.UpperBoundValue = args.pop()
        self.LowerBoundValue = args.pop()
        self.Unit = args.pop()
        self.SetPointValue = args.pop()

    def __str__(self):
        return "{sup}:UpperBoundValue:{UpperBoundValue}:LowerBoundValue:{LowerBoundValue}:Unit:{Unit}:SetPointValue:{SetPointValue}".format(
            sup=IfcSimpleProperty.__str__(self),
            UpperBoundValue=self.UpperBoundValue,
            LowerBoundValue=self.LowerBoundValue,
            Unit=self.Unit,
            SetPointValue=self.SetPointValue,
        )

    def __json__(self):
        sup = IfcSimpleProperty.__json__(self)
        attrs = {'UpperBoundValue': self.UpperBoundValue, 'LowerBoundValue': self.LowerBoundValue, 'Unit': self.Unit,
                 'SetPointValue': self.SetPointValue}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPropertyEnumeratedValue(IfcSimpleProperty):
    def __init__(self, rtype, args):
        IfcSimpleProperty.__init__(self, rtype, args)
        self.EnumerationValues = args.pop()
        self.EnumerationReference = args.pop()

    def __str__(self):
        return "{sup}:EnumerationValues:{EnumerationValues}:EnumerationReference:{EnumerationReference}".format(
            sup=IfcSimpleProperty.__str__(self),
            EnumerationValues=self.EnumerationValues,
            EnumerationReference=self.EnumerationReference,
        )

    def __json__(self):
        sup = IfcSimpleProperty.__json__(self)
        attrs = {'EnumerationValues': self.EnumerationValues, 'EnumerationReference': self.EnumerationReference}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPropertyListValue(IfcSimpleProperty):
    def __init__(self, rtype, args):
        IfcSimpleProperty.__init__(self, rtype, args)
        self.ListValues = args.pop()
        self.Unit = args.pop()

    def __str__(self):
        return "{sup}:ListValues:{ListValues}:Unit:{Unit}".format(
            sup=IfcSimpleProperty.__str__(self),
            ListValues=self.ListValues,
            Unit=self.Unit,
        )

    def __json__(self):
        sup = IfcSimpleProperty.__json__(self)
        attrs = {'ListValues': self.ListValues, 'Unit': self.Unit}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPropertyReferenceValue(IfcSimpleProperty):
    def __init__(self, rtype, args):
        IfcSimpleProperty.__init__(self, rtype, args)
        self.UsageName = args.pop()
        self.PropertyReference = args.pop()

    def __str__(self):
        return "{sup}:UsageName:{UsageName}:PropertyReference:{PropertyReference}".format(
            sup=IfcSimpleProperty.__str__(self),
            UsageName=self.UsageName,
            PropertyReference=self.PropertyReference,
        )

    def __json__(self):
        sup = IfcSimpleProperty.__json__(self)
        attrs = {'UsageName': self.UsageName, 'PropertyReference': self.PropertyReference}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPropertySet(IfcPropertySetDefinition):
    def __init__(self, rtype, args):
        IfcPropertySetDefinition.__init__(self, rtype, args)
        self.HasProperties = args.pop()

    def __str__(self):
        return "{sup}:HasProperties:{HasProperties}".format(
            sup=IfcPropertySetDefinition.__str__(self),
            HasProperties=self.HasProperties,
        )

    def __json__(self):
        sup = IfcPropertySetDefinition.__json__(self)
        attrs = {'HasProperties': self.HasProperties}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPropertySetTemplate(IfcPropertyTemplateDefinition):
    def __init__(self, rtype, args):
        IfcPropertyTemplateDefinition.__init__(self, rtype, args)
        self.TemplateType = args.pop()
        self.ApplicableEntity = args.pop()
        self.HasPropertyTemplates = args.pop()

    def __str__(self):
        return "{sup}:TemplateType:{TemplateType}:ApplicableEntity:{ApplicableEntity}:HasPropertyTemplates:{HasPropertyTemplates}".format(
            sup=IfcPropertyTemplateDefinition.__str__(self),
            TemplateType=self.TemplateType,
            ApplicableEntity=self.ApplicableEntity,
            HasPropertyTemplates=self.HasPropertyTemplates,
        )

    def __json__(self):
        sup = IfcPropertyTemplateDefinition.__json__(self)
        attrs = {'TemplateType': self.TemplateType, 'ApplicableEntity': self.ApplicableEntity,
                 'HasPropertyTemplates': self.HasPropertyTemplates}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPropertySingleValue(IfcSimpleProperty):
    def __init__(self, rtype, args):
        IfcSimpleProperty.__init__(self, rtype, args)
        self.NominalValue = args.pop()
        self.Unit = args.pop()

    def __str__(self):
        return "{sup}:NominalValue:{NominalValue}:Unit:{Unit}".format(
            sup=IfcSimpleProperty.__str__(self),
            NominalValue=self.NominalValue,
            Unit=self.Unit,
        )

    def __json__(self):
        sup = IfcSimpleProperty.__json__(self)
        attrs = {'NominalValue': self.NominalValue, 'Unit': self.Unit}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPropertyTableValue(IfcSimpleProperty):
    def __init__(self, rtype, args):
        IfcSimpleProperty.__init__(self, rtype, args)
        self.DefiningValues = args.pop()
        self.DefinedValues = args.pop()
        self.Expression = args.pop()
        self.DefiningUnit = args.pop()
        self.DefinedUnit = args.pop()
        self.CurveInterpolation = args.pop()

    def __str__(self):
        return "{sup}:DefiningValues:{DefiningValues}:DefinedValues:{DefinedValues}:Expression:{Expression}:DefiningUnit:{DefiningUnit}:DefinedUnit:{DefinedUnit}:CurveInterpolation:{CurveInterpolation}".format(
            sup=IfcSimpleProperty.__str__(self),
            DefiningValues=self.DefiningValues,
            DefinedValues=self.DefinedValues,
            Expression=self.Expression,
            DefiningUnit=self.DefiningUnit,
            DefinedUnit=self.DefinedUnit,
            CurveInterpolation=self.CurveInterpolation,
        )

    def __json__(self):
        sup = IfcSimpleProperty.__json__(self)
        attrs = {'DefiningValues': self.DefiningValues, 'DefinedValues': self.DefinedValues,
                 'Expression': self.Expression, 'DefiningUnit': self.DefiningUnit, 'DefinedUnit': self.DefinedUnit,
                 'CurveInterpolation': self.CurveInterpolation}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcPropertyTemplate(IfcPropertyTemplateDefinition):
    def __init__(self, rtype, args):
        IfcPropertyTemplateDefinition.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcPropertyTemplateDefinition.__str__(self),
        )

    def __json__(self):
        sup = IfcPropertyTemplateDefinition.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcProxy(IfcProduct):
    def __init__(self, rtype, args):
        IfcProduct.__init__(self, rtype, args)
        self.ProxyType = args.pop()
        self.Tag = args.pop()

    def __str__(self):
        return "{sup}:ProxyType:{ProxyType}:Tag:{Tag}".format(
            sup=IfcProduct.__str__(self),
            ProxyType=self.ProxyType,
            Tag=self.Tag,
        )

    def __json__(self):
        sup = IfcProduct.__json__(self)
        attrs = {'ProxyType': self.ProxyType, 'Tag': self.Tag}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRectangleHollowProfileDef(IfcRectangleProfileDef):
    def __init__(self, rtype, args):
        IfcRectangleProfileDef.__init__(self, rtype, args)
        self.WallThickness = args.pop()
        self.InnerFilletRadius = args.pop()
        self.OuterFilletRadius = args.pop()

    def __str__(self):
        return "{sup}:WallThickness:{WallThickness}:InnerFilletRadius:{InnerFilletRadius}:OuterFilletRadius:{OuterFilletRadius}".format(
            sup=IfcRectangleProfileDef.__str__(self),
            WallThickness=self.WallThickness,
            InnerFilletRadius=self.InnerFilletRadius,
            OuterFilletRadius=self.OuterFilletRadius,
        )

    def __json__(self):
        sup = IfcRectangleProfileDef.__json__(self)
        attrs = {'WallThickness': self.WallThickness, 'InnerFilletRadius': self.InnerFilletRadius,
                 'OuterFilletRadius': self.OuterFilletRadius}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRectangularPyramid(IfcCsgPrimitive3D):
    def __init__(self, rtype, args):
        IfcCsgPrimitive3D.__init__(self, rtype, args)
        self.XLength = args.pop()
        self.YLength = args.pop()
        self.Height = args.pop()

    def __str__(self):
        return "{sup}:XLength:{XLength}:YLength:{YLength}:Height:{Height}".format(
            sup=IfcCsgPrimitive3D.__str__(self),
            XLength=self.XLength,
            YLength=self.YLength,
            Height=self.Height,
        )

    def __json__(self):
        sup = IfcCsgPrimitive3D.__json__(self)
        attrs = {'XLength': self.XLength, 'YLength': self.YLength, 'Height': self.Height}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRectangularTrimmedSurface(IfcBoundedSurface):
    def __init__(self, rtype, args):
        IfcBoundedSurface.__init__(self, rtype, args)
        self.BasisSurface = args.pop()
        self.U1 = args.pop()
        self.V1 = args.pop()
        self.U2 = args.pop()
        self.V2 = args.pop()
        self.Usense = args.pop()
        self.Vsense = args.pop()

    def __str__(self):
        return "{sup}:BasisSurface:{BasisSurface}:U1:{U1}:V1:{V1}:U2:{U2}:V2:{V2}:Usense:{Usense}:Vsense:{Vsense}".format(
            sup=IfcBoundedSurface.__str__(self),
            BasisSurface=self.BasisSurface,
            U1=self.U1,
            V1=self.V1,
            U2=self.U2,
            V2=self.V2,
            Usense=self.Usense,
            Vsense=self.Vsense,
        )

    def __json__(self):
        sup = IfcBoundedSurface.__json__(self)
        attrs = {'BasisSurface': self.BasisSurface, 'U1': self.U1, 'V1': self.V1, 'U2': self.U2, 'V2': self.V2,
                 'Usense': self.Usense, 'Vsense': self.Vsense}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcReinforcementDefinitionProperties(IfcPreDefinedPropertySet):
    def __init__(self, rtype, args):
        IfcPreDefinedPropertySet.__init__(self, rtype, args)
        self.DefinitionType = args.pop()
        self.ReinforcementSectionDefinitions = args.pop()

    def __str__(self):
        return "{sup}:DefinitionType:{DefinitionType}:ReinforcementSectionDefinitions:{ReinforcementSectionDefinitions}".format(
            sup=IfcPreDefinedPropertySet.__str__(self),
            DefinitionType=self.DefinitionType,
            ReinforcementSectionDefinitions=self.ReinforcementSectionDefinitions,
        )

    def __json__(self):
        sup = IfcPreDefinedPropertySet.__json__(self)
        attrs = {'DefinitionType': self.DefinitionType,
                 'ReinforcementSectionDefinitions': self.ReinforcementSectionDefinitions}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcRelAssigns(IfcRelationship):
    def __init__(self, rtype, args):
        IfcRelationship.__init__(self, rtype, args)
        self.RelatedObjects = args.pop()
        self.RelatedObjectsType = args.pop()

    def __str__(self):
        return "{sup}:RelatedObjects:{RelatedObjects}:RelatedObjectsType:{RelatedObjectsType}".format(
            sup=IfcRelationship.__str__(self),
            RelatedObjects=self.RelatedObjects,
            RelatedObjectsType=self.RelatedObjectsType,
        )

    def __json__(self):
        sup = IfcRelationship.__json__(self)
        attrs = {'RelatedObjects': self.RelatedObjects, 'RelatedObjectsType': self.RelatedObjectsType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelAssignsToActor(IfcRelAssigns):
    def __init__(self, rtype, args):
        IfcRelAssigns.__init__(self, rtype, args)
        self.RelatingActor = args.pop()
        self.ActingRole = args.pop()

    def __str__(self):
        return "{sup}:RelatingActor:{RelatingActor}:ActingRole:{ActingRole}".format(
            sup=IfcRelAssigns.__str__(self),
            RelatingActor=self.RelatingActor,
            ActingRole=self.ActingRole,
        )

    def __json__(self):
        sup = IfcRelAssigns.__json__(self)
        attrs = {'RelatingActor': self.RelatingActor, 'ActingRole': self.ActingRole}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelAssignsToControl(IfcRelAssigns):
    def __init__(self, rtype, args):
        IfcRelAssigns.__init__(self, rtype, args)
        self.RelatingControl = args.pop()

    def __str__(self):
        return "{sup}:RelatingControl:{RelatingControl}".format(
            sup=IfcRelAssigns.__str__(self),
            RelatingControl=self.RelatingControl,
        )

    def __json__(self):
        sup = IfcRelAssigns.__json__(self)
        attrs = {'RelatingControl': self.RelatingControl}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelAssignsToGroup(IfcRelAssigns):
    def __init__(self, rtype, args):
        IfcRelAssigns.__init__(self, rtype, args)
        self.RelatingGroup = args.pop()

    def __str__(self):
        return "{sup}:RelatingGroup:{RelatingGroup}".format(
            sup=IfcRelAssigns.__str__(self),
            RelatingGroup=self.RelatingGroup,
        )

    def __json__(self):
        sup = IfcRelAssigns.__json__(self)
        attrs = {'RelatingGroup': self.RelatingGroup}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelAssignsToGroupByFactor(IfcRelAssignsToGroup):
    def __init__(self, rtype, args):
        IfcRelAssignsToGroup.__init__(self, rtype, args)
        self.Factor = args.pop()

    def __str__(self):
        return "{sup}:Factor:{Factor}".format(
            sup=IfcRelAssignsToGroup.__str__(self),
            Factor=self.Factor,
        )

    def __json__(self):
        sup = IfcRelAssignsToGroup.__json__(self)
        attrs = {'Factor': self.Factor}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelAssignsToProcess(IfcRelAssigns):
    def __init__(self, rtype, args):
        IfcRelAssigns.__init__(self, rtype, args)
        self.RelatingProcess = args.pop()
        self.QuantityInProcess = args.pop()

    def __str__(self):
        return "{sup}:RelatingProcess:{RelatingProcess}:QuantityInProcess:{QuantityInProcess}".format(
            sup=IfcRelAssigns.__str__(self),
            RelatingProcess=self.RelatingProcess,
            QuantityInProcess=self.QuantityInProcess,
        )

    def __json__(self):
        sup = IfcRelAssigns.__json__(self)
        attrs = {'RelatingProcess': self.RelatingProcess, 'QuantityInProcess': self.QuantityInProcess}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelAssignsToProduct(IfcRelAssigns):
    def __init__(self, rtype, args):
        IfcRelAssigns.__init__(self, rtype, args)
        self.RelatingProduct = args.pop()

    def __str__(self):
        return "{sup}:RelatingProduct:{RelatingProduct}".format(
            sup=IfcRelAssigns.__str__(self),
            RelatingProduct=self.RelatingProduct,
        )

    def __json__(self):
        sup = IfcRelAssigns.__json__(self)
        attrs = {'RelatingProduct': self.RelatingProduct}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelAssignsToResource(IfcRelAssigns):
    def __init__(self, rtype, args):
        IfcRelAssigns.__init__(self, rtype, args)
        self.RelatingResource = args.pop()

    def __str__(self):
        return "{sup}:RelatingResource:{RelatingResource}".format(
            sup=IfcRelAssigns.__str__(self),
            RelatingResource=self.RelatingResource,
        )

    def __json__(self):
        sup = IfcRelAssigns.__json__(self)
        attrs = {'RelatingResource': self.RelatingResource}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcRelAssociates(IfcRelationship):
    def __init__(self, rtype, args):
        IfcRelationship.__init__(self, rtype, args)
        self.RelatedObjects = args.pop()

    def __str__(self):
        return "{sup}:RelatedObjects:{RelatedObjects}".format(
            sup=IfcRelationship.__str__(self),
            RelatedObjects=self.RelatedObjects,
        )

    def __json__(self):
        sup = IfcRelationship.__json__(self)
        attrs = {'RelatedObjects': self.RelatedObjects}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelAssociatesApproval(IfcRelAssociates):
    def __init__(self, rtype, args):
        IfcRelAssociates.__init__(self, rtype, args)
        self.RelatingApproval = args.pop()

    def __str__(self):
        return "{sup}:RelatingApproval:{RelatingApproval}".format(
            sup=IfcRelAssociates.__str__(self),
            RelatingApproval=self.RelatingApproval,
        )

    def __json__(self):
        sup = IfcRelAssociates.__json__(self)
        attrs = {'RelatingApproval': self.RelatingApproval}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelAssociatesClassification(IfcRelAssociates):
    def __init__(self, rtype, args):
        IfcRelAssociates.__init__(self, rtype, args)
        self.RelatingClassification = args.pop()

    def __str__(self):
        return "{sup}:RelatingClassification:{RelatingClassification}".format(
            sup=IfcRelAssociates.__str__(self),
            RelatingClassification=self.RelatingClassification,
        )

    def __json__(self):
        sup = IfcRelAssociates.__json__(self)
        attrs = {'RelatingClassification': self.RelatingClassification}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelAssociatesConstraint(IfcRelAssociates):
    def __init__(self, rtype, args):
        IfcRelAssociates.__init__(self, rtype, args)
        self.Intent = args.pop()
        self.RelatingConstraint = args.pop()

    def __str__(self):
        return "{sup}:Intent:{Intent}:RelatingConstraint:{RelatingConstraint}".format(
            sup=IfcRelAssociates.__str__(self),
            Intent=self.Intent,
            RelatingConstraint=self.RelatingConstraint,
        )

    def __json__(self):
        sup = IfcRelAssociates.__json__(self)
        attrs = {'Intent': self.Intent, 'RelatingConstraint': self.RelatingConstraint}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelAssociatesDocument(IfcRelAssociates):
    def __init__(self, rtype, args):
        IfcRelAssociates.__init__(self, rtype, args)
        self.RelatingDocument = args.pop()

    def __str__(self):
        return "{sup}:RelatingDocument:{RelatingDocument}".format(
            sup=IfcRelAssociates.__str__(self),
            RelatingDocument=self.RelatingDocument,
        )

    def __json__(self):
        sup = IfcRelAssociates.__json__(self)
        attrs = {'RelatingDocument': self.RelatingDocument}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelAssociatesLibrary(IfcRelAssociates):
    def __init__(self, rtype, args):
        IfcRelAssociates.__init__(self, rtype, args)
        self.RelatingLibrary = args.pop()

    def __str__(self):
        return "{sup}:RelatingLibrary:{RelatingLibrary}".format(
            sup=IfcRelAssociates.__str__(self),
            RelatingLibrary=self.RelatingLibrary,
        )

    def __json__(self):
        sup = IfcRelAssociates.__json__(self)
        attrs = {'RelatingLibrary': self.RelatingLibrary}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelAssociatesMaterial(IfcRelAssociates):
    def __init__(self, rtype, args):
        IfcRelAssociates.__init__(self, rtype, args)
        self.RelatingMaterial = args.pop()

    def __str__(self):
        return "{sup}:RelatingMaterial:{RelatingMaterial}".format(
            sup=IfcRelAssociates.__str__(self),
            RelatingMaterial=self.RelatingMaterial,
        )

    def __json__(self):
        sup = IfcRelAssociates.__json__(self)
        attrs = {'RelatingMaterial': self.RelatingMaterial}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcRelConnects(IfcRelationship):
    def __init__(self, rtype, args):
        IfcRelationship.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcRelationship.__str__(self),
        )

    def __json__(self):
        sup = IfcRelationship.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelConnectsElements(IfcRelConnects):
    def __init__(self, rtype, args):
        IfcRelConnects.__init__(self, rtype, args)
        self.ConnectionGeometry = args.pop()
        self.RelatingElement = args.pop()
        self.RelatedElement = args.pop()

    def __str__(self):
        return "{sup}:ConnectionGeometry:{ConnectionGeometry}:RelatingElement:{RelatingElement}:RelatedElement:{RelatedElement}".format(
            sup=IfcRelConnects.__str__(self),
            ConnectionGeometry=self.ConnectionGeometry,
            RelatingElement=self.RelatingElement,
            RelatedElement=self.RelatedElement,
        )

    def __json__(self):
        sup = IfcRelConnects.__json__(self)
        attrs = {'ConnectionGeometry': self.ConnectionGeometry, 'RelatingElement': self.RelatingElement,
                 'RelatedElement': self.RelatedElement}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelConnectsPathElements(IfcRelConnectsElements):
    def __init__(self, rtype, args):
        IfcRelConnectsElements.__init__(self, rtype, args)
        self.RelatingPriorities = args.pop()
        self.RelatedPriorities = args.pop()
        self.RelatedConnectionType = args.pop()
        self.RelatingConnectionType = args.pop()

    def __str__(self):
        return "{sup}:RelatingPriorities:{RelatingPriorities}:RelatedPriorities:{RelatedPriorities}:RelatedConnectionType:{RelatedConnectionType}:RelatingConnectionType:{RelatingConnectionType}".format(
            sup=IfcRelConnectsElements.__str__(self),
            RelatingPriorities=self.RelatingPriorities,
            RelatedPriorities=self.RelatedPriorities,
            RelatedConnectionType=self.RelatedConnectionType,
            RelatingConnectionType=self.RelatingConnectionType,
        )

    def __json__(self):
        sup = IfcRelConnectsElements.__json__(self)
        attrs = {'RelatingPriorities': self.RelatingPriorities, 'RelatedPriorities': self.RelatedPriorities,
                 'RelatedConnectionType': self.RelatedConnectionType,
                 'RelatingConnectionType': self.RelatingConnectionType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelConnectsPortToElement(IfcRelConnects):
    def __init__(self, rtype, args):
        IfcRelConnects.__init__(self, rtype, args)
        self.RelatingPort = args.pop()
        self.RelatedElement = args.pop()

    def __str__(self):
        return "{sup}:RelatingPort:{RelatingPort}:RelatedElement:{RelatedElement}".format(
            sup=IfcRelConnects.__str__(self),
            RelatingPort=self.RelatingPort,
            RelatedElement=self.RelatedElement,
        )

    def __json__(self):
        sup = IfcRelConnects.__json__(self)
        attrs = {'RelatingPort': self.RelatingPort, 'RelatedElement': self.RelatedElement}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelConnectsPorts(IfcRelConnects):
    def __init__(self, rtype, args):
        IfcRelConnects.__init__(self, rtype, args)
        self.RelatingPort = args.pop()
        self.RelatedPort = args.pop()
        self.RealizingElement = args.pop()

    def __str__(self):
        return "{sup}:RelatingPort:{RelatingPort}:RelatedPort:{RelatedPort}:RealizingElement:{RealizingElement}".format(
            sup=IfcRelConnects.__str__(self),
            RelatingPort=self.RelatingPort,
            RelatedPort=self.RelatedPort,
            RealizingElement=self.RealizingElement,
        )

    def __json__(self):
        sup = IfcRelConnects.__json__(self)
        attrs = {'RelatingPort': self.RelatingPort, 'RelatedPort': self.RelatedPort,
                 'RealizingElement': self.RealizingElement}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelConnectsStructuralActivity(IfcRelConnects):
    def __init__(self, rtype, args):
        IfcRelConnects.__init__(self, rtype, args)
        self.RelatingElement = args.pop()
        self.RelatedStructuralActivity = args.pop()

    def __str__(self):
        return "{sup}:RelatingElement:{RelatingElement}:RelatedStructuralActivity:{RelatedStructuralActivity}".format(
            sup=IfcRelConnects.__str__(self),
            RelatingElement=self.RelatingElement,
            RelatedStructuralActivity=self.RelatedStructuralActivity,
        )

    def __json__(self):
        sup = IfcRelConnects.__json__(self)
        attrs = {'RelatingElement': self.RelatingElement, 'RelatedStructuralActivity': self.RelatedStructuralActivity}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelConnectsStructuralMember(IfcRelConnects):
    def __init__(self, rtype, args):
        IfcRelConnects.__init__(self, rtype, args)
        self.RelatingStructuralMember = args.pop()
        self.RelatedStructuralConnection = args.pop()
        self.AppliedCondition = args.pop()
        self.AdditionalConditions = args.pop()
        self.SupportedLength = args.pop()
        self.ConditionCoordinateSystem = args.pop()

    def __str__(self):
        return "{sup}:RelatingStructuralMember:{RelatingStructuralMember}:RelatedStructuralConnection:{RelatedStructuralConnection}:AppliedCondition:{AppliedCondition}:AdditionalConditions:{AdditionalConditions}:SupportedLength:{SupportedLength}:ConditionCoordinateSystem:{ConditionCoordinateSystem}".format(
            sup=IfcRelConnects.__str__(self),
            RelatingStructuralMember=self.RelatingStructuralMember,
            RelatedStructuralConnection=self.RelatedStructuralConnection,
            AppliedCondition=self.AppliedCondition,
            AdditionalConditions=self.AdditionalConditions,
            SupportedLength=self.SupportedLength,
            ConditionCoordinateSystem=self.ConditionCoordinateSystem,
        )

    def __json__(self):
        sup = IfcRelConnects.__json__(self)
        attrs = {'RelatingStructuralMember': self.RelatingStructuralMember,
                 'RelatedStructuralConnection': self.RelatedStructuralConnection,
                 'AppliedCondition': self.AppliedCondition, 'AdditionalConditions': self.AdditionalConditions,
                 'SupportedLength': self.SupportedLength, 'ConditionCoordinateSystem': self.ConditionCoordinateSystem}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelConnectsWithEccentricity(IfcRelConnectsStructuralMember):
    def __init__(self, rtype, args):
        IfcRelConnectsStructuralMember.__init__(self, rtype, args)
        self.ConnectionConstraint = args.pop()

    def __str__(self):
        return "{sup}:ConnectionConstraint:{ConnectionConstraint}".format(
            sup=IfcRelConnectsStructuralMember.__str__(self),
            ConnectionConstraint=self.ConnectionConstraint,
        )

    def __json__(self):
        sup = IfcRelConnectsStructuralMember.__json__(self)
        attrs = {'ConnectionConstraint': self.ConnectionConstraint}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelConnectsWithRealizingElements(IfcRelConnectsElements):
    def __init__(self, rtype, args):
        IfcRelConnectsElements.__init__(self, rtype, args)
        self.RealizingElements = args.pop()
        self.ConnectionType = args.pop()

    def __str__(self):
        return "{sup}:RealizingElements:{RealizingElements}:ConnectionType:{ConnectionType}".format(
            sup=IfcRelConnectsElements.__str__(self),
            RealizingElements=self.RealizingElements,
            ConnectionType=self.ConnectionType,
        )

    def __json__(self):
        sup = IfcRelConnectsElements.__json__(self)
        attrs = {'RealizingElements': self.RealizingElements, 'ConnectionType': self.ConnectionType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelContainedInSpatialStructure(IfcRelConnects):
    def __init__(self, rtype, args):
        IfcRelConnects.__init__(self, rtype, args)
        self.RelatedElements = args.pop()
        self.RelatingStructure = args.pop()

    def __str__(self):
        return "{sup}:RelatedElements:{RelatedElements}:RelatingStructure:{RelatingStructure}".format(
            sup=IfcRelConnects.__str__(self),
            RelatedElements=self.RelatedElements,
            RelatingStructure=self.RelatingStructure,
        )

    def __json__(self):
        sup = IfcRelConnects.__json__(self)
        attrs = {'RelatedElements': self.RelatedElements, 'RelatingStructure': self.RelatingStructure}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelCoversBldgElements(IfcRelConnects):
    def __init__(self, rtype, args):
        IfcRelConnects.__init__(self, rtype, args)
        self.RelatingBuildingElement = args.pop()
        self.RelatedCoverings = args.pop()

    def __str__(self):
        return "{sup}:RelatingBuildingElement:{RelatingBuildingElement}:RelatedCoverings:{RelatedCoverings}".format(
            sup=IfcRelConnects.__str__(self),
            RelatingBuildingElement=self.RelatingBuildingElement,
            RelatedCoverings=self.RelatedCoverings,
        )

    def __json__(self):
        sup = IfcRelConnects.__json__(self)
        attrs = {'RelatingBuildingElement': self.RelatingBuildingElement, 'RelatedCoverings': self.RelatedCoverings}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelCoversSpaces(IfcRelConnects):
    def __init__(self, rtype, args):
        IfcRelConnects.__init__(self, rtype, args)
        self.RelatingSpace = args.pop()
        self.RelatedCoverings = args.pop()

    def __str__(self):
        return "{sup}:RelatingSpace:{RelatingSpace}:RelatedCoverings:{RelatedCoverings}".format(
            sup=IfcRelConnects.__str__(self),
            RelatingSpace=self.RelatingSpace,
            RelatedCoverings=self.RelatedCoverings,
        )

    def __json__(self):
        sup = IfcRelConnects.__json__(self)
        attrs = {'RelatingSpace': self.RelatingSpace, 'RelatedCoverings': self.RelatedCoverings}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelDeclares(IfcRelationship):
    def __init__(self, rtype, args):
        IfcRelationship.__init__(self, rtype, args)
        self.RelatingContext = args.pop()
        self.RelatedDefinitions = args.pop()

    def __str__(self):
        return "{sup}:RelatingContext:{RelatingContext}:RelatedDefinitions:{RelatedDefinitions}".format(
            sup=IfcRelationship.__str__(self),
            RelatingContext=self.RelatingContext,
            RelatedDefinitions=self.RelatedDefinitions,
        )

    def __json__(self):
        sup = IfcRelationship.__json__(self)
        attrs = {'RelatingContext': self.RelatingContext, 'RelatedDefinitions': self.RelatedDefinitions}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcRelDecomposes(IfcRelationship):
    def __init__(self, rtype, args):
        IfcRelationship.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcRelationship.__str__(self),
        )

    def __json__(self):
        sup = IfcRelationship.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcRelDefines(IfcRelationship):
    def __init__(self, rtype, args):
        IfcRelationship.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcRelationship.__str__(self),
        )

    def __json__(self):
        sup = IfcRelationship.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelDefinesByObject(IfcRelDefines):
    def __init__(self, rtype, args):
        IfcRelDefines.__init__(self, rtype, args)
        self.RelatedObjects = args.pop()
        self.RelatingObject = args.pop()

    def __str__(self):
        return "{sup}:RelatedObjects:{RelatedObjects}:RelatingObject:{RelatingObject}".format(
            sup=IfcRelDefines.__str__(self),
            RelatedObjects=self.RelatedObjects,
            RelatingObject=self.RelatingObject,
        )

    def __json__(self):
        sup = IfcRelDefines.__json__(self)
        attrs = {'RelatedObjects': self.RelatedObjects, 'RelatingObject': self.RelatingObject}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelDefinesByProperties(IfcRelDefines):
    def __init__(self, rtype, args):
        IfcRelDefines.__init__(self, rtype, args)
        self.RelatedObjects = args.pop()
        self.RelatingPropertyDefinition = args.pop()

    def __str__(self):
        return "{sup}:RelatedObjects:{RelatedObjects}:RelatingPropertyDefinition:{RelatingPropertyDefinition}".format(
            sup=IfcRelDefines.__str__(self),
            RelatedObjects=self.RelatedObjects,
            RelatingPropertyDefinition=self.RelatingPropertyDefinition,
        )

    def __json__(self):
        sup = IfcRelDefines.__json__(self)
        attrs = {'RelatedObjects': self.RelatedObjects, 'RelatingPropertyDefinition': self.RelatingPropertyDefinition}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelDefinesByTemplate(IfcRelDefines):
    def __init__(self, rtype, args):
        IfcRelDefines.__init__(self, rtype, args)
        self.RelatedPropertySets = args.pop()
        self.RelatingTemplate = args.pop()

    def __str__(self):
        return "{sup}:RelatedPropertySets:{RelatedPropertySets}:RelatingTemplate:{RelatingTemplate}".format(
            sup=IfcRelDefines.__str__(self),
            RelatedPropertySets=self.RelatedPropertySets,
            RelatingTemplate=self.RelatingTemplate,
        )

    def __json__(self):
        sup = IfcRelDefines.__json__(self)
        attrs = {'RelatedPropertySets': self.RelatedPropertySets, 'RelatingTemplate': self.RelatingTemplate}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelDefinesByType(IfcRelDefines):
    def __init__(self, rtype, args):
        IfcRelDefines.__init__(self, rtype, args)
        self.RelatedObjects = args.pop()
        self.RelatingType = args.pop()

    def __str__(self):
        return "{sup}:RelatedObjects:{RelatedObjects}:RelatingType:{RelatingType}".format(
            sup=IfcRelDefines.__str__(self),
            RelatedObjects=self.RelatedObjects,
            RelatingType=self.RelatingType,
        )

    def __json__(self):
        sup = IfcRelDefines.__json__(self)
        attrs = {'RelatedObjects': self.RelatedObjects, 'RelatingType': self.RelatingType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelFillsElement(IfcRelConnects):
    def __init__(self, rtype, args):
        IfcRelConnects.__init__(self, rtype, args)
        self.RelatingOpeningElement = args.pop()
        self.RelatedBuildingElement = args.pop()

    def __str__(self):
        return "{sup}:RelatingOpeningElement:{RelatingOpeningElement}:RelatedBuildingElement:{RelatedBuildingElement}".format(
            sup=IfcRelConnects.__str__(self),
            RelatingOpeningElement=self.RelatingOpeningElement,
            RelatedBuildingElement=self.RelatedBuildingElement,
        )

    def __json__(self):
        sup = IfcRelConnects.__json__(self)
        attrs = {'RelatingOpeningElement': self.RelatingOpeningElement,
                 'RelatedBuildingElement': self.RelatedBuildingElement}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelFlowControlElements(IfcRelConnects):
    def __init__(self, rtype, args):
        IfcRelConnects.__init__(self, rtype, args)
        self.RelatedControlElements = args.pop()
        self.RelatingFlowElement = args.pop()

    def __str__(self):
        return "{sup}:RelatedControlElements:{RelatedControlElements}:RelatingFlowElement:{RelatingFlowElement}".format(
            sup=IfcRelConnects.__str__(self),
            RelatedControlElements=self.RelatedControlElements,
            RelatingFlowElement=self.RelatingFlowElement,
        )

    def __json__(self):
        sup = IfcRelConnects.__json__(self)
        attrs = {'RelatedControlElements': self.RelatedControlElements, 'RelatingFlowElement': self.RelatingFlowElement}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelInterferesElements(IfcRelConnects):
    def __init__(self, rtype, args):
        IfcRelConnects.__init__(self, rtype, args)
        self.RelatingElement = args.pop()
        self.RelatedElement = args.pop()
        self.InterferenceGeometry = args.pop()
        self.InterferenceType = args.pop()
        self.ImpliedOrder = args.pop()

    def __str__(self):
        return "{sup}:RelatingElement:{RelatingElement}:RelatedElement:{RelatedElement}:InterferenceGeometry:{InterferenceGeometry}:InterferenceType:{InterferenceType}:ImpliedOrder:{ImpliedOrder}".format(
            sup=IfcRelConnects.__str__(self),
            RelatingElement=self.RelatingElement,
            RelatedElement=self.RelatedElement,
            InterferenceGeometry=self.InterferenceGeometry,
            InterferenceType=self.InterferenceType,
            ImpliedOrder=self.ImpliedOrder,
        )

    def __json__(self):
        sup = IfcRelConnects.__json__(self)
        attrs = {'RelatingElement': self.RelatingElement, 'RelatedElement': self.RelatedElement,
                 'InterferenceGeometry': self.InterferenceGeometry, 'InterferenceType': self.InterferenceType,
                 'ImpliedOrder': self.ImpliedOrder}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelNests(IfcRelDecomposes):
    def __init__(self, rtype, args):
        IfcRelDecomposes.__init__(self, rtype, args)
        self.RelatingObject = args.pop()
        self.RelatedObjects = args.pop()

    def __str__(self):
        return "{sup}:RelatingObject:{RelatingObject}:RelatedObjects:{RelatedObjects}".format(
            sup=IfcRelDecomposes.__str__(self),
            RelatingObject=self.RelatingObject,
            RelatedObjects=self.RelatedObjects,
        )

    def __json__(self):
        sup = IfcRelDecomposes.__json__(self)
        attrs = {'RelatingObject': self.RelatingObject, 'RelatedObjects': self.RelatedObjects}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelProjectsElement(IfcRelDecomposes):
    def __init__(self, rtype, args):
        IfcRelDecomposes.__init__(self, rtype, args)
        self.RelatingElement = args.pop()
        self.RelatedFeatureElement = args.pop()

    def __str__(self):
        return "{sup}:RelatingElement:{RelatingElement}:RelatedFeatureElement:{RelatedFeatureElement}".format(
            sup=IfcRelDecomposes.__str__(self),
            RelatingElement=self.RelatingElement,
            RelatedFeatureElement=self.RelatedFeatureElement,
        )

    def __json__(self):
        sup = IfcRelDecomposes.__json__(self)
        attrs = {'RelatingElement': self.RelatingElement, 'RelatedFeatureElement': self.RelatedFeatureElement}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelReferencedInSpatialStructure(IfcRelConnects):
    def __init__(self, rtype, args):
        IfcRelConnects.__init__(self, rtype, args)
        self.RelatedElements = args.pop()
        self.RelatingStructure = args.pop()

    def __str__(self):
        return "{sup}:RelatedElements:{RelatedElements}:RelatingStructure:{RelatingStructure}".format(
            sup=IfcRelConnects.__str__(self),
            RelatedElements=self.RelatedElements,
            RelatingStructure=self.RelatingStructure,
        )

    def __json__(self):
        sup = IfcRelConnects.__json__(self)
        attrs = {'RelatedElements': self.RelatedElements, 'RelatingStructure': self.RelatingStructure}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelSequence(IfcRelConnects):
    def __init__(self, rtype, args):
        IfcRelConnects.__init__(self, rtype, args)
        self.RelatingProcess = args.pop()
        self.RelatedProcess = args.pop()
        self.TimeLag = args.pop()
        self.SequenceType = args.pop()
        self.UserDefinedSequenceType = args.pop()

    def __str__(self):
        return "{sup}:RelatingProcess:{RelatingProcess}:RelatedProcess:{RelatedProcess}:TimeLag:{TimeLag}:SequenceType:{SequenceType}:UserDefinedSequenceType:{UserDefinedSequenceType}".format(
            sup=IfcRelConnects.__str__(self),
            RelatingProcess=self.RelatingProcess,
            RelatedProcess=self.RelatedProcess,
            TimeLag=self.TimeLag,
            SequenceType=self.SequenceType,
            UserDefinedSequenceType=self.UserDefinedSequenceType,
        )

    def __json__(self):
        sup = IfcRelConnects.__json__(self)
        attrs = {'RelatingProcess': self.RelatingProcess, 'RelatedProcess': self.RelatedProcess,
                 'TimeLag': self.TimeLag, 'SequenceType': self.SequenceType,
                 'UserDefinedSequenceType': self.UserDefinedSequenceType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelServicesBuildings(IfcRelConnects):
    def __init__(self, rtype, args):
        IfcRelConnects.__init__(self, rtype, args)
        self.RelatingSystem = args.pop()
        self.RelatedBuildings = args.pop()

    def __str__(self):
        return "{sup}:RelatingSystem:{RelatingSystem}:RelatedBuildings:{RelatedBuildings}".format(
            sup=IfcRelConnects.__str__(self),
            RelatingSystem=self.RelatingSystem,
            RelatedBuildings=self.RelatedBuildings,
        )

    def __json__(self):
        sup = IfcRelConnects.__json__(self)
        attrs = {'RelatingSystem': self.RelatingSystem, 'RelatedBuildings': self.RelatedBuildings}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelSpaceBoundary(IfcRelConnects):
    def __init__(self, rtype, args):
        IfcRelConnects.__init__(self, rtype, args)
        self.RelatingSpace = args.pop()
        self.RelatedBuildingElement = args.pop()
        self.ConnectionGeometry = args.pop()
        self.PhysicalOrVirtualBoundary = args.pop()
        self.InternalOrExternalBoundary = args.pop()

    def __str__(self):
        return "{sup}:RelatingSpace:{RelatingSpace}:RelatedBuildingElement:{RelatedBuildingElement}:ConnectionGeometry:{ConnectionGeometry}:PhysicalOrVirtualBoundary:{PhysicalOrVirtualBoundary}:InternalOrExternalBoundary:{InternalOrExternalBoundary}".format(
            sup=IfcRelConnects.__str__(self),
            RelatingSpace=self.RelatingSpace,
            RelatedBuildingElement=self.RelatedBuildingElement,
            ConnectionGeometry=self.ConnectionGeometry,
            PhysicalOrVirtualBoundary=self.PhysicalOrVirtualBoundary,
            InternalOrExternalBoundary=self.InternalOrExternalBoundary,
        )

    def __json__(self):
        sup = IfcRelConnects.__json__(self)
        attrs = {'RelatingSpace': self.RelatingSpace, 'RelatedBuildingElement': self.RelatedBuildingElement,
                 'ConnectionGeometry': self.ConnectionGeometry,
                 'PhysicalOrVirtualBoundary': self.PhysicalOrVirtualBoundary,
                 'InternalOrExternalBoundary': self.InternalOrExternalBoundary}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelSpaceBoundary1stLevel(IfcRelSpaceBoundary):
    def __init__(self, rtype, args):
        IfcRelSpaceBoundary.__init__(self, rtype, args)
        self.ParentBoundary = args.pop()

    def __str__(self):
        return "{sup}:ParentBoundary:{ParentBoundary}".format(
            sup=IfcRelSpaceBoundary.__str__(self),
            ParentBoundary=self.ParentBoundary,
        )

    def __json__(self):
        sup = IfcRelSpaceBoundary.__json__(self)
        attrs = {'ParentBoundary': self.ParentBoundary}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelSpaceBoundary2ndLevel(IfcRelSpaceBoundary1stLevel):
    def __init__(self, rtype, args):
        IfcRelSpaceBoundary1stLevel.__init__(self, rtype, args)
        self.CorrespondingBoundary = args.pop()

    def __str__(self):
        return "{sup}:CorrespondingBoundary:{CorrespondingBoundary}".format(
            sup=IfcRelSpaceBoundary1stLevel.__str__(self),
            CorrespondingBoundary=self.CorrespondingBoundary,
        )

    def __json__(self):
        sup = IfcRelSpaceBoundary1stLevel.__json__(self)
        attrs = {'CorrespondingBoundary': self.CorrespondingBoundary}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelVoidsElement(IfcRelDecomposes):
    def __init__(self, rtype, args):
        IfcRelDecomposes.__init__(self, rtype, args)
        self.RelatingBuildingElement = args.pop()
        self.RelatedOpeningElement = args.pop()

    def __str__(self):
        return "{sup}:RelatingBuildingElement:{RelatingBuildingElement}:RelatedOpeningElement:{RelatedOpeningElement}".format(
            sup=IfcRelDecomposes.__str__(self),
            RelatingBuildingElement=self.RelatingBuildingElement,
            RelatedOpeningElement=self.RelatedOpeningElement,
        )

    def __json__(self):
        sup = IfcRelDecomposes.__json__(self)
        attrs = {'RelatingBuildingElement': self.RelatingBuildingElement,
                 'RelatedOpeningElement': self.RelatedOpeningElement}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcReparametrisedCompositeCurveSegment(IfcCompositeCurveSegment):
    def __init__(self, rtype, args):
        IfcCompositeCurveSegment.__init__(self, rtype, args)
        self.ParamLength = args.pop()

    def __str__(self):
        return "{sup}:ParamLength:{ParamLength}".format(
            sup=IfcCompositeCurveSegment.__str__(self),
            ParamLength=self.ParamLength,
        )

    def __json__(self):
        sup = IfcCompositeCurveSegment.__json__(self)
        attrs = {'ParamLength': self.ParamLength}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcResource(IfcObject):
    def __init__(self, rtype, args):
        IfcObject.__init__(self, rtype, args)
        self.Identification = args.pop()
        self.LongDescription = args.pop()

    def __str__(self):
        return "{sup}:Identification:{Identification}:LongDescription:{LongDescription}".format(
            sup=IfcObject.__str__(self),
            Identification=self.Identification,
            LongDescription=self.LongDescription,
        )

    def __json__(self):
        sup = IfcObject.__json__(self)
        attrs = {'Identification': self.Identification, 'LongDescription': self.LongDescription}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRevolvedAreaSolid(IfcSweptAreaSolid):
    def __init__(self, rtype, args):
        IfcSweptAreaSolid.__init__(self, rtype, args)
        self.Axis = args.pop()
        self.Angle = args.pop()

    def __str__(self):
        return "{sup}:Axis:{Axis}:Angle:{Angle}".format(
            sup=IfcSweptAreaSolid.__str__(self),
            Axis=self.Axis,
            Angle=self.Angle,
        )

    def __json__(self):
        sup = IfcSweptAreaSolid.__json__(self)
        attrs = {'Axis': self.Axis, 'Angle': self.Angle}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRevolvedAreaSolidTapered(IfcRevolvedAreaSolid):
    def __init__(self, rtype, args):
        IfcRevolvedAreaSolid.__init__(self, rtype, args)
        self.EndSweptArea = args.pop()

    def __str__(self):
        return "{sup}:EndSweptArea:{EndSweptArea}".format(
            sup=IfcRevolvedAreaSolid.__str__(self),
            EndSweptArea=self.EndSweptArea,
        )

    def __json__(self):
        sup = IfcRevolvedAreaSolid.__json__(self)
        attrs = {'EndSweptArea': self.EndSweptArea}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRightCircularCone(IfcCsgPrimitive3D):
    def __init__(self, rtype, args):
        IfcCsgPrimitive3D.__init__(self, rtype, args)
        self.Height = args.pop()
        self.BottomRadius = args.pop()

    def __str__(self):
        return "{sup}:Height:{Height}:BottomRadius:{BottomRadius}".format(
            sup=IfcCsgPrimitive3D.__str__(self),
            Height=self.Height,
            BottomRadius=self.BottomRadius,
        )

    def __json__(self):
        sup = IfcCsgPrimitive3D.__json__(self)
        attrs = {'Height': self.Height, 'BottomRadius': self.BottomRadius}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRightCircularCylinder(IfcCsgPrimitive3D):
    def __init__(self, rtype, args):
        IfcCsgPrimitive3D.__init__(self, rtype, args)
        self.Height = args.pop()
        self.Radius = args.pop()

    def __str__(self):
        return "{sup}:Height:{Height}:Radius:{Radius}".format(
            sup=IfcCsgPrimitive3D.__str__(self),
            Height=self.Height,
            Radius=self.Radius,
        )

    def __json__(self):
        sup = IfcCsgPrimitive3D.__json__(self)
        attrs = {'Height': self.Height, 'Radius': self.Radius}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcSectionedSolid(IfcSolidModel):
    def __init__(self, rtype, args):
        IfcSolidModel.__init__(self, rtype, args)
        self.Directrix = args.pop()
        self.CrossSections = args.pop()

    def __str__(self):
        return "{sup}:Directrix:{Directrix}:CrossSections:{CrossSections}".format(
            sup=IfcSolidModel.__str__(self),
            Directrix=self.Directrix,
            CrossSections=self.CrossSections,
        )

    def __json__(self):
        sup = IfcSolidModel.__json__(self)
        attrs = {'Directrix': self.Directrix, 'CrossSections': self.CrossSections}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSectionedSolidHorizontal(IfcSectionedSolid):
    def __init__(self, rtype, args):
        IfcSectionedSolid.__init__(self, rtype, args)
        self.CrossSectionPositions = args.pop()
        self.FixedAxisVertical = args.pop()

    def __str__(self):
        return "{sup}:CrossSectionPositions:{CrossSectionPositions}:FixedAxisVertical:{FixedAxisVertical}".format(
            sup=IfcSectionedSolid.__str__(self),
            CrossSectionPositions=self.CrossSectionPositions,
            FixedAxisVertical=self.FixedAxisVertical,
        )

    def __json__(self):
        sup = IfcSectionedSolid.__json__(self)
        attrs = {'CrossSectionPositions': self.CrossSectionPositions, 'FixedAxisVertical': self.FixedAxisVertical}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSimplePropertyTemplate(IfcPropertyTemplate):
    def __init__(self, rtype, args):
        IfcPropertyTemplate.__init__(self, rtype, args)
        self.TemplateType = args.pop()
        self.PrimaryMeasureType = args.pop()
        self.SecondaryMeasureType = args.pop()
        self.Enumerators = args.pop()
        self.PrimaryUnit = args.pop()
        self.SecondaryUnit = args.pop()
        self.Expression = args.pop()
        self.AccessState = args.pop()

    def __str__(self):
        return "{sup}:TemplateType:{TemplateType}:PrimaryMeasureType:{PrimaryMeasureType}:SecondaryMeasureType:{SecondaryMeasureType}:Enumerators:{Enumerators}:PrimaryUnit:{PrimaryUnit}:SecondaryUnit:{SecondaryUnit}:Expression:{Expression}:AccessState:{AccessState}".format(
            sup=IfcPropertyTemplate.__str__(self),
            TemplateType=self.TemplateType,
            PrimaryMeasureType=self.PrimaryMeasureType,
            SecondaryMeasureType=self.SecondaryMeasureType,
            Enumerators=self.Enumerators,
            PrimaryUnit=self.PrimaryUnit,
            SecondaryUnit=self.SecondaryUnit,
            Expression=self.Expression,
            AccessState=self.AccessState,
        )

    def __json__(self):
        sup = IfcPropertyTemplate.__json__(self)
        attrs = {'TemplateType': self.TemplateType, 'PrimaryMeasureType': self.PrimaryMeasureType,
                 'SecondaryMeasureType': self.SecondaryMeasureType, 'Enumerators': self.Enumerators,
                 'PrimaryUnit': self.PrimaryUnit, 'SecondaryUnit': self.SecondaryUnit, 'Expression': self.Expression,
                 'AccessState': self.AccessState}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcSpatialElement(IfcProduct):
    def __init__(self, rtype, args):
        IfcProduct.__init__(self, rtype, args)
        self.LongName = args.pop()

    def __str__(self):
        return "{sup}:LongName:{LongName}".format(
            sup=IfcProduct.__str__(self),
            LongName=self.LongName,
        )

    def __json__(self):
        sup = IfcProduct.__json__(self)
        attrs = {'LongName': self.LongName}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcSpatialElementType(IfcTypeProduct):
    def __init__(self, rtype, args):
        IfcTypeProduct.__init__(self, rtype, args)
        self.ElementType = args.pop()

    def __str__(self):
        return "{sup}:ElementType:{ElementType}".format(
            sup=IfcTypeProduct.__str__(self),
            ElementType=self.ElementType,
        )

    def __json__(self):
        sup = IfcTypeProduct.__json__(self)
        attrs = {'ElementType': self.ElementType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcSpatialStructureElement(IfcSpatialElement):
    def __init__(self, rtype, args):
        IfcSpatialElement.__init__(self, rtype, args)
        self.CompositionType = args.pop()

    def __str__(self):
        return "{sup}:CompositionType:{CompositionType}".format(
            sup=IfcSpatialElement.__str__(self),
            CompositionType=self.CompositionType,
        )

    def __json__(self):
        sup = IfcSpatialElement.__json__(self)
        attrs = {'CompositionType': self.CompositionType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcSpatialStructureElementType(IfcSpatialElementType):
    def __init__(self, rtype, args):
        IfcSpatialElementType.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcSpatialElementType.__str__(self),
        )

    def __json__(self):
        sup = IfcSpatialElementType.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSpatialZone(IfcSpatialElement):
    def __init__(self, rtype, args):
        IfcSpatialElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcSpatialElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcSpatialElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSpatialZoneType(IfcSpatialElementType):
    def __init__(self, rtype, args):
        IfcSpatialElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.LongName = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:LongName:{LongName}".format(
            sup=IfcSpatialElementType.__str__(self),
            PredefinedType=self.PredefinedType,
            LongName=self.LongName,
        )

    def __json__(self):
        sup = IfcSpatialElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'LongName': self.LongName}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSphere(IfcCsgPrimitive3D):
    def __init__(self, rtype, args):
        IfcCsgPrimitive3D.__init__(self, rtype, args)
        self.Radius = args.pop()

    def __str__(self):
        return "{sup}:Radius:{Radius}".format(
            sup=IfcCsgPrimitive3D.__str__(self),
            Radius=self.Radius,
        )

    def __json__(self):
        sup = IfcCsgPrimitive3D.__json__(self)
        attrs = {'Radius': self.Radius}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSphericalSurface(IfcElementarySurface):
    def __init__(self, rtype, args):
        IfcElementarySurface.__init__(self, rtype, args)
        self.Radius = args.pop()

    def __str__(self):
        return "{sup}:Radius:{Radius}".format(
            sup=IfcElementarySurface.__str__(self),
            Radius=self.Radius,
        )

    def __json__(self):
        sup = IfcElementarySurface.__json__(self)
        attrs = {'Radius': self.Radius}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcStructuralActivity(IfcProduct):
    def __init__(self, rtype, args):
        IfcProduct.__init__(self, rtype, args)
        self.AppliedLoad = args.pop()
        self.GlobalOrLocal = args.pop()

    def __str__(self):
        return "{sup}:AppliedLoad:{AppliedLoad}:GlobalOrLocal:{GlobalOrLocal}".format(
            sup=IfcProduct.__str__(self),
            AppliedLoad=self.AppliedLoad,
            GlobalOrLocal=self.GlobalOrLocal,
        )

    def __json__(self):
        sup = IfcProduct.__json__(self)
        attrs = {'AppliedLoad': self.AppliedLoad, 'GlobalOrLocal': self.GlobalOrLocal}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcStructuralItem(IfcProduct):
    def __init__(self, rtype, args):
        IfcProduct.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcProduct.__str__(self),
        )

    def __json__(self):
        sup = IfcProduct.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcStructuralMember(IfcStructuralItem):
    def __init__(self, rtype, args):
        IfcStructuralItem.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcStructuralItem.__str__(self),
        )

    def __json__(self):
        sup = IfcStructuralItem.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcStructuralReaction(IfcStructuralActivity):
    def __init__(self, rtype, args):
        IfcStructuralActivity.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcStructuralActivity.__str__(self),
        )

    def __json__(self):
        sup = IfcStructuralActivity.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralSurfaceMember(IfcStructuralMember):
    def __init__(self, rtype, args):
        IfcStructuralMember.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.Thickness = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:Thickness:{Thickness}".format(
            sup=IfcStructuralMember.__str__(self),
            PredefinedType=self.PredefinedType,
            Thickness=self.Thickness,
        )

    def __json__(self):
        sup = IfcStructuralMember.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'Thickness': self.Thickness}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralSurfaceMemberVarying(IfcStructuralSurfaceMember):
    def __init__(self, rtype, args):
        IfcStructuralSurfaceMember.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcStructuralSurfaceMember.__str__(self),
        )

    def __json__(self):
        sup = IfcStructuralSurfaceMember.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralSurfaceReaction(IfcStructuralReaction):
    def __init__(self, rtype, args):
        IfcStructuralReaction.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcStructuralReaction.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcStructuralReaction.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSubContractResourceType(IfcConstructionResourceType):
    def __init__(self, rtype, args):
        IfcConstructionResourceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcConstructionResourceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcConstructionResourceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSurfaceCurve(IfcCurve):
    def __init__(self, rtype, args):
        IfcCurve.__init__(self, rtype, args)
        self.Curve3D = args.pop()
        self.AssociatedGeometry = args.pop()
        self.MasterRepresentation = args.pop()

    def __str__(self):
        return "{sup}:Curve3D:{Curve3D}:AssociatedGeometry:{AssociatedGeometry}:MasterRepresentation:{MasterRepresentation}".format(
            sup=IfcCurve.__str__(self),
            Curve3D=self.Curve3D,
            AssociatedGeometry=self.AssociatedGeometry,
            MasterRepresentation=self.MasterRepresentation,
        )

    def __json__(self):
        sup = IfcCurve.__json__(self)
        attrs = {'Curve3D': self.Curve3D, 'AssociatedGeometry': self.AssociatedGeometry,
                 'MasterRepresentation': self.MasterRepresentation}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSurfaceCurveSweptAreaSolid(IfcSweptAreaSolid):
    def __init__(self, rtype, args):
        IfcSweptAreaSolid.__init__(self, rtype, args)
        self.Directrix = args.pop()
        self.StartParam = args.pop()
        self.EndParam = args.pop()
        self.ReferenceSurface = args.pop()

    def __str__(self):
        return "{sup}:Directrix:{Directrix}:StartParam:{StartParam}:EndParam:{EndParam}:ReferenceSurface:{ReferenceSurface}".format(
            sup=IfcSweptAreaSolid.__str__(self),
            Directrix=self.Directrix,
            StartParam=self.StartParam,
            EndParam=self.EndParam,
            ReferenceSurface=self.ReferenceSurface,
        )

    def __json__(self):
        sup = IfcSweptAreaSolid.__json__(self)
        attrs = {'Directrix': self.Directrix, 'StartParam': self.StartParam, 'EndParam': self.EndParam,
                 'ReferenceSurface': self.ReferenceSurface}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSurfaceOfLinearExtrusion(IfcSweptSurface):
    def __init__(self, rtype, args):
        IfcSweptSurface.__init__(self, rtype, args)
        self.ExtrudedDirection = args.pop()
        self.Depth = args.pop()

    def __str__(self):
        return "{sup}:ExtrudedDirection:{ExtrudedDirection}:Depth:{Depth}".format(
            sup=IfcSweptSurface.__str__(self),
            ExtrudedDirection=self.ExtrudedDirection,
            Depth=self.Depth,
        )

    def __json__(self):
        sup = IfcSweptSurface.__json__(self)
        attrs = {'ExtrudedDirection': self.ExtrudedDirection, 'Depth': self.Depth}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSurfaceOfRevolution(IfcSweptSurface):
    def __init__(self, rtype, args):
        IfcSweptSurface.__init__(self, rtype, args)
        self.AxisPosition = args.pop()

    def __str__(self):
        return "{sup}:AxisPosition:{AxisPosition}".format(
            sup=IfcSweptSurface.__str__(self),
            AxisPosition=self.AxisPosition,
        )

    def __json__(self):
        sup = IfcSweptSurface.__json__(self)
        attrs = {'AxisPosition': self.AxisPosition}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSystemFurnitureElementType(IfcFurnishingElementType):
    def __init__(self, rtype, args):
        IfcFurnishingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFurnishingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFurnishingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTask(IfcProcess):
    def __init__(self, rtype, args):
        IfcProcess.__init__(self, rtype, args)
        self.Status = args.pop()
        self.WorkMethod = args.pop()
        self.IsMilestone = args.pop()
        self.Priority = args.pop()
        self.TaskTime = args.pop()
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:Status:{Status}:WorkMethod:{WorkMethod}:IsMilestone:{IsMilestone}:Priority:{Priority}:TaskTime:{TaskTime}:PredefinedType:{PredefinedType}".format(
            sup=IfcProcess.__str__(self),
            Status=self.Status,
            WorkMethod=self.WorkMethod,
            IsMilestone=self.IsMilestone,
            Priority=self.Priority,
            TaskTime=self.TaskTime,
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcProcess.__json__(self)
        attrs = {'Status': self.Status, 'WorkMethod': self.WorkMethod, 'IsMilestone': self.IsMilestone,
                 'Priority': self.Priority, 'TaskTime': self.TaskTime, 'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTaskType(IfcTypeProcess):
    def __init__(self, rtype, args):
        IfcTypeProcess.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.WorkMethod = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:WorkMethod:{WorkMethod}".format(
            sup=IfcTypeProcess.__str__(self),
            PredefinedType=self.PredefinedType,
            WorkMethod=self.WorkMethod,
        )

    def __json__(self):
        sup = IfcTypeProcess.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'WorkMethod': self.WorkMethod}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcTessellatedFaceSet(IfcTessellatedItem):
    def __init__(self, rtype, args):
        IfcTessellatedItem.__init__(self, rtype, args)
        self.Coordinates = args.pop()

    def __str__(self):
        return "{sup}:Coordinates:{Coordinates}".format(
            sup=IfcTessellatedItem.__str__(self),
            Coordinates=self.Coordinates,
        )

    def __json__(self):
        sup = IfcTessellatedItem.__json__(self)
        attrs = {'Coordinates': self.Coordinates}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcToroidalSurface(IfcElementarySurface):
    def __init__(self, rtype, args):
        IfcElementarySurface.__init__(self, rtype, args)
        self.MajorRadius = args.pop()
        self.MinorRadius = args.pop()

    def __str__(self):
        return "{sup}:MajorRadius:{MajorRadius}:MinorRadius:{MinorRadius}".format(
            sup=IfcElementarySurface.__str__(self),
            MajorRadius=self.MajorRadius,
            MinorRadius=self.MinorRadius,
        )

    def __json__(self):
        sup = IfcElementarySurface.__json__(self)
        attrs = {'MajorRadius': self.MajorRadius, 'MinorRadius': self.MinorRadius}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTransportElementType(IfcElementType):
    def __init__(self, rtype, args):
        IfcElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTriangulatedFaceSet(IfcTessellatedFaceSet):
    def __init__(self, rtype, args):
        IfcTessellatedFaceSet.__init__(self, rtype, args)
        self.Normals = args.pop()
        self.Closed = args.pop()
        self.CoordIndex = args.pop()
        self.PnIndex = args.pop()

    def __str__(self):
        return "{sup}:Normals:{Normals}:Closed:{Closed}:CoordIndex:{CoordIndex}:PnIndex:{PnIndex}".format(
            sup=IfcTessellatedFaceSet.__str__(self),
            Normals=self.Normals,
            Closed=self.Closed,
            CoordIndex=self.CoordIndex,
            PnIndex=self.PnIndex,
        )

    def __json__(self):
        sup = IfcTessellatedFaceSet.__json__(self)
        attrs = {'Normals': self.Normals, 'Closed': self.Closed, 'CoordIndex': self.CoordIndex, 'PnIndex': self.PnIndex}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTriangulatedIrregularNetwork(IfcTriangulatedFaceSet):
    def __init__(self, rtype, args):
        IfcTriangulatedFaceSet.__init__(self, rtype, args)
        self.Flags = args.pop()

    def __str__(self):
        return "{sup}:Flags:{Flags}".format(
            sup=IfcTriangulatedFaceSet.__str__(self),
            Flags=self.Flags,
        )

    def __json__(self):
        sup = IfcTriangulatedFaceSet.__json__(self)
        attrs = {'Flags': self.Flags}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcWindowLiningProperties(IfcPreDefinedPropertySet):
    def __init__(self, rtype, args):
        IfcPreDefinedPropertySet.__init__(self, rtype, args)
        self.LiningDepth = args.pop()
        self.LiningThickness = args.pop()
        self.TransomThickness = args.pop()
        self.MullionThickness = args.pop()
        self.FirstTransomOffset = args.pop()
        self.SecondTransomOffset = args.pop()
        self.FirstMullionOffset = args.pop()
        self.SecondMullionOffset = args.pop()
        self.ShapeAspectStyle = args.pop()
        self.LiningOffset = args.pop()
        self.LiningToPanelOffsetX = args.pop()
        self.LiningToPanelOffsetY = args.pop()

    def __str__(self):
        return "{sup}:LiningDepth:{LiningDepth}:LiningThickness:{LiningThickness}:TransomThickness:{TransomThickness}:MullionThickness:{MullionThickness}:FirstTransomOffset:{FirstTransomOffset}:SecondTransomOffset:{SecondTransomOffset}:FirstMullionOffset:{FirstMullionOffset}:SecondMullionOffset:{SecondMullionOffset}:ShapeAspectStyle:{ShapeAspectStyle}:LiningOffset:{LiningOffset}:LiningToPanelOffsetX:{LiningToPanelOffsetX}:LiningToPanelOffsetY:{LiningToPanelOffsetY}".format(
            sup=IfcPreDefinedPropertySet.__str__(self),
            LiningDepth=self.LiningDepth,
            LiningThickness=self.LiningThickness,
            TransomThickness=self.TransomThickness,
            MullionThickness=self.MullionThickness,
            FirstTransomOffset=self.FirstTransomOffset,
            SecondTransomOffset=self.SecondTransomOffset,
            FirstMullionOffset=self.FirstMullionOffset,
            SecondMullionOffset=self.SecondMullionOffset,
            ShapeAspectStyle=self.ShapeAspectStyle,
            LiningOffset=self.LiningOffset,
            LiningToPanelOffsetX=self.LiningToPanelOffsetX,
            LiningToPanelOffsetY=self.LiningToPanelOffsetY,
        )

    def __json__(self):
        sup = IfcPreDefinedPropertySet.__json__(self)
        attrs = {'LiningDepth': self.LiningDepth, 'LiningThickness': self.LiningThickness,
                 'TransomThickness': self.TransomThickness, 'MullionThickness': self.MullionThickness,
                 'FirstTransomOffset': self.FirstTransomOffset, 'SecondTransomOffset': self.SecondTransomOffset,
                 'FirstMullionOffset': self.FirstMullionOffset, 'SecondMullionOffset': self.SecondMullionOffset,
                 'ShapeAspectStyle': self.ShapeAspectStyle, 'LiningOffset': self.LiningOffset,
                 'LiningToPanelOffsetX': self.LiningToPanelOffsetX, 'LiningToPanelOffsetY': self.LiningToPanelOffsetY}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcWindowPanelProperties(IfcPreDefinedPropertySet):
    def __init__(self, rtype, args):
        IfcPreDefinedPropertySet.__init__(self, rtype, args)
        self.OperationType = args.pop()
        self.PanelPosition = args.pop()
        self.FrameDepth = args.pop()
        self.FrameThickness = args.pop()
        self.ShapeAspectStyle = args.pop()

    def __str__(self):
        return "{sup}:OperationType:{OperationType}:PanelPosition:{PanelPosition}:FrameDepth:{FrameDepth}:FrameThickness:{FrameThickness}:ShapeAspectStyle:{ShapeAspectStyle}".format(
            sup=IfcPreDefinedPropertySet.__str__(self),
            OperationType=self.OperationType,
            PanelPosition=self.PanelPosition,
            FrameDepth=self.FrameDepth,
            FrameThickness=self.FrameThickness,
            ShapeAspectStyle=self.ShapeAspectStyle,
        )

    def __json__(self):
        sup = IfcPreDefinedPropertySet.__json__(self)
        attrs = {'OperationType': self.OperationType, 'PanelPosition': self.PanelPosition,
                 'FrameDepth': self.FrameDepth, 'FrameThickness': self.FrameThickness,
                 'ShapeAspectStyle': self.ShapeAspectStyle}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcActor(IfcObject):
    def __init__(self, rtype, args):
        IfcObject.__init__(self, rtype, args)
        self.TheActor = args.pop()

    def __str__(self):
        return "{sup}:TheActor:{TheActor}".format(
            sup=IfcObject.__str__(self),
            TheActor=self.TheActor,
        )

    def __json__(self):
        sup = IfcObject.__json__(self)
        attrs = {'TheActor': self.TheActor}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAdvancedBrep(IfcManifoldSolidBrep):
    def __init__(self, rtype, args):
        IfcManifoldSolidBrep.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcManifoldSolidBrep.__str__(self),
        )

    def __json__(self):
        sup = IfcManifoldSolidBrep.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAdvancedBrepWithVoids(IfcAdvancedBrep):
    def __init__(self, rtype, args):
        IfcAdvancedBrep.__init__(self, rtype, args)
        self.Voids = args.pop()

    def __str__(self):
        return "{sup}:Voids:{Voids}".format(
            sup=IfcAdvancedBrep.__str__(self),
            Voids=self.Voids,
        )

    def __json__(self):
        sup = IfcAdvancedBrep.__json__(self)
        attrs = {'Voids': self.Voids}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAlignment2DHorizontalSegment(IfcAlignment2DSegment):
    def __init__(self, rtype, args):
        IfcAlignment2DSegment.__init__(self, rtype, args)
        self.CurveGeometry = args.pop()

    def __str__(self):
        return "{sup}:CurveGeometry:{CurveGeometry}".format(
            sup=IfcAlignment2DSegment.__str__(self),
            CurveGeometry=self.CurveGeometry,
        )

    def __json__(self):
        sup = IfcAlignment2DSegment.__json__(self)
        attrs = {'CurveGeometry': self.CurveGeometry}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAlignment2DVerSegCircularArc(IfcAlignment2DVerticalSegment):
    def __init__(self, rtype, args):
        IfcAlignment2DVerticalSegment.__init__(self, rtype, args)
        self.Radius = args.pop()
        self.IsConvex = args.pop()

    def __str__(self):
        return "{sup}:Radius:{Radius}:IsConvex:{IsConvex}".format(
            sup=IfcAlignment2DVerticalSegment.__str__(self),
            Radius=self.Radius,
            IsConvex=self.IsConvex,
        )

    def __json__(self):
        sup = IfcAlignment2DVerticalSegment.__json__(self)
        attrs = {'Radius': self.Radius, 'IsConvex': self.IsConvex}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAlignment2DVerSegLine(IfcAlignment2DVerticalSegment):
    def __init__(self, rtype, args):
        IfcAlignment2DVerticalSegment.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcAlignment2DVerticalSegment.__str__(self),
        )

    def __json__(self):
        sup = IfcAlignment2DVerticalSegment.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAlignment2DVerSegParabolicArc(IfcAlignment2DVerticalSegment):
    def __init__(self, rtype, args):
        IfcAlignment2DVerticalSegment.__init__(self, rtype, args)
        self.ParabolaConstant = args.pop()
        self.IsConvex = args.pop()

    def __str__(self):
        return "{sup}:ParabolaConstant:{ParabolaConstant}:IsConvex:{IsConvex}".format(
            sup=IfcAlignment2DVerticalSegment.__str__(self),
            ParabolaConstant=self.ParabolaConstant,
            IsConvex=self.IsConvex,
        )

    def __json__(self):
        sup = IfcAlignment2DVerticalSegment.__json__(self)
        attrs = {'ParabolaConstant': self.ParabolaConstant, 'IsConvex': self.IsConvex}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAnnotation(IfcProduct):
    def __init__(self, rtype, args):
        IfcProduct.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcProduct.__str__(self),
        )

    def __json__(self):
        sup = IfcProduct.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcBSplineSurface(IfcBoundedSurface):
    def __init__(self, rtype, args):
        IfcBoundedSurface.__init__(self, rtype, args)
        self.UDegree = args.pop()
        self.VDegree = args.pop()
        self.ControlPointsList = args.pop()
        self.SurfaceForm = args.pop()
        self.UClosed = args.pop()
        self.VClosed = args.pop()
        self.SelfIntersect = args.pop()

    def __str__(self):
        return "{sup}:UDegree:{UDegree}:VDegree:{VDegree}:ControlPointsList:{ControlPointsList}:SurfaceForm:{SurfaceForm}:UClosed:{UClosed}:VClosed:{VClosed}:SelfIntersect:{SelfIntersect}".format(
            sup=IfcBoundedSurface.__str__(self),
            UDegree=self.UDegree,
            VDegree=self.VDegree,
            ControlPointsList=self.ControlPointsList,
            SurfaceForm=self.SurfaceForm,
            UClosed=self.UClosed,
            VClosed=self.VClosed,
            SelfIntersect=self.SelfIntersect,
        )

    def __json__(self):
        sup = IfcBoundedSurface.__json__(self)
        attrs = {'UDegree': self.UDegree, 'VDegree': self.VDegree, 'ControlPointsList': self.ControlPointsList,
                 'SurfaceForm': self.SurfaceForm, 'UClosed': self.UClosed, 'VClosed': self.VClosed,
                 'SelfIntersect': self.SelfIntersect}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBSplineSurfaceWithKnots(IfcBSplineSurface):
    def __init__(self, rtype, args):
        IfcBSplineSurface.__init__(self, rtype, args)
        self.UMultiplicities = args.pop()
        self.VMultiplicities = args.pop()
        self.UKnots = args.pop()
        self.VKnots = args.pop()
        self.KnotSpec = args.pop()

    def __str__(self):
        return "{sup}:UMultiplicities:{UMultiplicities}:VMultiplicities:{VMultiplicities}:UKnots:{UKnots}:VKnots:{VKnots}:KnotSpec:{KnotSpec}".format(
            sup=IfcBSplineSurface.__str__(self),
            UMultiplicities=self.UMultiplicities,
            VMultiplicities=self.VMultiplicities,
            UKnots=self.UKnots,
            VKnots=self.VKnots,
            KnotSpec=self.KnotSpec,
        )

    def __json__(self):
        sup = IfcBSplineSurface.__json__(self)
        attrs = {'UMultiplicities': self.UMultiplicities, 'VMultiplicities': self.VMultiplicities,
                 'UKnots': self.UKnots, 'VKnots': self.VKnots, 'KnotSpec': self.KnotSpec}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBlock(IfcCsgPrimitive3D):
    def __init__(self, rtype, args):
        IfcCsgPrimitive3D.__init__(self, rtype, args)
        self.XLength = args.pop()
        self.YLength = args.pop()
        self.ZLength = args.pop()

    def __str__(self):
        return "{sup}:XLength:{XLength}:YLength:{YLength}:ZLength:{ZLength}".format(
            sup=IfcCsgPrimitive3D.__str__(self),
            XLength=self.XLength,
            YLength=self.YLength,
            ZLength=self.ZLength,
        )

    def __json__(self):
        sup = IfcCsgPrimitive3D.__json__(self)
        attrs = {'XLength': self.XLength, 'YLength': self.YLength, 'ZLength': self.ZLength}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBooleanClippingResult(IfcBooleanResult):
    def __init__(self, rtype, args):
        IfcBooleanResult.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcBooleanResult.__str__(self),
        )

    def __json__(self):
        sup = IfcBooleanResult.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcBoundedCurve(IfcCurve):
    def __init__(self, rtype, args):
        IfcCurve.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcCurve.__str__(self),
        )

    def __json__(self):
        sup = IfcCurve.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBuilding(IfcSpatialStructureElement):
    def __init__(self, rtype, args):
        IfcSpatialStructureElement.__init__(self, rtype, args)
        self.ElevationOfRefHeight = args.pop()
        self.ElevationOfTerrain = args.pop()
        self.BuildingAddress = args.pop()

    def __str__(self):
        return "{sup}:ElevationOfRefHeight:{ElevationOfRefHeight}:ElevationOfTerrain:{ElevationOfTerrain}:BuildingAddress:{BuildingAddress}".format(
            sup=IfcSpatialStructureElement.__str__(self),
            ElevationOfRefHeight=self.ElevationOfRefHeight,
            ElevationOfTerrain=self.ElevationOfTerrain,
            BuildingAddress=self.BuildingAddress,
        )

    def __json__(self):
        sup = IfcSpatialStructureElement.__json__(self)
        attrs = {'ElevationOfRefHeight': self.ElevationOfRefHeight, 'ElevationOfTerrain': self.ElevationOfTerrain,
                 'BuildingAddress': self.BuildingAddress}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcBuildingElementType(IfcElementType):
    def __init__(self, rtype, args):
        IfcElementType.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcElementType.__str__(self),
        )

    def __json__(self):
        sup = IfcElementType.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBuildingStorey(IfcSpatialStructureElement):
    def __init__(self, rtype, args):
        IfcSpatialStructureElement.__init__(self, rtype, args)
        self.Elevation = args.pop()

    def __str__(self):
        return "{sup}:Elevation:{Elevation}".format(
            sup=IfcSpatialStructureElement.__str__(self),
            Elevation=self.Elevation,
        )

    def __json__(self):
        sup = IfcSpatialStructureElement.__json__(self)
        attrs = {'Elevation': self.Elevation}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcChimneyType(IfcBuildingElementType):
    def __init__(self, rtype, args):
        IfcBuildingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCircleHollowProfileDef(IfcCircleProfileDef):
    def __init__(self, rtype, args):
        IfcCircleProfileDef.__init__(self, rtype, args)
        self.WallThickness = args.pop()

    def __str__(self):
        return "{sup}:WallThickness:{WallThickness}".format(
            sup=IfcCircleProfileDef.__str__(self),
            WallThickness=self.WallThickness,
        )

    def __json__(self):
        sup = IfcCircleProfileDef.__json__(self)
        attrs = {'WallThickness': self.WallThickness}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCivilElementType(IfcElementType):
    def __init__(self, rtype, args):
        IfcElementType.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcElementType.__str__(self),
        )

    def __json__(self):
        sup = IfcElementType.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcColumnType(IfcBuildingElementType):
    def __init__(self, rtype, args):
        IfcBuildingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcComplexPropertyTemplate(IfcPropertyTemplate):
    def __init__(self, rtype, args):
        IfcPropertyTemplate.__init__(self, rtype, args)
        self.UsageName = args.pop()
        self.TemplateType = args.pop()
        self.HasPropertyTemplates = args.pop()

    def __str__(self):
        return "{sup}:UsageName:{UsageName}:TemplateType:{TemplateType}:HasPropertyTemplates:{HasPropertyTemplates}".format(
            sup=IfcPropertyTemplate.__str__(self),
            UsageName=self.UsageName,
            TemplateType=self.TemplateType,
            HasPropertyTemplates=self.HasPropertyTemplates,
        )

    def __json__(self):
        sup = IfcPropertyTemplate.__json__(self)
        attrs = {'UsageName': self.UsageName, 'TemplateType': self.TemplateType,
                 'HasPropertyTemplates': self.HasPropertyTemplates}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCompositeCurve(IfcBoundedCurve):
    def __init__(self, rtype, args):
        IfcBoundedCurve.__init__(self, rtype, args)
        self.Segments = args.pop()
        self.SelfIntersect = args.pop()

    def __str__(self):
        return "{sup}:Segments:{Segments}:SelfIntersect:{SelfIntersect}".format(
            sup=IfcBoundedCurve.__str__(self),
            Segments=self.Segments,
            SelfIntersect=self.SelfIntersect,
        )

    def __json__(self):
        sup = IfcBoundedCurve.__json__(self)
        attrs = {'Segments': self.Segments, 'SelfIntersect': self.SelfIntersect}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCompositeCurveOnSurface(IfcCompositeCurve):
    def __init__(self, rtype, args):
        IfcCompositeCurve.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcCompositeCurve.__str__(self),
        )

    def __json__(self):
        sup = IfcCompositeCurve.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcConic(IfcCurve):
    def __init__(self, rtype, args):
        IfcCurve.__init__(self, rtype, args)
        self.Position = args.pop()

    def __str__(self):
        return "{sup}:Position:{Position}".format(
            sup=IfcCurve.__str__(self),
            Position=self.Position,
        )

    def __json__(self):
        sup = IfcCurve.__json__(self)
        attrs = {'Position': self.Position}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcConstructionEquipmentResourceType(IfcConstructionResourceType):
    def __init__(self, rtype, args):
        IfcConstructionResourceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcConstructionResourceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcConstructionResourceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcConstructionMaterialResourceType(IfcConstructionResourceType):
    def __init__(self, rtype, args):
        IfcConstructionResourceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcConstructionResourceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcConstructionResourceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcConstructionProductResourceType(IfcConstructionResourceType):
    def __init__(self, rtype, args):
        IfcConstructionResourceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcConstructionResourceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcConstructionResourceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcConstructionResource(IfcResource):
    def __init__(self, rtype, args):
        IfcResource.__init__(self, rtype, args)
        self.Usage = args.pop()
        self.BaseCosts = args.pop()
        self.BaseQuantity = args.pop()

    def __str__(self):
        return "{sup}:Usage:{Usage}:BaseCosts:{BaseCosts}:BaseQuantity:{BaseQuantity}".format(
            sup=IfcResource.__str__(self),
            Usage=self.Usage,
            BaseCosts=self.BaseCosts,
            BaseQuantity=self.BaseQuantity,
        )

    def __json__(self):
        sup = IfcResource.__json__(self)
        attrs = {'Usage': self.Usage, 'BaseCosts': self.BaseCosts, 'BaseQuantity': self.BaseQuantity}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcControl(IfcObject):
    def __init__(self, rtype, args):
        IfcObject.__init__(self, rtype, args)
        self.Identification = args.pop()

    def __str__(self):
        return "{sup}:Identification:{Identification}".format(
            sup=IfcObject.__str__(self),
            Identification=self.Identification,
        )

    def __json__(self):
        sup = IfcObject.__json__(self)
        attrs = {'Identification': self.Identification}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCostItem(IfcControl):
    def __init__(self, rtype, args):
        IfcControl.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.CostValues = args.pop()
        self.CostQuantities = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:CostValues:{CostValues}:CostQuantities:{CostQuantities}".format(
            sup=IfcControl.__str__(self),
            PredefinedType=self.PredefinedType,
            CostValues=self.CostValues,
            CostQuantities=self.CostQuantities,
        )

    def __json__(self):
        sup = IfcControl.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'CostValues': self.CostValues,
                 'CostQuantities': self.CostQuantities}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCostSchedule(IfcControl):
    def __init__(self, rtype, args):
        IfcControl.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.Status = args.pop()
        self.SubmittedOn = args.pop()
        self.UpdateDate = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:Status:{Status}:SubmittedOn:{SubmittedOn}:UpdateDate:{UpdateDate}".format(
            sup=IfcControl.__str__(self),
            PredefinedType=self.PredefinedType,
            Status=self.Status,
            SubmittedOn=self.SubmittedOn,
            UpdateDate=self.UpdateDate,
        )

    def __json__(self):
        sup = IfcControl.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'Status': self.Status, 'SubmittedOn': self.SubmittedOn,
                 'UpdateDate': self.UpdateDate}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCoveringType(IfcBuildingElementType):
    def __init__(self, rtype, args):
        IfcBuildingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCrewResource(IfcConstructionResource):
    def __init__(self, rtype, args):
        IfcConstructionResource.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcConstructionResource.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcConstructionResource.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCurtainWallType(IfcBuildingElementType):
    def __init__(self, rtype, args):
        IfcBuildingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcCurveSegment2D(IfcBoundedCurve):
    def __init__(self, rtype, args):
        IfcBoundedCurve.__init__(self, rtype, args)
        self.StartPoint = args.pop()
        self.StartDirection = args.pop()
        self.SegmentLength = args.pop()

    def __str__(self):
        return "{sup}:StartPoint:{StartPoint}:StartDirection:{StartDirection}:SegmentLength:{SegmentLength}".format(
            sup=IfcBoundedCurve.__str__(self),
            StartPoint=self.StartPoint,
            StartDirection=self.StartDirection,
            SegmentLength=self.SegmentLength,
        )

    def __json__(self):
        sup = IfcBoundedCurve.__json__(self)
        attrs = {'StartPoint': self.StartPoint, 'StartDirection': self.StartDirection,
                 'SegmentLength': self.SegmentLength}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCylindricalSurface(IfcElementarySurface):
    def __init__(self, rtype, args):
        IfcElementarySurface.__init__(self, rtype, args)
        self.Radius = args.pop()

    def __str__(self):
        return "{sup}:Radius:{Radius}".format(
            sup=IfcElementarySurface.__str__(self),
            Radius=self.Radius,
        )

    def __json__(self):
        sup = IfcElementarySurface.__json__(self)
        attrs = {'Radius': self.Radius}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDistributionElementType(IfcElementType):
    def __init__(self, rtype, args):
        IfcElementType.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcElementType.__str__(self),
        )

    def __json__(self):
        sup = IfcElementType.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcDistributionFlowElementType(IfcDistributionElementType):
    def __init__(self, rtype, args):
        IfcDistributionElementType.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDistributionElementType.__str__(self),
        )

    def __json__(self):
        sup = IfcDistributionElementType.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDoorLiningProperties(IfcPreDefinedPropertySet):
    def __init__(self, rtype, args):
        IfcPreDefinedPropertySet.__init__(self, rtype, args)
        self.LiningDepth = args.pop()
        self.LiningThickness = args.pop()
        self.ThresholdDepth = args.pop()
        self.ThresholdThickness = args.pop()
        self.TransomThickness = args.pop()
        self.TransomOffset = args.pop()
        self.LiningOffset = args.pop()
        self.ThresholdOffset = args.pop()
        self.CasingThickness = args.pop()
        self.CasingDepth = args.pop()
        self.ShapeAspectStyle = args.pop()
        self.LiningToPanelOffsetX = args.pop()
        self.LiningToPanelOffsetY = args.pop()

    def __str__(self):
        return "{sup}:LiningDepth:{LiningDepth}:LiningThickness:{LiningThickness}:ThresholdDepth:{ThresholdDepth}:ThresholdThickness:{ThresholdThickness}:TransomThickness:{TransomThickness}:TransomOffset:{TransomOffset}:LiningOffset:{LiningOffset}:ThresholdOffset:{ThresholdOffset}:CasingThickness:{CasingThickness}:CasingDepth:{CasingDepth}:ShapeAspectStyle:{ShapeAspectStyle}:LiningToPanelOffsetX:{LiningToPanelOffsetX}:LiningToPanelOffsetY:{LiningToPanelOffsetY}".format(
            sup=IfcPreDefinedPropertySet.__str__(self),
            LiningDepth=self.LiningDepth,
            LiningThickness=self.LiningThickness,
            ThresholdDepth=self.ThresholdDepth,
            ThresholdThickness=self.ThresholdThickness,
            TransomThickness=self.TransomThickness,
            TransomOffset=self.TransomOffset,
            LiningOffset=self.LiningOffset,
            ThresholdOffset=self.ThresholdOffset,
            CasingThickness=self.CasingThickness,
            CasingDepth=self.CasingDepth,
            ShapeAspectStyle=self.ShapeAspectStyle,
            LiningToPanelOffsetX=self.LiningToPanelOffsetX,
            LiningToPanelOffsetY=self.LiningToPanelOffsetY,
        )

    def __json__(self):
        sup = IfcPreDefinedPropertySet.__json__(self)
        attrs = {'LiningDepth': self.LiningDepth, 'LiningThickness': self.LiningThickness,
                 'ThresholdDepth': self.ThresholdDepth, 'ThresholdThickness': self.ThresholdThickness,
                 'TransomThickness': self.TransomThickness, 'TransomOffset': self.TransomOffset,
                 'LiningOffset': self.LiningOffset, 'ThresholdOffset': self.ThresholdOffset,
                 'CasingThickness': self.CasingThickness, 'CasingDepth': self.CasingDepth,
                 'ShapeAspectStyle': self.ShapeAspectStyle, 'LiningToPanelOffsetX': self.LiningToPanelOffsetX,
                 'LiningToPanelOffsetY': self.LiningToPanelOffsetY}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDoorPanelProperties(IfcPreDefinedPropertySet):
    def __init__(self, rtype, args):
        IfcPreDefinedPropertySet.__init__(self, rtype, args)
        self.PanelDepth = args.pop()
        self.PanelOperation = args.pop()
        self.PanelWidth = args.pop()
        self.PanelPosition = args.pop()
        self.ShapeAspectStyle = args.pop()

    def __str__(self):
        return "{sup}:PanelDepth:{PanelDepth}:PanelOperation:{PanelOperation}:PanelWidth:{PanelWidth}:PanelPosition:{PanelPosition}:ShapeAspectStyle:{ShapeAspectStyle}".format(
            sup=IfcPreDefinedPropertySet.__str__(self),
            PanelDepth=self.PanelDepth,
            PanelOperation=self.PanelOperation,
            PanelWidth=self.PanelWidth,
            PanelPosition=self.PanelPosition,
            ShapeAspectStyle=self.ShapeAspectStyle,
        )

    def __json__(self):
        sup = IfcPreDefinedPropertySet.__json__(self)
        attrs = {'PanelDepth': self.PanelDepth, 'PanelOperation': self.PanelOperation, 'PanelWidth': self.PanelWidth,
                 'PanelPosition': self.PanelPosition, 'ShapeAspectStyle': self.ShapeAspectStyle}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDoorType(IfcBuildingElementType):
    def __init__(self, rtype, args):
        IfcBuildingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.OperationType = args.pop()
        self.ParameterTakesPrecedence = args.pop()
        self.UserDefinedOperationType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:OperationType:{OperationType}:ParameterTakesPrecedence:{ParameterTakesPrecedence}:UserDefinedOperationType:{UserDefinedOperationType}".format(
            sup=IfcBuildingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
            OperationType=self.OperationType,
            ParameterTakesPrecedence=self.ParameterTakesPrecedence,
            UserDefinedOperationType=self.UserDefinedOperationType,
        )

    def __json__(self):
        sup = IfcBuildingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'OperationType': self.OperationType,
                 'ParameterTakesPrecedence': self.ParameterTakesPrecedence,
                 'UserDefinedOperationType': self.UserDefinedOperationType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDraughtingPreDefinedColour(IfcPreDefinedColour):
    def __init__(self, rtype, args):
        IfcPreDefinedColour.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcPreDefinedColour.__str__(self),
        )

    def __json__(self):
        sup = IfcPreDefinedColour.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDraughtingPreDefinedCurveFont(IfcPreDefinedCurveFont):
    def __init__(self, rtype, args):
        IfcPreDefinedCurveFont.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcPreDefinedCurveFont.__str__(self),
        )

    def __json__(self):
        sup = IfcPreDefinedCurveFont.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcElement(IfcProduct):
    def __init__(self, rtype, args):
        IfcProduct.__init__(self, rtype, args)
        self.Tag = args.pop()

    def __str__(self):
        return "{sup}:Tag:{Tag}".format(
            sup=IfcProduct.__str__(self),
            Tag=self.Tag,
        )

    def __json__(self):
        sup = IfcProduct.__json__(self)
        attrs = {'Tag': self.Tag}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcElementAssembly(IfcElement):
    def __init__(self, rtype, args):
        IfcElement.__init__(self, rtype, args)
        self.AssemblyPlace = args.pop()
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:AssemblyPlace:{AssemblyPlace}:PredefinedType:{PredefinedType}".format(
            sup=IfcElement.__str__(self),
            AssemblyPlace=self.AssemblyPlace,
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcElement.__json__(self)
        attrs = {'AssemblyPlace': self.AssemblyPlace, 'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcElementAssemblyType(IfcElementType):
    def __init__(self, rtype, args):
        IfcElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcElementComponent(IfcElement):
    def __init__(self, rtype, args):
        IfcElement.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcElement.__str__(self),
        )

    def __json__(self):
        sup = IfcElement.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcElementComponentType(IfcElementType):
    def __init__(self, rtype, args):
        IfcElementType.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcElementType.__str__(self),
        )

    def __json__(self):
        sup = IfcElementType.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcEllipse(IfcConic):
    def __init__(self, rtype, args):
        IfcConic.__init__(self, rtype, args)
        self.SemiAxis1 = args.pop()
        self.SemiAxis2 = args.pop()

    def __str__(self):
        return "{sup}:SemiAxis1:{SemiAxis1}:SemiAxis2:{SemiAxis2}".format(
            sup=IfcConic.__str__(self),
            SemiAxis1=self.SemiAxis1,
            SemiAxis2=self.SemiAxis2,
        )

    def __json__(self):
        sup = IfcConic.__json__(self)
        attrs = {'SemiAxis1': self.SemiAxis1, 'SemiAxis2': self.SemiAxis2}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcEnergyConversionDeviceType(IfcDistributionFlowElementType):
    def __init__(self, rtype, args):
        IfcDistributionFlowElementType.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDistributionFlowElementType.__str__(self),
        )

    def __json__(self):
        sup = IfcDistributionFlowElementType.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcEngineType(IfcEnergyConversionDeviceType):
    def __init__(self, rtype, args):
        IfcEnergyConversionDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcEvaporativeCoolerType(IfcEnergyConversionDeviceType):
    def __init__(self, rtype, args):
        IfcEnergyConversionDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcEvaporatorType(IfcEnergyConversionDeviceType):
    def __init__(self, rtype, args):
        IfcEnergyConversionDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcEvent(IfcProcess):
    def __init__(self, rtype, args):
        IfcProcess.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.EventTriggerType = args.pop()
        self.UserDefinedEventTriggerType = args.pop()
        self.EventOccurenceTime = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:EventTriggerType:{EventTriggerType}:UserDefinedEventTriggerType:{UserDefinedEventTriggerType}:EventOccurenceTime:{EventOccurenceTime}".format(
            sup=IfcProcess.__str__(self),
            PredefinedType=self.PredefinedType,
            EventTriggerType=self.EventTriggerType,
            UserDefinedEventTriggerType=self.UserDefinedEventTriggerType,
            EventOccurenceTime=self.EventOccurenceTime,
        )

    def __json__(self):
        sup = IfcProcess.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'EventTriggerType': self.EventTriggerType,
                 'UserDefinedEventTriggerType': self.UserDefinedEventTriggerType,
                 'EventOccurenceTime': self.EventOccurenceTime}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcExternalSpatialStructureElement(IfcSpatialElement):
    def __init__(self, rtype, args):
        IfcSpatialElement.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcSpatialElement.__str__(self),
        )

    def __json__(self):
        sup = IfcSpatialElement.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFacetedBrep(IfcManifoldSolidBrep):
    def __init__(self, rtype, args):
        IfcManifoldSolidBrep.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcManifoldSolidBrep.__str__(self),
        )

    def __json__(self):
        sup = IfcManifoldSolidBrep.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFacetedBrepWithVoids(IfcFacetedBrep):
    def __init__(self, rtype, args):
        IfcFacetedBrep.__init__(self, rtype, args)
        self.Voids = args.pop()

    def __str__(self):
        return "{sup}:Voids:{Voids}".format(
            sup=IfcFacetedBrep.__str__(self),
            Voids=self.Voids,
        )

    def __json__(self):
        sup = IfcFacetedBrep.__json__(self)
        attrs = {'Voids': self.Voids}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFastener(IfcElementComponent):
    def __init__(self, rtype, args):
        IfcElementComponent.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcElementComponent.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcElementComponent.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFastenerType(IfcElementComponentType):
    def __init__(self, rtype, args):
        IfcElementComponentType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcElementComponentType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcElementComponentType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcFeatureElement(IfcElement):
    def __init__(self, rtype, args):
        IfcElement.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcElement.__str__(self),
        )

    def __json__(self):
        sup = IfcElement.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcFeatureElementAddition(IfcFeatureElement):
    def __init__(self, rtype, args):
        IfcFeatureElement.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcFeatureElement.__str__(self),
        )

    def __json__(self):
        sup = IfcFeatureElement.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcFeatureElementSubtraction(IfcFeatureElement):
    def __init__(self, rtype, args):
        IfcFeatureElement.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcFeatureElement.__str__(self),
        )

    def __json__(self):
        sup = IfcFeatureElement.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcFlowControllerType(IfcDistributionFlowElementType):
    def __init__(self, rtype, args):
        IfcDistributionFlowElementType.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDistributionFlowElementType.__str__(self),
        )

    def __json__(self):
        sup = IfcDistributionFlowElementType.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcFlowFittingType(IfcDistributionFlowElementType):
    def __init__(self, rtype, args):
        IfcDistributionFlowElementType.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDistributionFlowElementType.__str__(self),
        )

    def __json__(self):
        sup = IfcDistributionFlowElementType.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFlowMeterType(IfcFlowControllerType):
    def __init__(self, rtype, args):
        IfcFlowControllerType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowControllerType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowControllerType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcFlowMovingDeviceType(IfcDistributionFlowElementType):
    def __init__(self, rtype, args):
        IfcDistributionFlowElementType.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDistributionFlowElementType.__str__(self),
        )

    def __json__(self):
        sup = IfcDistributionFlowElementType.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcFlowSegmentType(IfcDistributionFlowElementType):
    def __init__(self, rtype, args):
        IfcDistributionFlowElementType.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDistributionFlowElementType.__str__(self),
        )

    def __json__(self):
        sup = IfcDistributionFlowElementType.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcFlowStorageDeviceType(IfcDistributionFlowElementType):
    def __init__(self, rtype, args):
        IfcDistributionFlowElementType.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDistributionFlowElementType.__str__(self),
        )

    def __json__(self):
        sup = IfcDistributionFlowElementType.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcFlowTerminalType(IfcDistributionFlowElementType):
    def __init__(self, rtype, args):
        IfcDistributionFlowElementType.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDistributionFlowElementType.__str__(self),
        )

    def __json__(self):
        sup = IfcDistributionFlowElementType.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcFlowTreatmentDeviceType(IfcDistributionFlowElementType):
    def __init__(self, rtype, args):
        IfcDistributionFlowElementType.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDistributionFlowElementType.__str__(self),
        )

    def __json__(self):
        sup = IfcDistributionFlowElementType.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFootingType(IfcBuildingElementType):
    def __init__(self, rtype, args):
        IfcBuildingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFurnishingElement(IfcElement):
    def __init__(self, rtype, args):
        IfcElement.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcElement.__str__(self),
        )

    def __json__(self):
        sup = IfcElement.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFurniture(IfcFurnishingElement):
    def __init__(self, rtype, args):
        IfcFurnishingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFurnishingElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFurnishingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcGeographicElement(IfcElement):
    def __init__(self, rtype, args):
        IfcElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcGroup(IfcObject):
    def __init__(self, rtype, args):
        IfcObject.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcObject.__str__(self),
        )

    def __json__(self):
        sup = IfcObject.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcHeatExchangerType(IfcEnergyConversionDeviceType):
    def __init__(self, rtype, args):
        IfcEnergyConversionDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcHumidifierType(IfcEnergyConversionDeviceType):
    def __init__(self, rtype, args):
        IfcEnergyConversionDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcIndexedPolyCurve(IfcBoundedCurve):
    def __init__(self, rtype, args):
        IfcBoundedCurve.__init__(self, rtype, args)
        self.Points = args.pop()
        self.Segments = args.pop()
        self.SelfIntersect = args.pop()

    def __str__(self):
        return "{sup}:Points:{Points}:Segments:{Segments}:SelfIntersect:{SelfIntersect}".format(
            sup=IfcBoundedCurve.__str__(self),
            Points=self.Points,
            Segments=self.Segments,
            SelfIntersect=self.SelfIntersect,
        )

    def __json__(self):
        sup = IfcBoundedCurve.__json__(self)
        attrs = {'Points': self.Points, 'Segments': self.Segments, 'SelfIntersect': self.SelfIntersect}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcInterceptorType(IfcFlowTreatmentDeviceType):
    def __init__(self, rtype, args):
        IfcFlowTreatmentDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTreatmentDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTreatmentDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcIntersectionCurve(IfcSurfaceCurve):
    def __init__(self, rtype, args):
        IfcSurfaceCurve.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcSurfaceCurve.__str__(self),
        )

    def __json__(self):
        sup = IfcSurfaceCurve.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcInventory(IfcGroup):
    def __init__(self, rtype, args):
        IfcGroup.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.Jurisdiction = args.pop()
        self.ResponsiblePersons = args.pop()
        self.LastUpdateDate = args.pop()
        self.CurrentValue = args.pop()
        self.OriginalValue = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:Jurisdiction:{Jurisdiction}:ResponsiblePersons:{ResponsiblePersons}:LastUpdateDate:{LastUpdateDate}:CurrentValue:{CurrentValue}:OriginalValue:{OriginalValue}".format(
            sup=IfcGroup.__str__(self),
            PredefinedType=self.PredefinedType,
            Jurisdiction=self.Jurisdiction,
            ResponsiblePersons=self.ResponsiblePersons,
            LastUpdateDate=self.LastUpdateDate,
            CurrentValue=self.CurrentValue,
            OriginalValue=self.OriginalValue,
        )

    def __json__(self):
        sup = IfcGroup.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'Jurisdiction': self.Jurisdiction,
                 'ResponsiblePersons': self.ResponsiblePersons, 'LastUpdateDate': self.LastUpdateDate,
                 'CurrentValue': self.CurrentValue, 'OriginalValue': self.OriginalValue}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcJunctionBoxType(IfcFlowFittingType):
    def __init__(self, rtype, args):
        IfcFlowFittingType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowFittingType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowFittingType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLaborResource(IfcConstructionResource):
    def __init__(self, rtype, args):
        IfcConstructionResource.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcConstructionResource.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcConstructionResource.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLampType(IfcFlowTerminalType):
    def __init__(self, rtype, args):
        IfcFlowTerminalType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminalType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminalType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLightFixtureType(IfcFlowTerminalType):
    def __init__(self, rtype, args):
        IfcFlowTerminalType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminalType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminalType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLineSegment2D(IfcCurveSegment2D):
    def __init__(self, rtype, args):
        IfcCurveSegment2D.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcCurveSegment2D.__str__(self),
        )

    def __json__(self):
        sup = IfcCurveSegment2D.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMechanicalFastener(IfcElementComponent):
    def __init__(self, rtype, args):
        IfcElementComponent.__init__(self, rtype, args)
        self.NominalDiameter = args.pop()
        self.NominalLength = args.pop()
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:NominalDiameter:{NominalDiameter}:NominalLength:{NominalLength}:PredefinedType:{PredefinedType}".format(
            sup=IfcElementComponent.__str__(self),
            NominalDiameter=self.NominalDiameter,
            NominalLength=self.NominalLength,
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcElementComponent.__json__(self)
        attrs = {'NominalDiameter': self.NominalDiameter, 'NominalLength': self.NominalLength,
                 'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMechanicalFastenerType(IfcElementComponentType):
    def __init__(self, rtype, args):
        IfcElementComponentType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.NominalDiameter = args.pop()
        self.NominalLength = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:NominalDiameter:{NominalDiameter}:NominalLength:{NominalLength}".format(
            sup=IfcElementComponentType.__str__(self),
            PredefinedType=self.PredefinedType,
            NominalDiameter=self.NominalDiameter,
            NominalLength=self.NominalLength,
        )

    def __json__(self):
        sup = IfcElementComponentType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'NominalDiameter': self.NominalDiameter,
                 'NominalLength': self.NominalLength}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMedicalDeviceType(IfcFlowTerminalType):
    def __init__(self, rtype, args):
        IfcFlowTerminalType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminalType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminalType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMemberType(IfcBuildingElementType):
    def __init__(self, rtype, args):
        IfcBuildingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMotorConnectionType(IfcEnergyConversionDeviceType):
    def __init__(self, rtype, args):
        IfcEnergyConversionDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcOccupant(IfcActor):
    def __init__(self, rtype, args):
        IfcActor.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcActor.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcActor.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcOpeningElement(IfcFeatureElementSubtraction):
    def __init__(self, rtype, args):
        IfcFeatureElementSubtraction.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFeatureElementSubtraction.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFeatureElementSubtraction.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcOpeningStandardCase(IfcOpeningElement):
    def __init__(self, rtype, args):
        IfcOpeningElement.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcOpeningElement.__str__(self),
        )

    def __json__(self):
        sup = IfcOpeningElement.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcOutletType(IfcFlowTerminalType):
    def __init__(self, rtype, args):
        IfcFlowTerminalType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminalType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminalType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPerformanceHistory(IfcControl):
    def __init__(self, rtype, args):
        IfcControl.__init__(self, rtype, args)
        self.LifeCyclePhase = args.pop()
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:LifeCyclePhase:{LifeCyclePhase}:PredefinedType:{PredefinedType}".format(
            sup=IfcControl.__str__(self),
            LifeCyclePhase=self.LifeCyclePhase,
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcControl.__json__(self)
        attrs = {'LifeCyclePhase': self.LifeCyclePhase, 'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPermeableCoveringProperties(IfcPreDefinedPropertySet):
    def __init__(self, rtype, args):
        IfcPreDefinedPropertySet.__init__(self, rtype, args)
        self.OperationType = args.pop()
        self.PanelPosition = args.pop()
        self.FrameDepth = args.pop()
        self.FrameThickness = args.pop()
        self.ShapeAspectStyle = args.pop()

    def __str__(self):
        return "{sup}:OperationType:{OperationType}:PanelPosition:{PanelPosition}:FrameDepth:{FrameDepth}:FrameThickness:{FrameThickness}:ShapeAspectStyle:{ShapeAspectStyle}".format(
            sup=IfcPreDefinedPropertySet.__str__(self),
            OperationType=self.OperationType,
            PanelPosition=self.PanelPosition,
            FrameDepth=self.FrameDepth,
            FrameThickness=self.FrameThickness,
            ShapeAspectStyle=self.ShapeAspectStyle,
        )

    def __json__(self):
        sup = IfcPreDefinedPropertySet.__json__(self)
        attrs = {'OperationType': self.OperationType, 'PanelPosition': self.PanelPosition,
                 'FrameDepth': self.FrameDepth, 'FrameThickness': self.FrameThickness,
                 'ShapeAspectStyle': self.ShapeAspectStyle}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPermit(IfcControl):
    def __init__(self, rtype, args):
        IfcControl.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.Status = args.pop()
        self.LongDescription = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:Status:{Status}:LongDescription:{LongDescription}".format(
            sup=IfcControl.__str__(self),
            PredefinedType=self.PredefinedType,
            Status=self.Status,
            LongDescription=self.LongDescription,
        )

    def __json__(self):
        sup = IfcControl.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'Status': self.Status, 'LongDescription': self.LongDescription}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPileType(IfcBuildingElementType):
    def __init__(self, rtype, args):
        IfcBuildingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPipeFittingType(IfcFlowFittingType):
    def __init__(self, rtype, args):
        IfcFlowFittingType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowFittingType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowFittingType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPipeSegmentType(IfcFlowSegmentType):
    def __init__(self, rtype, args):
        IfcFlowSegmentType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowSegmentType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowSegmentType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPlateType(IfcBuildingElementType):
    def __init__(self, rtype, args):
        IfcBuildingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPolygonalFaceSet(IfcTessellatedFaceSet):
    def __init__(self, rtype, args):
        IfcTessellatedFaceSet.__init__(self, rtype, args)
        self.Closed = args.pop()
        self.Faces = args.pop()
        self.PnIndex = args.pop()

    def __str__(self):
        return "{sup}:Closed:{Closed}:Faces:{Faces}:PnIndex:{PnIndex}".format(
            sup=IfcTessellatedFaceSet.__str__(self),
            Closed=self.Closed,
            Faces=self.Faces,
            PnIndex=self.PnIndex,
        )

    def __json__(self):
        sup = IfcTessellatedFaceSet.__json__(self)
        attrs = {'Closed': self.Closed, 'Faces': self.Faces, 'PnIndex': self.PnIndex}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPolyline(IfcBoundedCurve):
    def __init__(self, rtype, args):
        IfcBoundedCurve.__init__(self, rtype, args)
        self.Points = args.pop()

    def __str__(self):
        return "{sup}:Points:{Points}".format(
            sup=IfcBoundedCurve.__str__(self),
            Points=self.Points,
        )

    def __json__(self):
        sup = IfcBoundedCurve.__json__(self)
        attrs = {'Points': self.Points}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcPort(IfcProduct):
    def __init__(self, rtype, args):
        IfcProduct.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcProduct.__str__(self),
        )

    def __json__(self):
        sup = IfcProduct.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcPositioningElement(IfcProduct):
    def __init__(self, rtype, args):
        IfcProduct.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcProduct.__str__(self),
        )

    def __json__(self):
        sup = IfcProduct.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcProcedure(IfcProcess):
    def __init__(self, rtype, args):
        IfcProcess.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcProcess.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcProcess.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcProjectOrder(IfcControl):
    def __init__(self, rtype, args):
        IfcControl.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.Status = args.pop()
        self.LongDescription = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:Status:{Status}:LongDescription:{LongDescription}".format(
            sup=IfcControl.__str__(self),
            PredefinedType=self.PredefinedType,
            Status=self.Status,
            LongDescription=self.LongDescription,
        )

    def __json__(self):
        sup = IfcControl.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'Status': self.Status, 'LongDescription': self.LongDescription}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcProjectionElement(IfcFeatureElementAddition):
    def __init__(self, rtype, args):
        IfcFeatureElementAddition.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFeatureElementAddition.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFeatureElementAddition.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcProtectiveDeviceType(IfcFlowControllerType):
    def __init__(self, rtype, args):
        IfcFlowControllerType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowControllerType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowControllerType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPumpType(IfcFlowMovingDeviceType):
    def __init__(self, rtype, args):
        IfcFlowMovingDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowMovingDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowMovingDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRailingType(IfcBuildingElementType):
    def __init__(self, rtype, args):
        IfcBuildingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRampFlightType(IfcBuildingElementType):
    def __init__(self, rtype, args):
        IfcBuildingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRampType(IfcBuildingElementType):
    def __init__(self, rtype, args):
        IfcBuildingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRationalBSplineSurfaceWithKnots(IfcBSplineSurfaceWithKnots):
    def __init__(self, rtype, args):
        IfcBSplineSurfaceWithKnots.__init__(self, rtype, args)
        self.WeightsData = args.pop()

    def __str__(self):
        return "{sup}:WeightsData:{WeightsData}".format(
            sup=IfcBSplineSurfaceWithKnots.__str__(self),
            WeightsData=self.WeightsData,
        )

    def __json__(self):
        sup = IfcBSplineSurfaceWithKnots.__json__(self)
        attrs = {'WeightsData': self.WeightsData}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcReferent(IfcPositioningElement):
    def __init__(self, rtype, args):
        IfcPositioningElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.RestartDistance = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:RestartDistance:{RestartDistance}".format(
            sup=IfcPositioningElement.__str__(self),
            PredefinedType=self.PredefinedType,
            RestartDistance=self.RestartDistance,
        )

    def __json__(self):
        sup = IfcPositioningElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'RestartDistance': self.RestartDistance}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcReinforcingElement(IfcElementComponent):
    def __init__(self, rtype, args):
        IfcElementComponent.__init__(self, rtype, args)
        self.SteelGrade = args.pop()

    def __str__(self):
        return "{sup}:SteelGrade:{SteelGrade}".format(
            sup=IfcElementComponent.__str__(self),
            SteelGrade=self.SteelGrade,
        )

    def __json__(self):
        sup = IfcElementComponent.__json__(self)
        attrs = {'SteelGrade': self.SteelGrade}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcReinforcingElementType(IfcElementComponentType):
    def __init__(self, rtype, args):
        IfcElementComponentType.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcElementComponentType.__str__(self),
        )

    def __json__(self):
        sup = IfcElementComponentType.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcReinforcingMesh(IfcReinforcingElement):
    def __init__(self, rtype, args):
        IfcReinforcingElement.__init__(self, rtype, args)
        self.MeshLength = args.pop()
        self.MeshWidth = args.pop()
        self.LongitudinalBarNominalDiameter = args.pop()
        self.TransverseBarNominalDiameter = args.pop()
        self.LongitudinalBarCrossSectionArea = args.pop()
        self.TransverseBarCrossSectionArea = args.pop()
        self.LongitudinalBarSpacing = args.pop()
        self.TransverseBarSpacing = args.pop()
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:MeshLength:{MeshLength}:MeshWidth:{MeshWidth}:LongitudinalBarNominalDiameter:{LongitudinalBarNominalDiameter}:TransverseBarNominalDiameter:{TransverseBarNominalDiameter}:LongitudinalBarCrossSectionArea:{LongitudinalBarCrossSectionArea}:TransverseBarCrossSectionArea:{TransverseBarCrossSectionArea}:LongitudinalBarSpacing:{LongitudinalBarSpacing}:TransverseBarSpacing:{TransverseBarSpacing}:PredefinedType:{PredefinedType}".format(
            sup=IfcReinforcingElement.__str__(self),
            MeshLength=self.MeshLength,
            MeshWidth=self.MeshWidth,
            LongitudinalBarNominalDiameter=self.LongitudinalBarNominalDiameter,
            TransverseBarNominalDiameter=self.TransverseBarNominalDiameter,
            LongitudinalBarCrossSectionArea=self.LongitudinalBarCrossSectionArea,
            TransverseBarCrossSectionArea=self.TransverseBarCrossSectionArea,
            LongitudinalBarSpacing=self.LongitudinalBarSpacing,
            TransverseBarSpacing=self.TransverseBarSpacing,
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcReinforcingElement.__json__(self)
        attrs = {'MeshLength': self.MeshLength, 'MeshWidth': self.MeshWidth,
                 'LongitudinalBarNominalDiameter': self.LongitudinalBarNominalDiameter,
                 'TransverseBarNominalDiameter': self.TransverseBarNominalDiameter,
                 'LongitudinalBarCrossSectionArea': self.LongitudinalBarCrossSectionArea,
                 'TransverseBarCrossSectionArea': self.TransverseBarCrossSectionArea,
                 'LongitudinalBarSpacing': self.LongitudinalBarSpacing,
                 'TransverseBarSpacing': self.TransverseBarSpacing, 'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcReinforcingMeshType(IfcReinforcingElementType):
    def __init__(self, rtype, args):
        IfcReinforcingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.MeshLength = args.pop()
        self.MeshWidth = args.pop()
        self.LongitudinalBarNominalDiameter = args.pop()
        self.TransverseBarNominalDiameter = args.pop()
        self.LongitudinalBarCrossSectionArea = args.pop()
        self.TransverseBarCrossSectionArea = args.pop()
        self.LongitudinalBarSpacing = args.pop()
        self.TransverseBarSpacing = args.pop()
        self.BendingShapeCode = args.pop()
        self.BendingParameters = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:MeshLength:{MeshLength}:MeshWidth:{MeshWidth}:LongitudinalBarNominalDiameter:{LongitudinalBarNominalDiameter}:TransverseBarNominalDiameter:{TransverseBarNominalDiameter}:LongitudinalBarCrossSectionArea:{LongitudinalBarCrossSectionArea}:TransverseBarCrossSectionArea:{TransverseBarCrossSectionArea}:LongitudinalBarSpacing:{LongitudinalBarSpacing}:TransverseBarSpacing:{TransverseBarSpacing}:BendingShapeCode:{BendingShapeCode}:BendingParameters:{BendingParameters}".format(
            sup=IfcReinforcingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
            MeshLength=self.MeshLength,
            MeshWidth=self.MeshWidth,
            LongitudinalBarNominalDiameter=self.LongitudinalBarNominalDiameter,
            TransverseBarNominalDiameter=self.TransverseBarNominalDiameter,
            LongitudinalBarCrossSectionArea=self.LongitudinalBarCrossSectionArea,
            TransverseBarCrossSectionArea=self.TransverseBarCrossSectionArea,
            LongitudinalBarSpacing=self.LongitudinalBarSpacing,
            TransverseBarSpacing=self.TransverseBarSpacing,
            BendingShapeCode=self.BendingShapeCode,
            BendingParameters=self.BendingParameters,
        )

    def __json__(self):
        sup = IfcReinforcingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'MeshLength': self.MeshLength, 'MeshWidth': self.MeshWidth,
                 'LongitudinalBarNominalDiameter': self.LongitudinalBarNominalDiameter,
                 'TransverseBarNominalDiameter': self.TransverseBarNominalDiameter,
                 'LongitudinalBarCrossSectionArea': self.LongitudinalBarCrossSectionArea,
                 'TransverseBarCrossSectionArea': self.TransverseBarCrossSectionArea,
                 'LongitudinalBarSpacing': self.LongitudinalBarSpacing,
                 'TransverseBarSpacing': self.TransverseBarSpacing, 'BendingShapeCode': self.BendingShapeCode,
                 'BendingParameters': self.BendingParameters}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRelAggregates(IfcRelDecomposes):
    def __init__(self, rtype, args):
        IfcRelDecomposes.__init__(self, rtype, args)
        self.RelatingObject = args.pop()
        self.RelatedObjects = args.pop()

    def __str__(self):
        return "{sup}:RelatingObject:{RelatingObject}:RelatedObjects:{RelatedObjects}".format(
            sup=IfcRelDecomposes.__str__(self),
            RelatingObject=self.RelatingObject,
            RelatedObjects=self.RelatedObjects,
        )

    def __json__(self):
        sup = IfcRelDecomposes.__json__(self)
        attrs = {'RelatingObject': self.RelatingObject, 'RelatedObjects': self.RelatedObjects}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRoofType(IfcBuildingElementType):
    def __init__(self, rtype, args):
        IfcBuildingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSanitaryTerminalType(IfcFlowTerminalType):
    def __init__(self, rtype, args):
        IfcFlowTerminalType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminalType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminalType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSeamCurve(IfcSurfaceCurve):
    def __init__(self, rtype, args):
        IfcSurfaceCurve.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcSurfaceCurve.__str__(self),
        )

    def __json__(self):
        sup = IfcSurfaceCurve.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcShadingDeviceType(IfcBuildingElementType):
    def __init__(self, rtype, args):
        IfcBuildingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSite(IfcSpatialStructureElement):
    def __init__(self, rtype, args):
        IfcSpatialStructureElement.__init__(self, rtype, args)
        self.RefLatitude = args.pop()
        self.RefLongitude = args.pop()
        self.RefElevation = args.pop()
        self.LandTitleNumber = args.pop()
        self.SiteAddress = args.pop()

    def __str__(self):
        return "{sup}:RefLatitude:{RefLatitude}:RefLongitude:{RefLongitude}:RefElevation:{RefElevation}:LandTitleNumber:{LandTitleNumber}:SiteAddress:{SiteAddress}".format(
            sup=IfcSpatialStructureElement.__str__(self),
            RefLatitude=self.RefLatitude,
            RefLongitude=self.RefLongitude,
            RefElevation=self.RefElevation,
            LandTitleNumber=self.LandTitleNumber,
            SiteAddress=self.SiteAddress,
        )

    def __json__(self):
        sup = IfcSpatialStructureElement.__json__(self)
        attrs = {'RefLatitude': self.RefLatitude, 'RefLongitude': self.RefLongitude, 'RefElevation': self.RefElevation,
                 'LandTitleNumber': self.LandTitleNumber, 'SiteAddress': self.SiteAddress}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSlabType(IfcBuildingElementType):
    def __init__(self, rtype, args):
        IfcBuildingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSolarDeviceType(IfcEnergyConversionDeviceType):
    def __init__(self, rtype, args):
        IfcEnergyConversionDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSpace(IfcSpatialStructureElement):
    def __init__(self, rtype, args):
        IfcSpatialStructureElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.ElevationWithFlooring = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:ElevationWithFlooring:{ElevationWithFlooring}".format(
            sup=IfcSpatialStructureElement.__str__(self),
            PredefinedType=self.PredefinedType,
            ElevationWithFlooring=self.ElevationWithFlooring,
        )

    def __json__(self):
        sup = IfcSpatialStructureElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'ElevationWithFlooring': self.ElevationWithFlooring}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSpaceHeaterType(IfcFlowTerminalType):
    def __init__(self, rtype, args):
        IfcFlowTerminalType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminalType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminalType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSpaceType(IfcSpatialStructureElementType):
    def __init__(self, rtype, args):
        IfcSpatialStructureElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.LongName = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:LongName:{LongName}".format(
            sup=IfcSpatialStructureElementType.__str__(self),
            PredefinedType=self.PredefinedType,
            LongName=self.LongName,
        )

    def __json__(self):
        sup = IfcSpatialStructureElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'LongName': self.LongName}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStackTerminalType(IfcFlowTerminalType):
    def __init__(self, rtype, args):
        IfcFlowTerminalType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminalType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminalType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStairFlightType(IfcBuildingElementType):
    def __init__(self, rtype, args):
        IfcBuildingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStairType(IfcBuildingElementType):
    def __init__(self, rtype, args):
        IfcBuildingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcStructuralAction(IfcStructuralActivity):
    def __init__(self, rtype, args):
        IfcStructuralActivity.__init__(self, rtype, args)
        self.DestabilizingLoad = args.pop()

    def __str__(self):
        return "{sup}:DestabilizingLoad:{DestabilizingLoad}".format(
            sup=IfcStructuralActivity.__str__(self),
            DestabilizingLoad=self.DestabilizingLoad,
        )

    def __json__(self):
        sup = IfcStructuralActivity.__json__(self)
        attrs = {'DestabilizingLoad': self.DestabilizingLoad}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcStructuralConnection(IfcStructuralItem):
    def __init__(self, rtype, args):
        IfcStructuralItem.__init__(self, rtype, args)
        self.AppliedCondition = args.pop()

    def __str__(self):
        return "{sup}:AppliedCondition:{AppliedCondition}".format(
            sup=IfcStructuralItem.__str__(self),
            AppliedCondition=self.AppliedCondition,
        )

    def __json__(self):
        sup = IfcStructuralItem.__json__(self)
        attrs = {'AppliedCondition': self.AppliedCondition}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralCurveAction(IfcStructuralAction):
    def __init__(self, rtype, args):
        IfcStructuralAction.__init__(self, rtype, args)
        self.ProjectedOrTrue = args.pop()
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:ProjectedOrTrue:{ProjectedOrTrue}:PredefinedType:{PredefinedType}".format(
            sup=IfcStructuralAction.__str__(self),
            ProjectedOrTrue=self.ProjectedOrTrue,
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcStructuralAction.__json__(self)
        attrs = {'ProjectedOrTrue': self.ProjectedOrTrue, 'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralCurveConnection(IfcStructuralConnection):
    def __init__(self, rtype, args):
        IfcStructuralConnection.__init__(self, rtype, args)
        self.Axis = args.pop()

    def __str__(self):
        return "{sup}:Axis:{Axis}".format(
            sup=IfcStructuralConnection.__str__(self),
            Axis=self.Axis,
        )

    def __json__(self):
        sup = IfcStructuralConnection.__json__(self)
        attrs = {'Axis': self.Axis}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralCurveMember(IfcStructuralMember):
    def __init__(self, rtype, args):
        IfcStructuralMember.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.Axis = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:Axis:{Axis}".format(
            sup=IfcStructuralMember.__str__(self),
            PredefinedType=self.PredefinedType,
            Axis=self.Axis,
        )

    def __json__(self):
        sup = IfcStructuralMember.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'Axis': self.Axis}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralCurveMemberVarying(IfcStructuralCurveMember):
    def __init__(self, rtype, args):
        IfcStructuralCurveMember.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcStructuralCurveMember.__str__(self),
        )

    def __json__(self):
        sup = IfcStructuralCurveMember.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralCurveReaction(IfcStructuralReaction):
    def __init__(self, rtype, args):
        IfcStructuralReaction.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcStructuralReaction.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcStructuralReaction.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralLinearAction(IfcStructuralCurveAction):
    def __init__(self, rtype, args):
        IfcStructuralCurveAction.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcStructuralCurveAction.__str__(self),
        )

    def __json__(self):
        sup = IfcStructuralCurveAction.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralLoadGroup(IfcGroup):
    def __init__(self, rtype, args):
        IfcGroup.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.ActionType = args.pop()
        self.ActionSource = args.pop()
        self.Coefficient = args.pop()
        self.Purpose = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:ActionType:{ActionType}:ActionSource:{ActionSource}:Coefficient:{Coefficient}:Purpose:{Purpose}".format(
            sup=IfcGroup.__str__(self),
            PredefinedType=self.PredefinedType,
            ActionType=self.ActionType,
            ActionSource=self.ActionSource,
            Coefficient=self.Coefficient,
            Purpose=self.Purpose,
        )

    def __json__(self):
        sup = IfcGroup.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'ActionType': self.ActionType,
                 'ActionSource': self.ActionSource, 'Coefficient': self.Coefficient, 'Purpose': self.Purpose}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralPointAction(IfcStructuralAction):
    def __init__(self, rtype, args):
        IfcStructuralAction.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcStructuralAction.__str__(self),
        )

    def __json__(self):
        sup = IfcStructuralAction.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralPointConnection(IfcStructuralConnection):
    def __init__(self, rtype, args):
        IfcStructuralConnection.__init__(self, rtype, args)
        self.ConditionCoordinateSystem = args.pop()

    def __str__(self):
        return "{sup}:ConditionCoordinateSystem:{ConditionCoordinateSystem}".format(
            sup=IfcStructuralConnection.__str__(self),
            ConditionCoordinateSystem=self.ConditionCoordinateSystem,
        )

    def __json__(self):
        sup = IfcStructuralConnection.__json__(self)
        attrs = {'ConditionCoordinateSystem': self.ConditionCoordinateSystem}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralPointReaction(IfcStructuralReaction):
    def __init__(self, rtype, args):
        IfcStructuralReaction.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcStructuralReaction.__str__(self),
        )

    def __json__(self):
        sup = IfcStructuralReaction.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralResultGroup(IfcGroup):
    def __init__(self, rtype, args):
        IfcGroup.__init__(self, rtype, args)
        self.TheoryType = args.pop()
        self.ResultForLoadGroup = args.pop()
        self.IsLinear = args.pop()

    def __str__(self):
        return "{sup}:TheoryType:{TheoryType}:ResultForLoadGroup:{ResultForLoadGroup}:IsLinear:{IsLinear}".format(
            sup=IfcGroup.__str__(self),
            TheoryType=self.TheoryType,
            ResultForLoadGroup=self.ResultForLoadGroup,
            IsLinear=self.IsLinear,
        )

    def __json__(self):
        sup = IfcGroup.__json__(self)
        attrs = {'TheoryType': self.TheoryType, 'ResultForLoadGroup': self.ResultForLoadGroup,
                 'IsLinear': self.IsLinear}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralSurfaceAction(IfcStructuralAction):
    def __init__(self, rtype, args):
        IfcStructuralAction.__init__(self, rtype, args)
        self.ProjectedOrTrue = args.pop()
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:ProjectedOrTrue:{ProjectedOrTrue}:PredefinedType:{PredefinedType}".format(
            sup=IfcStructuralAction.__str__(self),
            ProjectedOrTrue=self.ProjectedOrTrue,
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcStructuralAction.__json__(self)
        attrs = {'ProjectedOrTrue': self.ProjectedOrTrue, 'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralSurfaceConnection(IfcStructuralConnection):
    def __init__(self, rtype, args):
        IfcStructuralConnection.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcStructuralConnection.__str__(self),
        )

    def __json__(self):
        sup = IfcStructuralConnection.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSubContractResource(IfcConstructionResource):
    def __init__(self, rtype, args):
        IfcConstructionResource.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcConstructionResource.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcConstructionResource.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSurfaceFeature(IfcFeatureElement):
    def __init__(self, rtype, args):
        IfcFeatureElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFeatureElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFeatureElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSwitchingDeviceType(IfcFlowControllerType):
    def __init__(self, rtype, args):
        IfcFlowControllerType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowControllerType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowControllerType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSystem(IfcGroup):
    def __init__(self, rtype, args):
        IfcGroup.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcGroup.__str__(self),
        )

    def __json__(self):
        sup = IfcGroup.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSystemFurnitureElement(IfcFurnishingElement):
    def __init__(self, rtype, args):
        IfcFurnishingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFurnishingElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFurnishingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTankType(IfcFlowStorageDeviceType):
    def __init__(self, rtype, args):
        IfcFlowStorageDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowStorageDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowStorageDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTendon(IfcReinforcingElement):
    def __init__(self, rtype, args):
        IfcReinforcingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.NominalDiameter = args.pop()
        self.CrossSectionArea = args.pop()
        self.TensionForce = args.pop()
        self.PreStress = args.pop()
        self.FrictionCoefficient = args.pop()
        self.AnchorageSlip = args.pop()
        self.MinCurvatureRadius = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:NominalDiameter:{NominalDiameter}:CrossSectionArea:{CrossSectionArea}:TensionForce:{TensionForce}:PreStress:{PreStress}:FrictionCoefficient:{FrictionCoefficient}:AnchorageSlip:{AnchorageSlip}:MinCurvatureRadius:{MinCurvatureRadius}".format(
            sup=IfcReinforcingElement.__str__(self),
            PredefinedType=self.PredefinedType,
            NominalDiameter=self.NominalDiameter,
            CrossSectionArea=self.CrossSectionArea,
            TensionForce=self.TensionForce,
            PreStress=self.PreStress,
            FrictionCoefficient=self.FrictionCoefficient,
            AnchorageSlip=self.AnchorageSlip,
            MinCurvatureRadius=self.MinCurvatureRadius,
        )

    def __json__(self):
        sup = IfcReinforcingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'NominalDiameter': self.NominalDiameter,
                 'CrossSectionArea': self.CrossSectionArea, 'TensionForce': self.TensionForce,
                 'PreStress': self.PreStress, 'FrictionCoefficient': self.FrictionCoefficient,
                 'AnchorageSlip': self.AnchorageSlip, 'MinCurvatureRadius': self.MinCurvatureRadius}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTendonAnchor(IfcReinforcingElement):
    def __init__(self, rtype, args):
        IfcReinforcingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcReinforcingElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcReinforcingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTendonAnchorType(IfcReinforcingElementType):
    def __init__(self, rtype, args):
        IfcReinforcingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcReinforcingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcReinforcingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTendonType(IfcReinforcingElementType):
    def __init__(self, rtype, args):
        IfcReinforcingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.NominalDiameter = args.pop()
        self.CrossSectionArea = args.pop()
        self.SheathDiameter = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:NominalDiameter:{NominalDiameter}:CrossSectionArea:{CrossSectionArea}:SheathDiameter:{SheathDiameter}".format(
            sup=IfcReinforcingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
            NominalDiameter=self.NominalDiameter,
            CrossSectionArea=self.CrossSectionArea,
            SheathDiameter=self.SheathDiameter,
        )

    def __json__(self):
        sup = IfcReinforcingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'NominalDiameter': self.NominalDiameter,
                 'CrossSectionArea': self.CrossSectionArea, 'SheathDiameter': self.SheathDiameter}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTransformerType(IfcEnergyConversionDeviceType):
    def __init__(self, rtype, args):
        IfcEnergyConversionDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTransitionCurveSegment2D(IfcCurveSegment2D):
    def __init__(self, rtype, args):
        IfcCurveSegment2D.__init__(self, rtype, args)
        self.StartRadius = args.pop()
        self.EndRadius = args.pop()
        self.IsStartRadiusCCW = args.pop()
        self.IsEndRadiusCCW = args.pop()
        self.TransitionCurveType = args.pop()

    def __str__(self):
        return "{sup}:StartRadius:{StartRadius}:EndRadius:{EndRadius}:IsStartRadiusCCW:{IsStartRadiusCCW}:IsEndRadiusCCW:{IsEndRadiusCCW}:TransitionCurveType:{TransitionCurveType}".format(
            sup=IfcCurveSegment2D.__str__(self),
            StartRadius=self.StartRadius,
            EndRadius=self.EndRadius,
            IsStartRadiusCCW=self.IsStartRadiusCCW,
            IsEndRadiusCCW=self.IsEndRadiusCCW,
            TransitionCurveType=self.TransitionCurveType,
        )

    def __json__(self):
        sup = IfcCurveSegment2D.__json__(self)
        attrs = {'StartRadius': self.StartRadius, 'EndRadius': self.EndRadius,
                 'IsStartRadiusCCW': self.IsStartRadiusCCW, 'IsEndRadiusCCW': self.IsEndRadiusCCW,
                 'TransitionCurveType': self.TransitionCurveType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTransportElement(IfcElement):
    def __init__(self, rtype, args):
        IfcElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTrimmedCurve(IfcBoundedCurve):
    def __init__(self, rtype, args):
        IfcBoundedCurve.__init__(self, rtype, args)
        self.BasisCurve = args.pop()
        self.Trim1 = args.pop()
        self.Trim2 = args.pop()
        self.SenseAgreement = args.pop()
        self.MasterRepresentation = args.pop()

    def __str__(self):
        return "{sup}:BasisCurve:{BasisCurve}:Trim1:{Trim1}:Trim2:{Trim2}:SenseAgreement:{SenseAgreement}:MasterRepresentation:{MasterRepresentation}".format(
            sup=IfcBoundedCurve.__str__(self),
            BasisCurve=self.BasisCurve,
            Trim1=self.Trim1,
            Trim2=self.Trim2,
            SenseAgreement=self.SenseAgreement,
            MasterRepresentation=self.MasterRepresentation,
        )

    def __json__(self):
        sup = IfcBoundedCurve.__json__(self)
        attrs = {'BasisCurve': self.BasisCurve, 'Trim1': self.Trim1, 'Trim2': self.Trim2,
                 'SenseAgreement': self.SenseAgreement, 'MasterRepresentation': self.MasterRepresentation}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTubeBundleType(IfcEnergyConversionDeviceType):
    def __init__(self, rtype, args):
        IfcEnergyConversionDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcUnitaryEquipmentType(IfcEnergyConversionDeviceType):
    def __init__(self, rtype, args):
        IfcEnergyConversionDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcValveType(IfcFlowControllerType):
    def __init__(self, rtype, args):
        IfcFlowControllerType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowControllerType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowControllerType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcVibrationIsolator(IfcElementComponent):
    def __init__(self, rtype, args):
        IfcElementComponent.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcElementComponent.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcElementComponent.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcVibrationIsolatorType(IfcElementComponentType):
    def __init__(self, rtype, args):
        IfcElementComponentType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcElementComponentType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcElementComponentType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcVirtualElement(IfcElement):
    def __init__(self, rtype, args):
        IfcElement.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcElement.__str__(self),
        )

    def __json__(self):
        sup = IfcElement.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcVoidingFeature(IfcFeatureElementSubtraction):
    def __init__(self, rtype, args):
        IfcFeatureElementSubtraction.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFeatureElementSubtraction.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFeatureElementSubtraction.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcWallType(IfcBuildingElementType):
    def __init__(self, rtype, args):
        IfcBuildingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcWasteTerminalType(IfcFlowTerminalType):
    def __init__(self, rtype, args):
        IfcFlowTerminalType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminalType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminalType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcWindowType(IfcBuildingElementType):
    def __init__(self, rtype, args):
        IfcBuildingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.PartitioningType = args.pop()
        self.ParameterTakesPrecedence = args.pop()
        self.UserDefinedPartitioningType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:PartitioningType:{PartitioningType}:ParameterTakesPrecedence:{ParameterTakesPrecedence}:UserDefinedPartitioningType:{UserDefinedPartitioningType}".format(
            sup=IfcBuildingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
            PartitioningType=self.PartitioningType,
            ParameterTakesPrecedence=self.ParameterTakesPrecedence,
            UserDefinedPartitioningType=self.UserDefinedPartitioningType,
        )

    def __json__(self):
        sup = IfcBuildingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'PartitioningType': self.PartitioningType,
                 'ParameterTakesPrecedence': self.ParameterTakesPrecedence,
                 'UserDefinedPartitioningType': self.UserDefinedPartitioningType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcWorkCalendar(IfcControl):
    def __init__(self, rtype, args):
        IfcControl.__init__(self, rtype, args)
        self.WorkingTimes = args.pop()
        self.ExceptionTimes = args.pop()
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:WorkingTimes:{WorkingTimes}:ExceptionTimes:{ExceptionTimes}:PredefinedType:{PredefinedType}".format(
            sup=IfcControl.__str__(self),
            WorkingTimes=self.WorkingTimes,
            ExceptionTimes=self.ExceptionTimes,
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcControl.__json__(self)
        attrs = {'WorkingTimes': self.WorkingTimes, 'ExceptionTimes': self.ExceptionTimes,
                 'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcWorkControl(IfcControl):
    def __init__(self, rtype, args):
        IfcControl.__init__(self, rtype, args)
        self.CreationDate = args.pop()
        self.Creators = args.pop()
        self.Purpose = args.pop()
        self.Duration = args.pop()
        self.TotalFloat = args.pop()
        self.StartTime = args.pop()
        self.FinishTime = args.pop()

    def __str__(self):
        return "{sup}:CreationDate:{CreationDate}:Creators:{Creators}:Purpose:{Purpose}:Duration:{Duration}:TotalFloat:{TotalFloat}:StartTime:{StartTime}:FinishTime:{FinishTime}".format(
            sup=IfcControl.__str__(self),
            CreationDate=self.CreationDate,
            Creators=self.Creators,
            Purpose=self.Purpose,
            Duration=self.Duration,
            TotalFloat=self.TotalFloat,
            StartTime=self.StartTime,
            FinishTime=self.FinishTime,
        )

    def __json__(self):
        sup = IfcControl.__json__(self)
        attrs = {'CreationDate': self.CreationDate, 'Creators': self.Creators, 'Purpose': self.Purpose,
                 'Duration': self.Duration, 'TotalFloat': self.TotalFloat, 'StartTime': self.StartTime,
                 'FinishTime': self.FinishTime}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcWorkPlan(IfcWorkControl):
    def __init__(self, rtype, args):
        IfcWorkControl.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcWorkControl.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcWorkControl.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcWorkSchedule(IfcWorkControl):
    def __init__(self, rtype, args):
        IfcWorkControl.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcWorkControl.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcWorkControl.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcZone(IfcSystem):
    def __init__(self, rtype, args):
        IfcSystem.__init__(self, rtype, args)
        self.LongName = args.pop()

    def __str__(self):
        return "{sup}:LongName:{LongName}".format(
            sup=IfcSystem.__str__(self),
            LongName=self.LongName,
        )

    def __json__(self):
        sup = IfcSystem.__json__(self)
        attrs = {'LongName': self.LongName}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcActionRequest(IfcControl):
    def __init__(self, rtype, args):
        IfcControl.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.Status = args.pop()
        self.LongDescription = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:Status:{Status}:LongDescription:{LongDescription}".format(
            sup=IfcControl.__str__(self),
            PredefinedType=self.PredefinedType,
            Status=self.Status,
            LongDescription=self.LongDescription,
        )

    def __json__(self):
        sup = IfcControl.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'Status': self.Status, 'LongDescription': self.LongDescription}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAirTerminalBoxType(IfcFlowControllerType):
    def __init__(self, rtype, args):
        IfcFlowControllerType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowControllerType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowControllerType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAirTerminalType(IfcFlowTerminalType):
    def __init__(self, rtype, args):
        IfcFlowTerminalType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminalType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminalType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAirToAirHeatRecoveryType(IfcEnergyConversionDeviceType):
    def __init__(self, rtype, args):
        IfcEnergyConversionDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAlignmentCurve(IfcBoundedCurve):
    def __init__(self, rtype, args):
        IfcBoundedCurve.__init__(self, rtype, args)
        self.Horizontal = args.pop()
        self.Vertical = args.pop()
        self.Tag = args.pop()

    def __str__(self):
        return "{sup}:Horizontal:{Horizontal}:Vertical:{Vertical}:Tag:{Tag}".format(
            sup=IfcBoundedCurve.__str__(self),
            Horizontal=self.Horizontal,
            Vertical=self.Vertical,
            Tag=self.Tag,
        )

    def __json__(self):
        sup = IfcBoundedCurve.__json__(self)
        attrs = {'Horizontal': self.Horizontal, 'Vertical': self.Vertical, 'Tag': self.Tag}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAsset(IfcGroup):
    def __init__(self, rtype, args):
        IfcGroup.__init__(self, rtype, args)
        self.Identification = args.pop()
        self.OriginalValue = args.pop()
        self.CurrentValue = args.pop()
        self.TotalReplacementCost = args.pop()
        self.Owner = args.pop()
        self.User = args.pop()
        self.ResponsiblePerson = args.pop()
        self.IncorporationDate = args.pop()
        self.DepreciatedValue = args.pop()

    def __str__(self):
        return "{sup}:Identification:{Identification}:OriginalValue:{OriginalValue}:CurrentValue:{CurrentValue}:TotalReplacementCost:{TotalReplacementCost}:Owner:{Owner}:User:{User}:ResponsiblePerson:{ResponsiblePerson}:IncorporationDate:{IncorporationDate}:DepreciatedValue:{DepreciatedValue}".format(
            sup=IfcGroup.__str__(self),
            Identification=self.Identification,
            OriginalValue=self.OriginalValue,
            CurrentValue=self.CurrentValue,
            TotalReplacementCost=self.TotalReplacementCost,
            Owner=self.Owner,
            User=self.User,
            ResponsiblePerson=self.ResponsiblePerson,
            IncorporationDate=self.IncorporationDate,
            DepreciatedValue=self.DepreciatedValue,
        )

    def __json__(self):
        sup = IfcGroup.__json__(self)
        attrs = {'Identification': self.Identification, 'OriginalValue': self.OriginalValue,
                 'CurrentValue': self.CurrentValue, 'TotalReplacementCost': self.TotalReplacementCost,
                 'Owner': self.Owner, 'User': self.User, 'ResponsiblePerson': self.ResponsiblePerson,
                 'IncorporationDate': self.IncorporationDate, 'DepreciatedValue': self.DepreciatedValue}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAudioVisualApplianceType(IfcFlowTerminalType):
    def __init__(self, rtype, args):
        IfcFlowTerminalType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminalType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminalType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcBSplineCurve(IfcBoundedCurve):
    def __init__(self, rtype, args):
        IfcBoundedCurve.__init__(self, rtype, args)
        self.Degree = args.pop()
        self.ControlPointsList = args.pop()
        self.CurveForm = args.pop()
        self.ClosedCurve = args.pop()
        self.SelfIntersect = args.pop()

    def __str__(self):
        return "{sup}:Degree:{Degree}:ControlPointsList:{ControlPointsList}:CurveForm:{CurveForm}:ClosedCurve:{ClosedCurve}:SelfIntersect:{SelfIntersect}".format(
            sup=IfcBoundedCurve.__str__(self),
            Degree=self.Degree,
            ControlPointsList=self.ControlPointsList,
            CurveForm=self.CurveForm,
            ClosedCurve=self.ClosedCurve,
            SelfIntersect=self.SelfIntersect,
        )

    def __json__(self):
        sup = IfcBoundedCurve.__json__(self)
        attrs = {'Degree': self.Degree, 'ControlPointsList': self.ControlPointsList, 'CurveForm': self.CurveForm,
                 'ClosedCurve': self.ClosedCurve, 'SelfIntersect': self.SelfIntersect}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBSplineCurveWithKnots(IfcBSplineCurve):
    def __init__(self, rtype, args):
        IfcBSplineCurve.__init__(self, rtype, args)
        self.KnotMultiplicities = args.pop()
        self.Knots = args.pop()
        self.KnotSpec = args.pop()

    def __str__(self):
        return "{sup}:KnotMultiplicities:{KnotMultiplicities}:Knots:{Knots}:KnotSpec:{KnotSpec}".format(
            sup=IfcBSplineCurve.__str__(self),
            KnotMultiplicities=self.KnotMultiplicities,
            Knots=self.Knots,
            KnotSpec=self.KnotSpec,
        )

    def __json__(self):
        sup = IfcBSplineCurve.__json__(self)
        attrs = {'KnotMultiplicities': self.KnotMultiplicities, 'Knots': self.Knots, 'KnotSpec': self.KnotSpec}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBeamType(IfcBuildingElementType):
    def __init__(self, rtype, args):
        IfcBuildingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBoilerType(IfcEnergyConversionDeviceType):
    def __init__(self, rtype, args):
        IfcEnergyConversionDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBoundaryCurve(IfcCompositeCurveOnSurface):
    def __init__(self, rtype, args):
        IfcCompositeCurveOnSurface.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcCompositeCurveOnSurface.__str__(self),
        )

    def __json__(self):
        sup = IfcCompositeCurveOnSurface.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcBuildingElement(IfcElement):
    def __init__(self, rtype, args):
        IfcElement.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcElement.__str__(self),
        )

    def __json__(self):
        sup = IfcElement.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBuildingElementPart(IfcElementComponent):
    def __init__(self, rtype, args):
        IfcElementComponent.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcElementComponent.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcElementComponent.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBuildingElementPartType(IfcElementComponentType):
    def __init__(self, rtype, args):
        IfcElementComponentType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcElementComponentType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcElementComponentType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBuildingElementProxy(IfcBuildingElement):
    def __init__(self, rtype, args):
        IfcBuildingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBuildingElementProxyType(IfcBuildingElementType):
    def __init__(self, rtype, args):
        IfcBuildingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBuildingSystem(IfcSystem):
    def __init__(self, rtype, args):
        IfcSystem.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.LongName = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:LongName:{LongName}".format(
            sup=IfcSystem.__str__(self),
            PredefinedType=self.PredefinedType,
            LongName=self.LongName,
        )

    def __json__(self):
        sup = IfcSystem.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'LongName': self.LongName}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBurnerType(IfcEnergyConversionDeviceType):
    def __init__(self, rtype, args):
        IfcEnergyConversionDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCableCarrierFittingType(IfcFlowFittingType):
    def __init__(self, rtype, args):
        IfcFlowFittingType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowFittingType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowFittingType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCableCarrierSegmentType(IfcFlowSegmentType):
    def __init__(self, rtype, args):
        IfcFlowSegmentType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowSegmentType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowSegmentType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCableFittingType(IfcFlowFittingType):
    def __init__(self, rtype, args):
        IfcFlowFittingType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowFittingType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowFittingType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCableSegmentType(IfcFlowSegmentType):
    def __init__(self, rtype, args):
        IfcFlowSegmentType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowSegmentType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowSegmentType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcChillerType(IfcEnergyConversionDeviceType):
    def __init__(self, rtype, args):
        IfcEnergyConversionDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcChimney(IfcBuildingElement):
    def __init__(self, rtype, args):
        IfcBuildingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCircle(IfcConic):
    def __init__(self, rtype, args):
        IfcConic.__init__(self, rtype, args)
        self.Radius = args.pop()

    def __str__(self):
        return "{sup}:Radius:{Radius}".format(
            sup=IfcConic.__str__(self),
            Radius=self.Radius,
        )

    def __json__(self):
        sup = IfcConic.__json__(self)
        attrs = {'Radius': self.Radius}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCircularArcSegment2D(IfcCurveSegment2D):
    def __init__(self, rtype, args):
        IfcCurveSegment2D.__init__(self, rtype, args)
        self.Radius = args.pop()
        self.IsCCW = args.pop()

    def __str__(self):
        return "{sup}:Radius:{Radius}:IsCCW:{IsCCW}".format(
            sup=IfcCurveSegment2D.__str__(self),
            Radius=self.Radius,
            IsCCW=self.IsCCW,
        )

    def __json__(self):
        sup = IfcCurveSegment2D.__json__(self)
        attrs = {'Radius': self.Radius, 'IsCCW': self.IsCCW}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCivilElement(IfcElement):
    def __init__(self, rtype, args):
        IfcElement.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcElement.__str__(self),
        )

    def __json__(self):
        sup = IfcElement.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCoilType(IfcEnergyConversionDeviceType):
    def __init__(self, rtype, args):
        IfcEnergyConversionDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcColumn(IfcBuildingElement):
    def __init__(self, rtype, args):
        IfcBuildingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcColumnStandardCase(IfcColumn):
    def __init__(self, rtype, args):
        IfcColumn.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcColumn.__str__(self),
        )

    def __json__(self):
        sup = IfcColumn.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCommunicationsApplianceType(IfcFlowTerminalType):
    def __init__(self, rtype, args):
        IfcFlowTerminalType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminalType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminalType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCompressorType(IfcFlowMovingDeviceType):
    def __init__(self, rtype, args):
        IfcFlowMovingDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowMovingDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowMovingDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCondenserType(IfcEnergyConversionDeviceType):
    def __init__(self, rtype, args):
        IfcEnergyConversionDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcConstructionEquipmentResource(IfcConstructionResource):
    def __init__(self, rtype, args):
        IfcConstructionResource.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcConstructionResource.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcConstructionResource.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcConstructionMaterialResource(IfcConstructionResource):
    def __init__(self, rtype, args):
        IfcConstructionResource.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcConstructionResource.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcConstructionResource.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcConstructionProductResource(IfcConstructionResource):
    def __init__(self, rtype, args):
        IfcConstructionResource.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcConstructionResource.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcConstructionResource.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCooledBeamType(IfcEnergyConversionDeviceType):
    def __init__(self, rtype, args):
        IfcEnergyConversionDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCoolingTowerType(IfcEnergyConversionDeviceType):
    def __init__(self, rtype, args):
        IfcEnergyConversionDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCovering(IfcBuildingElement):
    def __init__(self, rtype, args):
        IfcBuildingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCurtainWall(IfcBuildingElement):
    def __init__(self, rtype, args):
        IfcBuildingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDamperType(IfcFlowControllerType):
    def __init__(self, rtype, args):
        IfcFlowControllerType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowControllerType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowControllerType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDiscreteAccessory(IfcElementComponent):
    def __init__(self, rtype, args):
        IfcElementComponent.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcElementComponent.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcElementComponent.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDiscreteAccessoryType(IfcElementComponentType):
    def __init__(self, rtype, args):
        IfcElementComponentType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcElementComponentType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcElementComponentType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDistributionChamberElementType(IfcDistributionFlowElementType):
    def __init__(self, rtype, args):
        IfcDistributionFlowElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcDistributionFlowElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcDistributionFlowElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcDistributionControlElementType(IfcDistributionElementType):
    def __init__(self, rtype, args):
        IfcDistributionElementType.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDistributionElementType.__str__(self),
        )

    def __json__(self):
        sup = IfcDistributionElementType.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDistributionElement(IfcElement):
    def __init__(self, rtype, args):
        IfcElement.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcElement.__str__(self),
        )

    def __json__(self):
        sup = IfcElement.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDistributionFlowElement(IfcDistributionElement):
    def __init__(self, rtype, args):
        IfcDistributionElement.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDistributionElement.__str__(self),
        )

    def __json__(self):
        sup = IfcDistributionElement.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDistributionPort(IfcPort):
    def __init__(self, rtype, args):
        IfcPort.__init__(self, rtype, args)
        self.FlowDirection = args.pop()
        self.PredefinedType = args.pop()
        self.SystemType = args.pop()

    def __str__(self):
        return "{sup}:FlowDirection:{FlowDirection}:PredefinedType:{PredefinedType}:SystemType:{SystemType}".format(
            sup=IfcPort.__str__(self),
            FlowDirection=self.FlowDirection,
            PredefinedType=self.PredefinedType,
            SystemType=self.SystemType,
        )

    def __json__(self):
        sup = IfcPort.__json__(self)
        attrs = {'FlowDirection': self.FlowDirection, 'PredefinedType': self.PredefinedType,
                 'SystemType': self.SystemType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDistributionSystem(IfcSystem):
    def __init__(self, rtype, args):
        IfcSystem.__init__(self, rtype, args)
        self.LongName = args.pop()
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:LongName:{LongName}:PredefinedType:{PredefinedType}".format(
            sup=IfcSystem.__str__(self),
            LongName=self.LongName,
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcSystem.__json__(self)
        attrs = {'LongName': self.LongName, 'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDoor(IfcBuildingElement):
    def __init__(self, rtype, args):
        IfcBuildingElement.__init__(self, rtype, args)
        self.OverallHeight = args.pop()
        self.OverallWidth = args.pop()
        self.PredefinedType = args.pop()
        self.OperationType = args.pop()
        self.UserDefinedOperationType = args.pop()

    def __str__(self):
        return "{sup}:OverallHeight:{OverallHeight}:OverallWidth:{OverallWidth}:PredefinedType:{PredefinedType}:OperationType:{OperationType}:UserDefinedOperationType:{UserDefinedOperationType}".format(
            sup=IfcBuildingElement.__str__(self),
            OverallHeight=self.OverallHeight,
            OverallWidth=self.OverallWidth,
            PredefinedType=self.PredefinedType,
            OperationType=self.OperationType,
            UserDefinedOperationType=self.UserDefinedOperationType,
        )

    def __json__(self):
        sup = IfcBuildingElement.__json__(self)
        attrs = {'OverallHeight': self.OverallHeight, 'OverallWidth': self.OverallWidth,
                 'PredefinedType': self.PredefinedType, 'OperationType': self.OperationType,
                 'UserDefinedOperationType': self.UserDefinedOperationType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDoorStandardCase(IfcDoor):
    def __init__(self, rtype, args):
        IfcDoor.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDoor.__str__(self),
        )

    def __json__(self):
        sup = IfcDoor.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDuctFittingType(IfcFlowFittingType):
    def __init__(self, rtype, args):
        IfcFlowFittingType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowFittingType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowFittingType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDuctSegmentType(IfcFlowSegmentType):
    def __init__(self, rtype, args):
        IfcFlowSegmentType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowSegmentType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowSegmentType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDuctSilencerType(IfcFlowTreatmentDeviceType):
    def __init__(self, rtype, args):
        IfcFlowTreatmentDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTreatmentDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTreatmentDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcElectricApplianceType(IfcFlowTerminalType):
    def __init__(self, rtype, args):
        IfcFlowTerminalType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminalType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminalType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcElectricDistributionBoardType(IfcFlowControllerType):
    def __init__(self, rtype, args):
        IfcFlowControllerType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowControllerType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowControllerType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcElectricFlowStorageDeviceType(IfcFlowStorageDeviceType):
    def __init__(self, rtype, args):
        IfcFlowStorageDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowStorageDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowStorageDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcElectricGeneratorType(IfcEnergyConversionDeviceType):
    def __init__(self, rtype, args):
        IfcEnergyConversionDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcElectricMotorType(IfcEnergyConversionDeviceType):
    def __init__(self, rtype, args):
        IfcEnergyConversionDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcElectricTimeControlType(IfcFlowControllerType):
    def __init__(self, rtype, args):
        IfcFlowControllerType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowControllerType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowControllerType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcEnergyConversionDevice(IfcDistributionFlowElement):
    def __init__(self, rtype, args):
        IfcDistributionFlowElement.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDistributionFlowElement.__str__(self),
        )

    def __json__(self):
        sup = IfcDistributionFlowElement.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcEngine(IfcEnergyConversionDevice):
    def __init__(self, rtype, args):
        IfcEnergyConversionDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcEvaporativeCooler(IfcEnergyConversionDevice):
    def __init__(self, rtype, args):
        IfcEnergyConversionDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcEvaporator(IfcEnergyConversionDevice):
    def __init__(self, rtype, args):
        IfcEnergyConversionDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcExternalSpatialElement(IfcExternalSpatialStructureElement):
    def __init__(self, rtype, args):
        IfcExternalSpatialStructureElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcExternalSpatialStructureElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcExternalSpatialStructureElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFanType(IfcFlowMovingDeviceType):
    def __init__(self, rtype, args):
        IfcFlowMovingDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowMovingDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowMovingDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFilterType(IfcFlowTreatmentDeviceType):
    def __init__(self, rtype, args):
        IfcFlowTreatmentDeviceType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTreatmentDeviceType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTreatmentDeviceType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFireSuppressionTerminalType(IfcFlowTerminalType):
    def __init__(self, rtype, args):
        IfcFlowTerminalType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminalType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminalType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFlowController(IfcDistributionFlowElement):
    def __init__(self, rtype, args):
        IfcDistributionFlowElement.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDistributionFlowElement.__str__(self),
        )

    def __json__(self):
        sup = IfcDistributionFlowElement.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFlowFitting(IfcDistributionFlowElement):
    def __init__(self, rtype, args):
        IfcDistributionFlowElement.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDistributionFlowElement.__str__(self),
        )

    def __json__(self):
        sup = IfcDistributionFlowElement.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFlowInstrumentType(IfcDistributionControlElementType):
    def __init__(self, rtype, args):
        IfcDistributionControlElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcDistributionControlElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcDistributionControlElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFlowMeter(IfcFlowController):
    def __init__(self, rtype, args):
        IfcFlowController.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowController.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowController.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFlowMovingDevice(IfcDistributionFlowElement):
    def __init__(self, rtype, args):
        IfcDistributionFlowElement.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDistributionFlowElement.__str__(self),
        )

    def __json__(self):
        sup = IfcDistributionFlowElement.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFlowSegment(IfcDistributionFlowElement):
    def __init__(self, rtype, args):
        IfcDistributionFlowElement.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDistributionFlowElement.__str__(self),
        )

    def __json__(self):
        sup = IfcDistributionFlowElement.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFlowStorageDevice(IfcDistributionFlowElement):
    def __init__(self, rtype, args):
        IfcDistributionFlowElement.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDistributionFlowElement.__str__(self),
        )

    def __json__(self):
        sup = IfcDistributionFlowElement.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFlowTerminal(IfcDistributionFlowElement):
    def __init__(self, rtype, args):
        IfcDistributionFlowElement.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDistributionFlowElement.__str__(self),
        )

    def __json__(self):
        sup = IfcDistributionFlowElement.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFlowTreatmentDevice(IfcDistributionFlowElement):
    def __init__(self, rtype, args):
        IfcDistributionFlowElement.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDistributionFlowElement.__str__(self),
        )

    def __json__(self):
        sup = IfcDistributionFlowElement.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFooting(IfcBuildingElement):
    def __init__(self, rtype, args):
        IfcBuildingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcGrid(IfcPositioningElement):
    def __init__(self, rtype, args):
        IfcPositioningElement.__init__(self, rtype, args)
        self.UAxes = args.pop()
        self.VAxes = args.pop()
        self.WAxes = args.pop()
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:UAxes:{UAxes}:VAxes:{VAxes}:WAxes:{WAxes}:PredefinedType:{PredefinedType}".format(
            sup=IfcPositioningElement.__str__(self),
            UAxes=self.UAxes,
            VAxes=self.VAxes,
            WAxes=self.WAxes,
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcPositioningElement.__json__(self)
        attrs = {'UAxes': self.UAxes, 'VAxes': self.VAxes, 'WAxes': self.WAxes, 'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcHeatExchanger(IfcEnergyConversionDevice):
    def __init__(self, rtype, args):
        IfcEnergyConversionDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcHumidifier(IfcEnergyConversionDevice):
    def __init__(self, rtype, args):
        IfcEnergyConversionDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcInterceptor(IfcFlowTreatmentDevice):
    def __init__(self, rtype, args):
        IfcFlowTreatmentDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTreatmentDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTreatmentDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcJunctionBox(IfcFlowFitting):
    def __init__(self, rtype, args):
        IfcFlowFitting.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowFitting.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowFitting.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLamp(IfcFlowTerminal):
    def __init__(self, rtype, args):
        IfcFlowTerminal.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminal.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminal.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcLightFixture(IfcFlowTerminal):
    def __init__(self, rtype, args):
        IfcFlowTerminal.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminal.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminal.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_abstract_class
class IfcLinearPositioningElement(IfcPositioningElement):
    def __init__(self, rtype, args):
        IfcPositioningElement.__init__(self, rtype, args)
        self.Axis = args.pop()

    def __str__(self):
        return "{sup}:Axis:{Axis}".format(
            sup=IfcPositioningElement.__str__(self),
            Axis=self.Axis,
        )

    def __json__(self):
        sup = IfcPositioningElement.__json__(self)
        attrs = {'Axis': self.Axis}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMedicalDevice(IfcFlowTerminal):
    def __init__(self, rtype, args):
        IfcFlowTerminal.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminal.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminal.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMember(IfcBuildingElement):
    def __init__(self, rtype, args):
        IfcBuildingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMemberStandardCase(IfcMember):
    def __init__(self, rtype, args):
        IfcMember.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcMember.__str__(self),
        )

    def __json__(self):
        sup = IfcMember.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcMotorConnection(IfcEnergyConversionDevice):
    def __init__(self, rtype, args):
        IfcEnergyConversionDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcOuterBoundaryCurve(IfcBoundaryCurve):
    def __init__(self, rtype, args):
        IfcBoundaryCurve.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcBoundaryCurve.__str__(self),
        )

    def __json__(self):
        sup = IfcBoundaryCurve.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcOutlet(IfcFlowTerminal):
    def __init__(self, rtype, args):
        IfcFlowTerminal.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminal.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminal.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPile(IfcBuildingElement):
    def __init__(self, rtype, args):
        IfcBuildingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.ConstructionType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:ConstructionType:{ConstructionType}".format(
            sup=IfcBuildingElement.__str__(self),
            PredefinedType=self.PredefinedType,
            ConstructionType=self.ConstructionType,
        )

    def __json__(self):
        sup = IfcBuildingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'ConstructionType': self.ConstructionType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPipeFitting(IfcFlowFitting):
    def __init__(self, rtype, args):
        IfcFlowFitting.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowFitting.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowFitting.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPipeSegment(IfcFlowSegment):
    def __init__(self, rtype, args):
        IfcFlowSegment.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowSegment.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowSegment.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPlate(IfcBuildingElement):
    def __init__(self, rtype, args):
        IfcBuildingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPlateStandardCase(IfcPlate):
    def __init__(self, rtype, args):
        IfcPlate.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcPlate.__str__(self),
        )

    def __json__(self):
        sup = IfcPlate.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcProtectiveDevice(IfcFlowController):
    def __init__(self, rtype, args):
        IfcFlowController.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowController.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowController.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcProtectiveDeviceTrippingUnitType(IfcDistributionControlElementType):
    def __init__(self, rtype, args):
        IfcDistributionControlElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcDistributionControlElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcDistributionControlElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcPump(IfcFlowMovingDevice):
    def __init__(self, rtype, args):
        IfcFlowMovingDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowMovingDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowMovingDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRailing(IfcBuildingElement):
    def __init__(self, rtype, args):
        IfcBuildingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRamp(IfcBuildingElement):
    def __init__(self, rtype, args):
        IfcBuildingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRampFlight(IfcBuildingElement):
    def __init__(self, rtype, args):
        IfcBuildingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRationalBSplineCurveWithKnots(IfcBSplineCurveWithKnots):
    def __init__(self, rtype, args):
        IfcBSplineCurveWithKnots.__init__(self, rtype, args)
        self.WeightsData = args.pop()

    def __str__(self):
        return "{sup}:WeightsData:{WeightsData}".format(
            sup=IfcBSplineCurveWithKnots.__str__(self),
            WeightsData=self.WeightsData,
        )

    def __json__(self):
        sup = IfcBSplineCurveWithKnots.__json__(self)
        attrs = {'WeightsData': self.WeightsData}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcReinforcingBar(IfcReinforcingElement):
    def __init__(self, rtype, args):
        IfcReinforcingElement.__init__(self, rtype, args)
        self.NominalDiameter = args.pop()
        self.CrossSectionArea = args.pop()
        self.BarLength = args.pop()
        self.PredefinedType = args.pop()
        self.BarSurface = args.pop()

    def __str__(self):
        return "{sup}:NominalDiameter:{NominalDiameter}:CrossSectionArea:{CrossSectionArea}:BarLength:{BarLength}:PredefinedType:{PredefinedType}:BarSurface:{BarSurface}".format(
            sup=IfcReinforcingElement.__str__(self),
            NominalDiameter=self.NominalDiameter,
            CrossSectionArea=self.CrossSectionArea,
            BarLength=self.BarLength,
            PredefinedType=self.PredefinedType,
            BarSurface=self.BarSurface,
        )

    def __json__(self):
        sup = IfcReinforcingElement.__json__(self)
        attrs = {'NominalDiameter': self.NominalDiameter, 'CrossSectionArea': self.CrossSectionArea,
                 'BarLength': self.BarLength, 'PredefinedType': self.PredefinedType, 'BarSurface': self.BarSurface}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcReinforcingBarType(IfcReinforcingElementType):
    def __init__(self, rtype, args):
        IfcReinforcingElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.NominalDiameter = args.pop()
        self.CrossSectionArea = args.pop()
        self.BarLength = args.pop()
        self.BarSurface = args.pop()
        self.BendingShapeCode = args.pop()
        self.BendingParameters = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:NominalDiameter:{NominalDiameter}:CrossSectionArea:{CrossSectionArea}:BarLength:{BarLength}:BarSurface:{BarSurface}:BendingShapeCode:{BendingShapeCode}:BendingParameters:{BendingParameters}".format(
            sup=IfcReinforcingElementType.__str__(self),
            PredefinedType=self.PredefinedType,
            NominalDiameter=self.NominalDiameter,
            CrossSectionArea=self.CrossSectionArea,
            BarLength=self.BarLength,
            BarSurface=self.BarSurface,
            BendingShapeCode=self.BendingShapeCode,
            BendingParameters=self.BendingParameters,
        )

    def __json__(self):
        sup = IfcReinforcingElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'NominalDiameter': self.NominalDiameter,
                 'CrossSectionArea': self.CrossSectionArea, 'BarLength': self.BarLength, 'BarSurface': self.BarSurface,
                 'BendingShapeCode': self.BendingShapeCode, 'BendingParameters': self.BendingParameters}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcRoof(IfcBuildingElement):
    def __init__(self, rtype, args):
        IfcBuildingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSanitaryTerminal(IfcFlowTerminal):
    def __init__(self, rtype, args):
        IfcFlowTerminal.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminal.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminal.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSensorType(IfcDistributionControlElementType):
    def __init__(self, rtype, args):
        IfcDistributionControlElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcDistributionControlElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcDistributionControlElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcShadingDevice(IfcBuildingElement):
    def __init__(self, rtype, args):
        IfcBuildingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSlab(IfcBuildingElement):
    def __init__(self, rtype, args):
        IfcBuildingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSlabElementedCase(IfcSlab):
    def __init__(self, rtype, args):
        IfcSlab.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcSlab.__str__(self),
        )

    def __json__(self):
        sup = IfcSlab.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSlabStandardCase(IfcSlab):
    def __init__(self, rtype, args):
        IfcSlab.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcSlab.__str__(self),
        )

    def __json__(self):
        sup = IfcSlab.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSolarDevice(IfcEnergyConversionDevice):
    def __init__(self, rtype, args):
        IfcEnergyConversionDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSpaceHeater(IfcFlowTerminal):
    def __init__(self, rtype, args):
        IfcFlowTerminal.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminal.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminal.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStackTerminal(IfcFlowTerminal):
    def __init__(self, rtype, args):
        IfcFlowTerminal.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminal.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminal.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStair(IfcBuildingElement):
    def __init__(self, rtype, args):
        IfcBuildingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStairFlight(IfcBuildingElement):
    def __init__(self, rtype, args):
        IfcBuildingElement.__init__(self, rtype, args)
        self.NumberOfRisers = args.pop()
        self.NumberOfTreads = args.pop()
        self.RiserHeight = args.pop()
        self.TreadLength = args.pop()
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:NumberOfRisers:{NumberOfRisers}:NumberOfTreads:{NumberOfTreads}:RiserHeight:{RiserHeight}:TreadLength:{TreadLength}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElement.__str__(self),
            NumberOfRisers=self.NumberOfRisers,
            NumberOfTreads=self.NumberOfTreads,
            RiserHeight=self.RiserHeight,
            TreadLength=self.TreadLength,
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElement.__json__(self)
        attrs = {'NumberOfRisers': self.NumberOfRisers, 'NumberOfTreads': self.NumberOfTreads,
                 'RiserHeight': self.RiserHeight, 'TreadLength': self.TreadLength,
                 'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralAnalysisModel(IfcSystem):
    def __init__(self, rtype, args):
        IfcSystem.__init__(self, rtype, args)
        self.PredefinedType = args.pop()
        self.OrientationOf2DPlane = args.pop()
        self.LoadedBy = args.pop()
        self.HasResults = args.pop()
        self.SharedPlacement = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}:OrientationOf2DPlane:{OrientationOf2DPlane}:LoadedBy:{LoadedBy}:HasResults:{HasResults}:SharedPlacement:{SharedPlacement}".format(
            sup=IfcSystem.__str__(self),
            PredefinedType=self.PredefinedType,
            OrientationOf2DPlane=self.OrientationOf2DPlane,
            LoadedBy=self.LoadedBy,
            HasResults=self.HasResults,
            SharedPlacement=self.SharedPlacement,
        )

    def __json__(self):
        sup = IfcSystem.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType, 'OrientationOf2DPlane': self.OrientationOf2DPlane,
                 'LoadedBy': self.LoadedBy, 'HasResults': self.HasResults, 'SharedPlacement': self.SharedPlacement}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralLoadCase(IfcStructuralLoadGroup):
    def __init__(self, rtype, args):
        IfcStructuralLoadGroup.__init__(self, rtype, args)
        self.SelfWeightCoefficients = args.pop()

    def __str__(self):
        return "{sup}:SelfWeightCoefficients:{SelfWeightCoefficients}".format(
            sup=IfcStructuralLoadGroup.__str__(self),
            SelfWeightCoefficients=self.SelfWeightCoefficients,
        )

    def __json__(self):
        sup = IfcStructuralLoadGroup.__json__(self)
        attrs = {'SelfWeightCoefficients': self.SelfWeightCoefficients}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcStructuralPlanarAction(IfcStructuralSurfaceAction):
    def __init__(self, rtype, args):
        IfcStructuralSurfaceAction.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcStructuralSurfaceAction.__str__(self),
        )

    def __json__(self):
        sup = IfcStructuralSurfaceAction.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSwitchingDevice(IfcFlowController):
    def __init__(self, rtype, args):
        IfcFlowController.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowController.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowController.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTank(IfcFlowStorageDevice):
    def __init__(self, rtype, args):
        IfcFlowStorageDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowStorageDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowStorageDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTransformer(IfcEnergyConversionDevice):
    def __init__(self, rtype, args):
        IfcEnergyConversionDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcTubeBundle(IfcEnergyConversionDevice):
    def __init__(self, rtype, args):
        IfcEnergyConversionDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcUnitaryControlElementType(IfcDistributionControlElementType):
    def __init__(self, rtype, args):
        IfcDistributionControlElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcDistributionControlElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcDistributionControlElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcUnitaryEquipment(IfcEnergyConversionDevice):
    def __init__(self, rtype, args):
        IfcEnergyConversionDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcValve(IfcFlowController):
    def __init__(self, rtype, args):
        IfcFlowController.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowController.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowController.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcWall(IfcBuildingElement):
    def __init__(self, rtype, args):
        IfcBuildingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcWallElementedCase(IfcWall):
    def __init__(self, rtype, args):
        IfcWall.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcWall.__str__(self),
        )

    def __json__(self):
        sup = IfcWall.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcWallStandardCase(IfcWall):
    def __init__(self, rtype, args):
        IfcWall.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcWall.__str__(self),
        )

    def __json__(self):
        sup = IfcWall.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcWasteTerminal(IfcFlowTerminal):
    def __init__(self, rtype, args):
        IfcFlowTerminal.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminal.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminal.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcWindow(IfcBuildingElement):
    def __init__(self, rtype, args):
        IfcBuildingElement.__init__(self, rtype, args)
        self.OverallHeight = args.pop()
        self.OverallWidth = args.pop()
        self.PredefinedType = args.pop()
        self.PartitioningType = args.pop()
        self.UserDefinedPartitioningType = args.pop()

    def __str__(self):
        return "{sup}:OverallHeight:{OverallHeight}:OverallWidth:{OverallWidth}:PredefinedType:{PredefinedType}:PartitioningType:{PartitioningType}:UserDefinedPartitioningType:{UserDefinedPartitioningType}".format(
            sup=IfcBuildingElement.__str__(self),
            OverallHeight=self.OverallHeight,
            OverallWidth=self.OverallWidth,
            PredefinedType=self.PredefinedType,
            PartitioningType=self.PartitioningType,
            UserDefinedPartitioningType=self.UserDefinedPartitioningType,
        )

    def __json__(self):
        sup = IfcBuildingElement.__json__(self)
        attrs = {'OverallHeight': self.OverallHeight, 'OverallWidth': self.OverallWidth,
                 'PredefinedType': self.PredefinedType, 'PartitioningType': self.PartitioningType,
                 'UserDefinedPartitioningType': self.UserDefinedPartitioningType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcWindowStandardCase(IfcWindow):
    def __init__(self, rtype, args):
        IfcWindow.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcWindow.__str__(self),
        )

    def __json__(self):
        sup = IfcWindow.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcActuatorType(IfcDistributionControlElementType):
    def __init__(self, rtype, args):
        IfcDistributionControlElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcDistributionControlElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcDistributionControlElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAirTerminal(IfcFlowTerminal):
    def __init__(self, rtype, args):
        IfcFlowTerminal.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminal.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminal.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAirTerminalBox(IfcFlowController):
    def __init__(self, rtype, args):
        IfcFlowController.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowController.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowController.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAirToAirHeatRecovery(IfcEnergyConversionDevice):
    def __init__(self, rtype, args):
        IfcEnergyConversionDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAlarmType(IfcDistributionControlElementType):
    def __init__(self, rtype, args):
        IfcDistributionControlElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcDistributionControlElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcDistributionControlElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAlignment(IfcLinearPositioningElement):
    def __init__(self, rtype, args):
        IfcLinearPositioningElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcLinearPositioningElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcLinearPositioningElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAudioVisualAppliance(IfcFlowTerminal):
    def __init__(self, rtype, args):
        IfcFlowTerminal.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminal.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminal.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBeam(IfcBuildingElement):
    def __init__(self, rtype, args):
        IfcBuildingElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcBuildingElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcBuildingElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBeamStandardCase(IfcBeam):
    def __init__(self, rtype, args):
        IfcBeam.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcBeam.__str__(self),
        )

    def __json__(self):
        sup = IfcBeam.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBoiler(IfcEnergyConversionDevice):
    def __init__(self, rtype, args):
        IfcEnergyConversionDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcBurner(IfcEnergyConversionDevice):
    def __init__(self, rtype, args):
        IfcEnergyConversionDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCableCarrierFitting(IfcFlowFitting):
    def __init__(self, rtype, args):
        IfcFlowFitting.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowFitting.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowFitting.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCableCarrierSegment(IfcFlowSegment):
    def __init__(self, rtype, args):
        IfcFlowSegment.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowSegment.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowSegment.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCableFitting(IfcFlowFitting):
    def __init__(self, rtype, args):
        IfcFlowFitting.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowFitting.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowFitting.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCableSegment(IfcFlowSegment):
    def __init__(self, rtype, args):
        IfcFlowSegment.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowSegment.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowSegment.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcChiller(IfcEnergyConversionDevice):
    def __init__(self, rtype, args):
        IfcEnergyConversionDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCoil(IfcEnergyConversionDevice):
    def __init__(self, rtype, args):
        IfcEnergyConversionDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCommunicationsAppliance(IfcFlowTerminal):
    def __init__(self, rtype, args):
        IfcFlowTerminal.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminal.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminal.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCompressor(IfcFlowMovingDevice):
    def __init__(self, rtype, args):
        IfcFlowMovingDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowMovingDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowMovingDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCondenser(IfcEnergyConversionDevice):
    def __init__(self, rtype, args):
        IfcEnergyConversionDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcControllerType(IfcDistributionControlElementType):
    def __init__(self, rtype, args):
        IfcDistributionControlElementType.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcDistributionControlElementType.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcDistributionControlElementType.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCooledBeam(IfcEnergyConversionDevice):
    def __init__(self, rtype, args):
        IfcEnergyConversionDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcCoolingTower(IfcEnergyConversionDevice):
    def __init__(self, rtype, args):
        IfcEnergyConversionDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDamper(IfcFlowController):
    def __init__(self, rtype, args):
        IfcFlowController.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowController.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowController.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDistributionChamberElement(IfcDistributionFlowElement):
    def __init__(self, rtype, args):
        IfcDistributionFlowElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcDistributionFlowElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcDistributionFlowElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDistributionCircuit(IfcDistributionSystem):
    def __init__(self, rtype, args):
        IfcDistributionSystem.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDistributionSystem.__str__(self),
        )

    def __json__(self):
        sup = IfcDistributionSystem.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDistributionControlElement(IfcDistributionElement):
    def __init__(self, rtype, args):
        IfcDistributionElement.__init__(self, rtype, args)

    def __str__(self):
        return "{sup}".format(
            sup=IfcDistributionElement.__str__(self),
        )

    def __json__(self):
        sup = IfcDistributionElement.__json__(self)
        attrs = {}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDuctFitting(IfcFlowFitting):
    def __init__(self, rtype, args):
        IfcFlowFitting.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowFitting.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowFitting.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDuctSegment(IfcFlowSegment):
    def __init__(self, rtype, args):
        IfcFlowSegment.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowSegment.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowSegment.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcDuctSilencer(IfcFlowTreatmentDevice):
    def __init__(self, rtype, args):
        IfcFlowTreatmentDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTreatmentDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTreatmentDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcElectricAppliance(IfcFlowTerminal):
    def __init__(self, rtype, args):
        IfcFlowTerminal.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminal.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminal.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcElectricDistributionBoard(IfcFlowController):
    def __init__(self, rtype, args):
        IfcFlowController.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowController.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowController.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcElectricFlowStorageDevice(IfcFlowStorageDevice):
    def __init__(self, rtype, args):
        IfcFlowStorageDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowStorageDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowStorageDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcElectricGenerator(IfcEnergyConversionDevice):
    def __init__(self, rtype, args):
        IfcEnergyConversionDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcElectricMotor(IfcEnergyConversionDevice):
    def __init__(self, rtype, args):
        IfcEnergyConversionDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcEnergyConversionDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcEnergyConversionDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcElectricTimeControl(IfcFlowController):
    def __init__(self, rtype, args):
        IfcFlowController.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowController.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowController.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFan(IfcFlowMovingDevice):
    def __init__(self, rtype, args):
        IfcFlowMovingDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowMovingDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowMovingDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFilter(IfcFlowTreatmentDevice):
    def __init__(self, rtype, args):
        IfcFlowTreatmentDevice.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTreatmentDevice.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTreatmentDevice.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFireSuppressionTerminal(IfcFlowTerminal):
    def __init__(self, rtype, args):
        IfcFlowTerminal.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcFlowTerminal.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcFlowTerminal.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcFlowInstrument(IfcDistributionControlElement):
    def __init__(self, rtype, args):
        IfcDistributionControlElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcDistributionControlElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcDistributionControlElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcProtectiveDeviceTrippingUnit(IfcDistributionControlElement):
    def __init__(self, rtype, args):
        IfcDistributionControlElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcDistributionControlElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcDistributionControlElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcSensor(IfcDistributionControlElement):
    def __init__(self, rtype, args):
        IfcDistributionControlElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcDistributionControlElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcDistributionControlElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcUnitaryControlElement(IfcDistributionControlElement):
    def __init__(self, rtype, args):
        IfcDistributionControlElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcDistributionControlElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcDistributionControlElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcActuator(IfcDistributionControlElement):
    def __init__(self, rtype, args):
        IfcDistributionControlElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcDistributionControlElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcDistributionControlElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcAlarm(IfcDistributionControlElement):
    def __init__(self, rtype, args):
        IfcDistributionControlElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcDistributionControlElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcDistributionControlElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res


@ifc_class
class IfcController(IfcDistributionControlElement):
    def __init__(self, rtype, args):
        IfcDistributionControlElement.__init__(self, rtype, args)
        self.PredefinedType = args.pop()

    def __str__(self):
        return "{sup}:PredefinedType:{PredefinedType}".format(
            sup=IfcDistributionControlElement.__str__(self),
            PredefinedType=self.PredefinedType,
        )

    def __json__(self):
        sup = IfcDistributionControlElement.__json__(self)
        attrs = {'PredefinedType': self.PredefinedType}
        res = {'rtype': self.rtype}
        res.update(sup)
        res.update(attrs)
        return res

# vim: set sw=4 ts=4 et:
