# @internal
#  @author: Gabriel JARRY
# @endinternal

DERIV = "DERIV"
SEP = "_"

COL_SYST_TRAJ_ID = "SYST_TRAJ_ID"
COL_SYST_POINT_ID = "SYST_POINT_ID"
COL_PLOT_DATE = "PLOT_DATE"
COL_TIME_LAST_PLOT = "TIME_LAST_PLOT"
COL_LONGITUDE = "LONGITUDE"
COL_LATITUDE = "LATITUDE"
COL_ALTI_STD_FT = "ALTI_STD_FT"
COL_GRND_SPD_KT = "GRND_SPD_KT"
COL_VERT_SPD_FTMN = "VERT_SPD_FTMN"
COL_FLPL_CALL_SIGN = "FLPL_CALL_SIGN"
COL_FLPL_AIRC_TYPE = "FLPL_AIRC_TYPE"
COL_FLPL_DEPR_AIRP = "FLPL_DEPR_AIRP"
COL_FLPL_ARRV_AIRP = "FLPL_ARRV_AIRP"
COL_ESTIM_FUEL_FLOW_ACRPL = "ESTIM_FUEL_FLOW_ACRPL"
COL_ESTIM_FUEL_FLOW_KGH = "ESTIM_FUEL_FLOW_KGH"
COL_CONF_IND = "CONF_IND"
COL_ESTIM_CONSO_KG = "ESTIM_CONSO_KG"
COL_FLIGHT_TIME = "FLIGHT_TIME"
COL_TIME = "TIME"
COL_MASS = "MASS"
COL_MASS_KG = "MASS_KG"
COL_TRUE_AIR_SPD_KT = "TRUE_AIR_SPD_KT"
COL_ACFT_ICAO_TYPE = "ACFT_ICAO_TYPE"
COL_FUEL_FLOW_TO = "FUEL_FLOW_TO"
COL_MAX_OPE_MACH_NUM = "MAX_OPE_MACH_NUM"
COL_MAX_TO_WEIGHT = "MAX_TO_WEIGHT"
COL_OPE_EMPTY_WEIGHT = "OPE_EMPTY_WEIGHT"
COL_ACFT_SPAN = "ACFT_SPAN"
COL_ACFT_LENGTH = "ACFT_LENGTH"
COL_ENGINE_NUM = "ENGINE_NUM"
COL_MAX_OPE_SPEED = "MAX_OPE_SPEED"
COL_MAX_OPE_ALTI = "MAX_OPE_ALTI"
COL_SURFACE = "SURFACE"
COL_ENGINE_TYPE = "ENGINE_TYPE"

COL_DERIV_ALTI_STD_FT = DERIV + SEP + COL_ALTI_STD_FT
COL_DERIV_GRND_SPD_KT = DERIV + SEP + COL_GRND_SPD_KT
COL_DERIV_TRUE_AIR_SPD_KT = DERIV + SEP + COL_TRUE_AIR_SPD_KT

COLS_SMOOTH = [
    COL_ALTI_STD_FT,
    COL_GRND_SPD_KT,
    COL_VERT_SPD_FTMN
]

COLS_KEEP = [
    COL_SYST_TRAJ_ID,
    COL_FLPL_AIRC_TYPE,
    COL_FLPL_CALL_SIGN,
    COL_FLPL_DEPR_AIRP,
    COL_FLPL_ARRV_AIRP
]


COLS_RESAMPLE = [
    COL_LONGITUDE,
    COL_LATITUDE,
    COL_ALTI_STD_FT,
    COL_GRND_SPD_KT,
    COL_VERT_SPD_FTMN
]

COLS_ACFT_PARAMS = [
    COL_ACFT_ICAO_TYPE,
    COL_FUEL_FLOW_TO,
    COL_SURFACE,
    COL_MAX_OPE_ALTI,
    COL_MAX_OPE_MACH_NUM,
    COL_MAX_TO_WEIGHT,
    COL_OPE_EMPTY_WEIGHT,
    COL_ACFT_SPAN,
    COL_ACFT_LENGTH,
    COL_ENGINE_NUM,
    COL_MAX_OPE_SPEED,
    COL_CONF_IND,
    COL_ENGINE_TYPE
]

COLS_INPUT_FUEL = [
    COL_ENGINE_TYPE,
    COL_DERIV_ALTI_STD_FT,
    COL_DERIV_GRND_SPD_KT,
    COL_DERIV_TRUE_AIR_SPD_KT,
    COL_SURFACE,
    COL_MAX_OPE_ALTI,
    COL_MAX_OPE_SPEED,
    COL_ALTI_STD_FT,
    COL_GRND_SPD_KT,
    COL_TRUE_AIR_SPD_KT,
    COL_VERT_SPD_FTMN,
    COL_MASS
]

COLS_PROCESS = [
    COL_SYST_POINT_ID,
    COL_TIME,
    COL_TIME_LAST_PLOT,
    COL_FLIGHT_TIME,
    COL_PLOT_DATE
]

COLS_FUEL = [
    COL_ESTIM_FUEL_FLOW_ACRPL,
    COL_ESTIM_CONSO_KG,
    COL_ESTIM_FUEL_FLOW_KGH,
    COL_GRND_SPD_KT,
    COL_TRUE_AIR_SPD_KT,
    COL_MASS,
    COL_FLPL_AIRC_TYPE,
    COL_ENGINE_NUM,
    COL_FUEL_FLOW_TO,
    COL_CONF_IND,
    COL_DERIV_TRUE_AIR_SPD_KT,
    COL_DERIV_GRND_SPD_KT,
    COL_TIME_LAST_PLOT,
    COL_ALTI_STD_FT,
    COL_OPE_EMPTY_WEIGHT,
    COL_MAX_TO_WEIGHT
]


