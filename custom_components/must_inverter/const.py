from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.number import NumberDeviceClass
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.const import Platform
from typing import NamedTuple

DOMAIN = "must_inverter"

CONF_BAUDRATE = "baudrate"
CONF_PARITY = "parity"
CONF_STOPBITS = "stopbits"
CONF_BYTESIZE = "bytesize"
CONF_RETRIES = "retries"
CONF_RECONNECT_DELAY = "reconnect_delay"
CONF_RECONNECT_DELAY_MAX = "reconnect_delay_max"

DEFAULT_SCAN_INTERVAL = 15

# model constants, needs to be lowercase otherwise hassfest checks fails...
MODEL_PV1800 = "pv1800"  # Base model
MODEL_PV1900 = "pv1900"

SUPPORTED_MODELS = [MODEL_PV1800, MODEL_PV1900]


class Sensor(NamedTuple):
    address: int
    name: str
    coeff: float | None
    unit: str | None
    platform: str
    device_class: str | None
    enabled: bool


class Range(NamedTuple):
    min: float | int
    max: float | int
    step: float | int


# fmt: off
# Base sensors, valid for all models
SENSORS_ARRAY = [
    #      addr    name                              coeff    unit      platform                       device_class                       enabled
    # Charger Control Messages
    Sensor(10101, "ChargerWorkEnable",               None,    None,     Platform.SWITCH,               None,                              True,  ),
    Sensor(10102, "AbsorbVoltage",                   0.1,     "V",      Platform.SENSOR,               SensorDeviceClass.VOLTAGE,         True,  ),
    Sensor(10103, "FloatVoltage",                    0.1,     "V",      Platform.NUMBER,               NumberDeviceClass.VOLTAGE,         True,  ),
    Sensor(10104, "AbsorptionVoltage",               0.1,     "V",      Platform.NUMBER,               NumberDeviceClass.VOLTAGE,         True,  ),
    Sensor(10105, "BatteryLowVoltage",               0.1,     "V",      Platform.NUMBER,               NumberDeviceClass.VOLTAGE,         True,  ),
    Sensor(10107, "BatteryHighVoltage",              0.1,     "V",      Platform.SENSOR,               SensorDeviceClass.VOLTAGE,         True,  ),
    Sensor(10108, "MaxChargerCurrent",               0.1,     "A",      Platform.NUMBER,               NumberDeviceClass.CURRENT,         True,  ),
    Sensor(10109, "AbsorbChargerCurrent",            0.1,     "A",      Platform.SENSOR,               SensorDeviceClass.CURRENT,         True,  ),
    Sensor(10110, "BatteryType",                     None,    None,     Platform.SELECT,               None,                              True,  ),
    Sensor(10111, "BatteryAh",                       1,       "Ah",     Platform.NUMBER,               None,                              True,  ),
    Sensor(10112, "RemoveTheAccumulatedData",        None,    None,     Platform.BUTTON,               None,                              False, ),
    Sensor(10118, "BatteryEqualizationEnable",       None,    None,     Platform.SWITCH,               None,                              True,  ),
    Sensor(10119, "BatteryEqualizationVoltage",      0.1,     "V",      Platform.NUMBER,               NumberDeviceClass.VOLTAGE,         True,  ),
    Sensor(10121, "BatteryEqualizationTime",         1,       "min",    Platform.NUMBER,               None,                              True,  ),
    Sensor(10122, "BatteryEqualizationTimeout",      1,       "min",    Platform.NUMBER,               None,                              True,  ),
    Sensor(10123, "BatteryEqualizationInterval",     1,       "day",    Platform.NUMBER,               None,                              True,  ),
    Sensor(10124, "BatteryEqualizationImmediately",  None,    None,     Platform.SWITCH,               None,                              True,  ),
    # Charger Display Messages
    Sensor(15201, "ChargerWorkstate",                None,    None,     Platform.SENSOR,               SensorDeviceClass.ENUM,            True,  ),
    Sensor(15202, "MpptState",                       None,    None,     Platform.SENSOR,               SensorDeviceClass.ENUM,            True,  ),
    Sensor(15203, "ChargingState",                   None,    None,     Platform.SENSOR,               SensorDeviceClass.ENUM,            True,  ),
    Sensor(15205, "PvVoltage",                       0.1,     "V",      Platform.SENSOR,               SensorDeviceClass.VOLTAGE,         True,  ),
    Sensor(15206, "BatteryVoltage",                  0.1,     "V",      Platform.SENSOR,               SensorDeviceClass.VOLTAGE,         True,  ),
    Sensor(15207, "ChargerCurrent",                  0.1,     "A",      Platform.SENSOR,               SensorDeviceClass.CURRENT,         True,  ),
    Sensor(15208, "ChargerPower",                    None,    "W",      Platform.SENSOR,               SensorDeviceClass.POWER,           True,  ),
    Sensor(15209, "RadiatorTemperature",             None,    "°C",     Platform.SENSOR,               SensorDeviceClass.TEMPERATURE,     True,  ),
    Sensor(15210, "ExternalTemperature",             None,    "°C",     Platform.SENSOR,               SensorDeviceClass.TEMPERATURE,     True,  ),
    Sensor(15211, "BatteryRelay",                    None,    None,     Platform.BINARY_SENSOR,        BinarySensorDeviceClass.POWER,     False, ),
    Sensor(15212, "PvRelay",                         None,    None,     Platform.BINARY_SENSOR,        BinarySensorDeviceClass.POWER,     False, ),
    Sensor(15213, "ChargerErrorMessage",             None,    None,     Platform.SENSOR,               None,                              True,  ),
    Sensor(15214, "ChargerWarningMessage",           None,    None,     Platform.SENSOR,               None,                              True,  ),
    Sensor(15215, "BattVolGrade",                    None,    "V",      Platform.SENSOR,               SensorDeviceClass.VOLTAGE,         False, ),
    Sensor(15216, "RatedCurrent",                    0.1,     "A",      Platform.SENSOR,               SensorDeviceClass.CURRENT,         False, ),
    Sensor(15217, "AccumulatedPower",                None,    "kWh",    Platform.SENSOR,               SensorDeviceClass.ENERGY,          True,  ),
    Sensor(15219, "AccumulatedTime",                 None,    "s",      Platform.SENSOR,               SensorDeviceClass.DURATION,        False, ),
    # Inverter Control Messages
    Sensor(20000, "InverterMachineType",             None,    None,     Platform.SENSOR,               None,                              False, ),
    Sensor(20002, "InverterSerialNumber",            None,    None,     Platform.SENSOR,               None,                              False, ),
    Sensor(20004, "InverterHardwareVersion",         None,    None,     Platform.SENSOR,               None,                              False, ),
    Sensor(20005, "InverterSoftwareVersion",         None,    None,     Platform.SENSOR,               None,                              False, ),
    Sensor(20009, "InverterBatteryVoltageC",         None,    None,     Platform.NUMBER,               None,                              False, ),
    Sensor(20010, "InverterVoltageC",                None,    None,     Platform.NUMBER,               None,                              False, ),
    Sensor(20011, "GridVoltageC",                    None,    None,     Platform.NUMBER,               None,                              False, ),
    Sensor(20012, "BusVoltageC",                     None,    None,     Platform.NUMBER,               None,                              False, ),
    Sensor(20013, "ControlCurrentC",                 None,    None,     Platform.NUMBER,               None,                              False, ),
    Sensor(20014, "InverterCurrentC",                None,    None,     Platform.NUMBER,               None,                              False, ),
    Sensor(20015, "GridCurrentC",                    None,    None,     Platform.NUMBER,               None,                              False, ),
    Sensor(20016, "LoadCurrentC",                    None,    None,     Platform.NUMBER,               None,                              False, ),
    Sensor(20101, "InverterOffgridWorkEnable",       None,    None,     Platform.SWITCH,               None,                              True,  ),
    Sensor(20102, "InverterOutputVoltageSet",        0.1,     "V",      Platform.NUMBER,               NumberDeviceClass.VOLTAGE,         True,  ),
    Sensor(20103, "InverterOutputFrequencySet",      0.01,    "Hz",     Platform.NUMBER,               NumberDeviceClass.FREQUENCY,       True,  ),
    Sensor(20104, "InverterSearchModeEnable",        None,    None,     Platform.SWITCH,               None,                              True,  ),
    Sensor(20105, "InverterOngridWorkEnable",        None,    None,     Platform.SWITCH,               None,                              False, ),
    Sensor(20106, "InverterChargerFromGridEnable",   None,    None,     Platform.SWITCH,               None,                              False, ),
    Sensor(20107, "InverterDischargerEnable",        None,    None,     Platform.SWITCH,               None,                              False, ),
    Sensor(20108, "InverterDischargerToGridEnable",  None,    None,     Platform.SWITCH,               None,                              False, ),
    Sensor(20109, "EnergyUseMode",                   None,    None,     Platform.SELECT,               None,                              True,  ),
    Sensor(20111, "GridProtectStandard",             None,    None,     Platform.SELECT,               None,                              True,  ),
    Sensor(20112, "SolarUseAim",                     None,    None,     Platform.SELECT,               None,                              True,  ),
    Sensor(20113, "InverterMaxDischargerCurrent",    0.1,     "A",      Platform.NUMBER,               NumberDeviceClass.CURRENT,         True,  ),
    Sensor(20118, "BatteryStopDischargingVoltage",   0.1,     "V",      Platform.NUMBER,               NumberDeviceClass.VOLTAGE,         True,  ),
    Sensor(20119, "BatteryStopChargingVoltage",      0.1,     "V",      Platform.NUMBER,               NumberDeviceClass.VOLTAGE,         True,  ),
    Sensor(20125, "GridMaxChargerCurrentSet",        0.1,     "A",      Platform.NUMBER,               NumberDeviceClass.CURRENT,         True,  ),
    Sensor(20127, "InverterBatteryLowVoltage",       0.1,     "V",      Platform.NUMBER,               NumberDeviceClass.VOLTAGE,         True,  ),
    Sensor(20128, "InverterBatteryHighVoltage",      0.1,     "V",      Platform.SENSOR,               SensorDeviceClass.VOLTAGE,         True,  ),
    Sensor(20132, "MaxCombineChargerCurrent",        0.1,     "A",      Platform.NUMBER,               NumberDeviceClass.CURRENT,         True,  ),
    Sensor(20142, "SystemSetting",                   None,    None,     Platform.SENSOR,               None,                              False, ),
    Sensor(20143, "ChargerSourcePriority",           None,    None,     Platform.SELECT,               None,                              True,  ),
    Sensor(20144, "SolarPowerBalance",               None,    None,     Platform.SWITCH,               None,                              True,  ),
    Sensor(20213, "InverterRemoveTheAccumulatedData",None,    None,     Platform.BUTTON,               None,                              False, ),
    # Inverter Display Messages
    Sensor(25201, "WorkState",                       None,    None,     Platform.SENSOR,               SensorDeviceClass.ENUM,            True,  ),
    Sensor(25202, "AcVoltageGrade",                  None,    "V",      Platform.SENSOR,               SensorDeviceClass.VOLTAGE,         False, ),
    Sensor(25203, "RatedPower",                      None,    "VA",     Platform.SENSOR,               SensorDeviceClass.APPARENT_POWER,  False, ),
    Sensor(25205, "InverterBatteryVoltage",          0.1,     "V",      Platform.SENSOR,               SensorDeviceClass.VOLTAGE,         True,  ),
    Sensor(25206, "InverterVoltage",                 0.1,     "V",      Platform.SENSOR,               SensorDeviceClass.VOLTAGE,         True,  ),
    Sensor(25207, "GridVoltage",                     0.1,     "V",      Platform.SENSOR,               SensorDeviceClass.VOLTAGE,         True,  ),
    Sensor(25208, "BusVoltage",                      0.1,     "V",      Platform.SENSOR,               SensorDeviceClass.VOLTAGE,         True,  ),
    Sensor(25209, "ControlCurrent",                  0.1,     "A",      Platform.SENSOR,               SensorDeviceClass.CURRENT,         True,  ),
    Sensor(25210, "InverterCurrent",                 0.1,     "A",      Platform.SENSOR,               SensorDeviceClass.CURRENT,         True,  ),
    Sensor(25211, "GridCurrent",                     0.1,     "A",      Platform.SENSOR,               SensorDeviceClass.CURRENT,         True,  ),
    Sensor(25212, "LoadCurrent",                     0.1,     "A",      Platform.SENSOR,               SensorDeviceClass.CURRENT,         True,  ),
    Sensor(25213, "PInverter",                       None,    "W",      Platform.SENSOR,               SensorDeviceClass.POWER,           True,  ),
    Sensor(25214, "PGrid",                           None,    "W",      Platform.SENSOR,               SensorDeviceClass.POWER,           True,  ),
    Sensor(25215, "PLoad",                           None,    "W",      Platform.SENSOR,               SensorDeviceClass.POWER,           True,  ),
    Sensor(25216, "LoadPercent",                     None,    "%",      Platform.SENSOR,               None,                              True,  ),
    Sensor(25217, "SInverter",                       None,    "VA",     Platform.SENSOR,               SensorDeviceClass.APPARENT_POWER,  True,  ),
    Sensor(25218, "SGrid",                           None,    "VA",     Platform.SENSOR,               SensorDeviceClass.APPARENT_POWER,  True,  ),
    Sensor(25219, "Sload",                           None,    "VA",     Platform.SENSOR,               SensorDeviceClass.APPARENT_POWER,  True,  ),
    Sensor(25221, "Qinverter",                       None,    "var",    Platform.SENSOR,               SensorDeviceClass.REACTIVE_POWER,  True,  ),
    Sensor(25222, "Qgrid",                           None,    "var",    Platform.SENSOR,               SensorDeviceClass.REACTIVE_POWER,  True,  ),
    Sensor(25223, "Qload",                           None,    "var",    Platform.SENSOR,               SensorDeviceClass.REACTIVE_POWER,  True,  ),
    Sensor(25225, "InverterFrequency",               0.01,    "Hz",     Platform.SENSOR,               SensorDeviceClass.FREQUENCY,       True,  ),
    Sensor(25226, "GridFrequency",                   0.01,    "Hz",     Platform.SENSOR,               SensorDeviceClass.FREQUENCY,       True,  ),
    Sensor(25229, "InverterMaxNumber",               None,    None,     Platform.SENSOR,               None,                              False, ),
    Sensor(25230, "CombineType",                     None,    None,     Platform.SENSOR,               None,                              False, ),
    Sensor(25231, "InverterNumber",                  None,    None,     Platform.SENSOR,               None,                              False, ),
    Sensor(25233, "AcRadiatorTemperature",           None,    "°C",     Platform.SENSOR,               SensorDeviceClass.TEMPERATURE,     True,  ),
    Sensor(25234, "TransformerTemperature",          None,    "°C",     Platform.SENSOR,               SensorDeviceClass.TEMPERATURE,     True,  ),
    Sensor(25235, "DcRadiatorTemperature",           None,    "°C",     Platform.SENSOR,               SensorDeviceClass.TEMPERATURE,     True,  ),
    Sensor(25237, "InverterRelayState",              None,    None,     Platform.BINARY_SENSOR,        BinarySensorDeviceClass.POWER,     False, ),
    Sensor(25238, "GridRelayState",                  None,    None,     Platform.BINARY_SENSOR,        BinarySensorDeviceClass.POWER,     False, ),
    Sensor(25239, "LoadRelayState",                  None,    None,     Platform.BINARY_SENSOR,        BinarySensorDeviceClass.POWER,     False, ),
    Sensor(25240, "N_LineRelayState",                None,    None,     Platform.BINARY_SENSOR,        BinarySensorDeviceClass.POWER,     False, ),
    Sensor(25241, "DCRelayState",                    None,    None,     Platform.BINARY_SENSOR,        BinarySensorDeviceClass.POWER,     False, ),
    Sensor(25242, "EarthRelayState",                 None,    None,     Platform.BINARY_SENSOR,        BinarySensorDeviceClass.POWER,     False, ),
    Sensor(25245, "AccumulatedChargerPower",         None,    "kWh",    Platform.SENSOR,               SensorDeviceClass.ENERGY,          True,  ),
    Sensor(25247, "AccumulatedDischargerPower",      None,    "kWh",    Platform.SENSOR,               SensorDeviceClass.ENERGY,          True,  ),
    Sensor(25249, "AccumulatedBuyPower",             None,    "kWh",    Platform.SENSOR,               SensorDeviceClass.ENERGY,          True,  ),
    Sensor(25251, "AccumulatedSellPower",            None,    "kWh",    Platform.SENSOR,               SensorDeviceClass.ENERGY,          True,  ),
    Sensor(25253, "AccumulatedLoadPower",            None,    "kWh",    Platform.SENSOR,               SensorDeviceClass.ENERGY,          True,  ),
    Sensor(25255, "AccumulatedSelfUsePower",         None,    "kWh",    Platform.SENSOR,               SensorDeviceClass.ENERGY,          True,  ),
    Sensor(25257, "AccumulatedPvSellPower",          None,    "kWh",    Platform.SENSOR,               SensorDeviceClass.ENERGY,          True,  ),
    Sensor(25259, "AccumulatedGridChargerPower",     None,    "kWh",    Platform.SENSOR,               SensorDeviceClass.ENERGY,          True,  ),
    Sensor(25261, "InverterErrorMessage",            None,    None,     Platform.SENSOR,               None,                              True,  ),
    Sensor(25265, "InverterWarningMessage",          None,    None,     Platform.SENSOR,               None,                              True,  ),
    Sensor(25273, "BattPower",                       None,    "W",      Platform.SENSOR,               SensorDeviceClass.POWER,           True,  ),
    Sensor(25274, "BattCurrent",                     None,    "A",      Platform.SENSOR,               SensorDeviceClass.CURRENT,         True,  ),
    Sensor(25277, "RatedPowerW",                     None,    "W",      Platform.SENSOR,               SensorDeviceClass.POWER,           False, ),
]

PV1900_SENSORS = [
    # Additional sensors for PV19 series
    Sensor(113,   "StateOfCharge",                   None,    "%",      Platform.SENSOR,               SensorDeviceClass.BATTERY,         True,  ),
    Sensor(114,   "BatteryStateOfHealth",            None,    "%",      Platform.SENSOR,               None,                              True,  ),
    # PV1 Charger data
    Sensor(15207, "PV1ChargerCurrent",               0.1,     "A",      Platform.SENSOR,               SensorDeviceClass.CURRENT,         True,  ),
    Sensor(15208, "PV1ChargerPower",                 None,    "W",      Platform.SENSOR,               SensorDeviceClass.POWER,           True,  ),
    # PV2 Charger data
    Sensor(16207, "PV2ChargerCurrent",               0.1,     "A",      Platform.SENSOR,               SensorDeviceClass.CURRENT,         True,  ),
    Sensor(16208, "PV2ChargerPower",                 None,    "W",      Platform.SENSOR,               SensorDeviceClass.POWER,           True,  ),
]
# fmt: on

OPTIONS = {
    "EnergyUseMode": ["", "sbu", "sub", "uti", "sol"],
    "GridProtectStandard": ["vde4105", "ups", "apl", "gen"],
    "SolarUseAim": ["lbu", "blu"],
    "ChargerSourcePriority": ["solar_first", "", "solar_and_utility", "only_solar"],
    "WorkState": ["poweron", "selftest", "offgrid", "grid_tie", "bypass", "stop", "grid_charging"],
    "BatteryType": ["", "user_defined", "lithium", "sealed_lead", "agm", "gel", "flooded"],
    "ChargerWorkstate": ["initialization", "selftest", "work", "stop"],
    "MpptState": ["stop", "mppt", "current_limiting"],
    "ChargingState": ["stop", "absorb_charge", "float_charge", "equalization_charge"],
}

# fmt: off
RANGES = {
    # name                                               min    max    step
    "FloatVoltage":                   lambda data: Range((data["BattVolGrade"] / 24) * 24.0,  (data["BattVolGrade"] / 24) * 29.2,   0.1 ),
    "AbsorptionVoltage":              lambda data: Range((data["BattVolGrade"] / 24) * 24.0,  (data["BattVolGrade"] / 24) * 29.2,   0.1 ),
    "BatteryLowVoltage":              lambda data: Range((data["BattVolGrade"] / 24) * 20.0,  (data["BattVolGrade"] / 24) * 24.0,   0.1 ),
    "BatteryEqualizationVoltage":     lambda data: Range((data["BattVolGrade"] / 24) * 24,    (data["BattVolGrade"] / 24) * 29.2,   0.1 ),
    "BatteryStopDischargingVoltage":  lambda data: Range((data["BattVolGrade"] / 24) * 22.0,  (data["BattVolGrade"] / 24) * 29.0,   0.1 ),
    "BatteryStopChargingVoltage":     lambda data: Range((data["BattVolGrade"] / 24) * 22.0,  (data["BattVolGrade"] / 24) * 29.0,   0.1 ),
    "InverterBatteryLowVoltage":      lambda data: Range((data["BattVolGrade"] / 24) * 20.0,  (data["BattVolGrade"] / 24) * 24.0,   0.1 ),
    "MaxChargerCurrent":              lambda data: Range(1,     data["RatedCurrent"] * 0.1,    1),
    "BatteryAh":                      lambda data: Range(1,     900,    1   ),
    "BatteryEqualizationTime":        lambda data: Range(5,     900,    5   ),
    "BatteryEqualizationTimeout":     lambda data: Range(5,     900,    5   ),
    "BatteryEqualizationInterval":    lambda data: Range(0,     90,     1   ),
    "InverterOutputVoltageSet":       lambda data: Range(220,   240,    1   ),
    "InverterOutputFrequencySet":     lambda data: Range(50,    60,     10  ),
    "InverterMaxDischargerCurrent":   lambda data: Range(1,     13,     0.1 ),
    "GridMaxChargerCurrentSet":       lambda data: Range(20,    30,     10  ),
    "MaxCombineChargerCurrent":       lambda data: Range(1,     80,     1   ),
    "InverterBatteryVoltageC":        lambda data: Range(0,     0xFFFF, 1   ),
    "InverterVoltageC":               lambda data: Range(0,     0xFFFF, 1   ),
    "GridVoltageC":                   lambda data: Range(0,     0xFFFF, 1   ),
    "BusVoltageC":                    lambda data: Range(0,     0xFFFF, 1   ),
    "ControlCurrentC":                lambda data: Range(0,     0xFFFF, 1   ),
    "InverterCurrentC":               lambda data: Range(0,     0xFFFF, 1   ),
    "GridCurrentC":                   lambda data: Range(0,     0xFFFF, 1   ),
    "LoadCurrentC":                   lambda data: Range(0,     0xFFFF, 1   ),
}
# fmt: on

INVERTER_ERROR = [
    # 1
    "Fan is locked when inverter is off",
    "Inverter transformer over temperature",
    "battery voltage is too high",
    "battery voltage is too low",
    "Output short circuited",
    "Inverter output voltage is high",
    "Overload time out",
    "Inverter bus voltage is too high",
    "Bus soft start failed",
    "Main relay failed",
    "Inverter output voltage sensor error",
    "Inverter grid voltage sensor error",
    "Inverter output current sensor error",
    "Inverter grid current sensor error",
    "Inverter load current sensor error",
    "Inverter grid over current error"
    # 2
    "Inverter radiator over temperature",
    "Solar charger battery voltage class error",
    "Solar charger current sensor error",
    "Solar charger current is uncontrollable",
    "Inverter grid voltage is low",
    "Inverter grid voltage is high",
    "Inverter grid under frequency",
    "Inverter grid over frequency",
    "Inverter over current protection error",
    "Inverter bus voltage is too low",
    "Inverter soft start failed",
    "Over DC voltage in AC output",
    "Battery connection is open",
    "Inverter control current sensor error",
    "Inverter output voltage is too low",
    "",
    # 3
    # Unknown
]

INVERTER_WARNING = [
    "Fan is locked when inverter is on.",
    "Fan2 is locked when inverter is on.",
    "Battery is over-charged.",
    "Low battery",
    "Overload",
    "Output power derating",
    "Solar charger stops due to low battery.",
    "Solar charger stops due to high PV voltage.",
    "Solar charger stops due to over load.",
    "Solar charger over temperature",
    "PV charger communication error ",
    "",
    "",
    "",
    "",
    "",
]

CHARGER_ERROR = [
    "Hardware protection",
    "Over current",
    "Current sensor error",
    "Over temperature",
    "PV voltage is too high",
    "PV voltage is too low",
    "Battery voltage is too high",
    "Battery voltage is too Low",
    "Current is uncontrollable",
    "Parameter error",
    "",
    "",
    "",
    "",
    "",
    "",
]

CHARGER_WARNING = ["Fan Error", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]


def get_sensors_for_model(model: str) -> list:
    """Return sensors based on inverter model.

    PV1800: Base sensors only
    PV1900: Base sensors + PV2 and extended battery monitoring
    """
    if model == MODEL_PV1900:
        return SENSORS_ARRAY + PV1900_SENSORS
    return SENSORS_ARRAY
