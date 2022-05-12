from typing import ClassVar, Dict, Iterator, List, Sequence, Optional, Union
from logging import Logger

class ArrayStruct:
    def __init__(self) -> None: ...

class BalanceType:
    __members__: ClassVar[Dict[str, BalanceType]] = ...  # read-only
    PROPORTIONAL_TO_CONFORM_LOAD: ClassVar[BalanceType] = ...
    PROPORTIONAL_TO_GENERATION_P: ClassVar[BalanceType] = ...
    PROPORTIONAL_TO_GENERATION_P_MAX: ClassVar[BalanceType] = ...
    PROPORTIONAL_TO_LOAD: ClassVar[BalanceType] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class ConnectedComponentMode:
    __members__: ClassVar[Dict[str, ConnectedComponentMode]] = ...  # read-only
    ALL: ClassVar[ConnectedComponentMode] = ...
    MAIN: ClassVar[ConnectedComponentMode] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class ContingencyContextType:
    __members__: ClassVar[Dict[str, ContingencyContextType]] = ...  # read-only
    ALL: ClassVar[ContingencyContextType] = ...
    NONE: ClassVar[ContingencyContextType] = ...
    SPECIFIC: ClassVar[ContingencyContextType] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class ContingencyResult:
    @property
    def contingency_id(self) -> str: ...
    @property
    def limit_violations(self) -> LimitViolationArray: ...
    @property
    def status(self) -> LoadFlowComponentStatus: ...

class ContingencyResultArray:
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...

class ElementType:
    __members__: ClassVar[Dict[str, ElementType]] = ...  # read-only
    BATTERY: ClassVar[ElementType] = ...
    BUS: ClassVar[ElementType] = ...
    BUSBAR_SECTION: ClassVar[ElementType] = ...
    DANGLING_LINE: ClassVar[ElementType] = ...
    GENERATOR: ClassVar[ElementType] = ...
    HVDC_LINE: ClassVar[ElementType] = ...
    LCC_CONVERTER_STATION: ClassVar[ElementType] = ...
    OPERATIONAL_LIMITS: ClassVar[ElementType] = ...
    LINE: ClassVar[ElementType] = ...
    LINEAR_SHUNT_COMPENSATOR_SECTION: ClassVar[ElementType] = ...
    LOAD: ClassVar[ElementType] = ...
    MINMAX_REACTIVE_LIMITS: ClassVar[ElementType] = ...
    NON_LINEAR_SHUNT_COMPENSATOR_SECTION: ClassVar[ElementType] = ...
    PHASE_TAP_CHANGER: ClassVar[ElementType] = ...
    PHASE_TAP_CHANGER_STEP: ClassVar[ElementType] = ...
    RATIO_TAP_CHANGER: ClassVar[ElementType] = ...
    RATIO_TAP_CHANGER_STEP: ClassVar[ElementType] = ...
    REACTIVE_CAPABILITY_CURVE_POINT: ClassVar[ElementType] = ...
    SHUNT_COMPENSATOR: ClassVar[ElementType] = ...
    STATIC_VAR_COMPENSATOR: ClassVar[ElementType] = ...
    SUBSTATION: ClassVar[ElementType] = ...
    SWITCH: ClassVar[ElementType] = ...
    THREE_WINDINGS_TRANSFORMER: ClassVar[ElementType] = ...
    TWO_WINDINGS_TRANSFORMER: ClassVar[ElementType] = ...
    VOLTAGE_LEVEL: ClassVar[ElementType] = ...
    VSC_CONVERTER_STATION: ClassVar[ElementType] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class FilterAttributesType:
    __members__: ClassVar[Dict[str, FilterAttributesType]] = ...  # read-only
    ALL_ATTRIBUTES: ClassVar[FilterAttributesType] = ...
    DEFAULT_ATTRIBUTES: ClassVar[FilterAttributesType] = ...
    SELECTION_ATTRIBUTES: ClassVar[FilterAttributesType] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class JavaHandle:
    ...

class Dataframe:
    ...

class LimitType:
    __members__: ClassVar[Dict[str, LimitType]] = ...  # read-only
    CURRENT: ClassVar[LimitType] = ...
    HIGH_VOLTAGE: ClassVar[LimitType] = ...
    LOW_VOLTAGE: ClassVar[LimitType] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class LimitViolation:
    @property
    def acceptable_duration(self) -> int: ...
    @property
    def limit(self) -> float: ...
    @property
    def limit_name(self) -> str: ...
    @property
    def limit_reduction(self) -> float: ...
    @property
    def limit_type(self) -> LimitType: ...
    @property
    def side(self) -> Side: ...
    @property
    def subject_id(self) -> str: ...
    @property
    def subject_name(self) -> str: ...
    @property
    def value(self) -> float: ...

class LimitViolationArray:
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...

class LoadFlowComponentResult:
    @property
    def connected_component_num(self) -> int: ...
    @property
    def iteration_count(self) -> int: ...
    @property
    def slack_bus_active_power_mismatch(self) -> float: ...
    @property
    def slack_bus_id(self) -> str: ...
    @property
    def status(self) -> LoadFlowComponentStatus: ...
    @property
    def synchronous_component_num(self) -> int: ...

class LoadFlowComponentResultArray:
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...

class LoadFlowComponentStatus:
    __members__: ClassVar[Dict[str, LoadFlowComponentStatus]] = ...  # read-only
    CONVERGED: ClassVar[LoadFlowComponentStatus] = ...
    FAILED: ClassVar[LoadFlowComponentStatus] = ...
    MAX_ITERATION_REACHED: ClassVar[LoadFlowComponentStatus] = ...
    SOLVER_FAILED: ClassVar[LoadFlowComponentStatus] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class LoadFlowParameters:
    balance_type: BalanceType
    connected_component_mode: ConnectedComponentMode
    countries_to_balance: Sequence[str]
    dc_use_transformer_ratio: bool
    distributed_slack: bool
    no_generator_reactive_limits: bool
    phase_shifter_regulation_on: bool
    read_slack_bus: bool
    simul_shunt: bool
    transformer_voltage_control_on: bool
    twt_split_shunt_admittance: bool
    voltage_init_mode: VoltageInitMode
    write_slack_bus: bool
    provider_parameters_keys: List[str]
    provider_parameters_values: List[str]
    def __init__(self) -> None: ...

class Matrix:
    ...

class NetworkMetadata:
    @property
    def case_date(self) -> float: ...
    @property
    def forecast_distance(self) -> int: ...
    @property
    def id(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def source_format(self) -> str: ...

class PyPowsyblError(Exception): ...

class Series:
    @property
    def data(self) -> object: ...
    @property
    def index(self) -> bool: ...
    @property
    def name(self) -> str: ...

class SeriesArray:
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...

class SeriesMetadata:
    def __init__(self, arg0: str, arg1: int, arg2: bool, arg3: bool, arg4: bool) -> None: ...
    @property
    def is_index(self) -> bool: ...
    @property
    def is_modifiable(self) -> bool: ...
    @property
    def is_default(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def type(self) -> int: ...

class Side:
    __members__: ClassVar[Dict[str, Side]] = ...  # read-only
    NONE: ClassVar[Side] = ...
    ONE: ClassVar[Side] = ...
    TWO: ClassVar[Side] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class ValidationLevel:
    __members__: ClassVar[Dict[str, ValidationLevel]] = ...  # read-only
    EQUIPMENT: ClassVar[ValidationLevel] = ...
    STEADY_STATE_HYPOTHESIS: ClassVar[ValidationLevel] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class ValidationType:
    __members__: ClassVar[Dict[str, ValidationType]] = ...  # read-only
    ALL: ClassVar[list] = ...
    BUSES: ClassVar[ValidationType] = ...
    FLOWS: ClassVar[ValidationType] = ...
    GENERATORS: ClassVar[ValidationType] = ...
    SHUNTS: ClassVar[ValidationType] = ...
    SVCS: ClassVar[ValidationType] = ...
    TWTS: ClassVar[ValidationType] = ...
    TWTS3W: ClassVar[ValidationType] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class VoltageInitMode:
    __members__: ClassVar[Dict[str, VoltageInitMode]] = ...  # read-only
    DC_VALUES: ClassVar[VoltageInitMode] = ...
    PREVIOUS_VALUES: ClassVar[VoltageInitMode] = ...
    UNIFORM_VALUES: ClassVar[VoltageInitMode] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class Zone:
    def __init__(self, id: str, injections_ids: List[str], injections_shift_keys: List[float]) -> None: ...

def add_contingency(analysis_context: JavaHandle, contingency_id: str, elements_ids: List[str]) -> None: ...
def add_monitored_elements(security_analysis_context: JavaHandle, contingency_context_type: ContingencyContextType, branch_ids: List[str], voltage_level_ids: List[str], three_windings_transformer_ids: List[str], contingency_ids: List[str]) -> None: ...
def clone_variant(network: JavaHandle, src: str, variant: str, may_overwrite: bool) -> None: ...
def create_dataframe(columns_values: list, columns_names: List[str], columns_types: List[int], is_index: List[bool]) -> Dataframe: ...
def create_element(network: JavaHandle, dataframes: List[Optional[Dataframe]], element_type: ElementType) -> None: ...
def create_exporter_parameters_series_array(format: str) -> SeriesArray: ...
def create_importer_parameters_series_array(format: str) -> SeriesArray: ...
def create_network(name: str, id: str) -> JavaHandle: ...
def create_network_elements_series_array(network: JavaHandle, element_type: ElementType, filter_attributes_type: FilterAttributesType, attributes: List[str], array: Optional[Dataframe]) -> SeriesArray: ...
def create_network_elements_extension_series_array(network: JavaHandle, extension_name: str) -> SeriesArray: ...
def get_extensions_names() -> List[str]: ...
def create_security_analysis() -> JavaHandle: ...
def create_sensitivity_analysis() -> JavaHandle: ...
def dump_network(network: JavaHandle, file: str, format: str, parameters: Dict[str,str]) -> None: ...
def dump_network_to_string(network: JavaHandle, format: str, parameters: Dict[str,str]) -> str: ...
def get_branch_flows_sensitivity_matrix(sensitivity_analysis_result_context: JavaHandle, matrix_id: str, contingency_id: str) -> Matrix: ...
def get_branch_results(result: JavaHandle) -> SeriesArray: ...
def get_bus_breaker_view_buses(network: JavaHandle, voltage_level: str) -> SeriesArray: ...
def get_bus_breaker_view_elements(network: JavaHandle, voltage_level: str) -> SeriesArray: ...
def get_bus_breaker_view_switches(network: JavaHandle, voltage_level: str) -> SeriesArray: ...
def get_bus_results(result: JavaHandle) -> SeriesArray: ...
def get_bus_voltages_sensitivity_matrix(sensitivity_analysis_result_context: JavaHandle, contingency_id: str) -> Matrix: ...
def get_provider_parameters_names(provider: str) -> List[str]: ...
def get_limit_violations(result: JavaHandle) -> SeriesArray: ...
def get_network_area_diagram_svg(network: JavaHandle, voltage_level_ids:  Union[str, List[str]], depth: int) -> str: ...
def get_network_elements_ids(network: JavaHandle, element_type: ElementType, nominal_voltages: List[float], countries: List[str], main_connected_component: bool, main_synchronous_component: bool, not_connected_to_same_bus_at_both_sides: bool) -> List[str]: ...
def get_network_export_formats() -> List[str]: ...
def get_network_import_formats() -> List[str]: ...
def get_loadflow_provider_names() -> List[str]: ...
def get_security_analysis_provider_names() -> List[str]: ...
def get_sensitivity_analysis_provider_names() -> List[str]: ...
def get_network_metadata(network: JavaHandle) -> NetworkMetadata: ...
def get_node_breaker_view_internal_connections(network: JavaHandle, voltage_level: str) -> SeriesArray: ...
def get_node_breaker_view_nodes(network: JavaHandle, voltage_level: str) -> SeriesArray: ...
def get_node_breaker_view_switches(network: JavaHandle, voltage_level: str) -> SeriesArray: ...
def get_reference_flows(sensitivity_analysis_result_context: JavaHandle, matrix_id: str, contingency_id: str) -> Matrix: ...
def get_reference_voltages(sensitivity_analysis_result_context: JavaHandle, contingency_id: str) -> Matrix: ...
def get_security_analysis_result(result: JavaHandle) -> ContingencyResultArray: ...
def get_network_elements_dataframe_metadata(element_type: ElementType) -> List[SeriesMetadata]: ...
def get_network_elements_creation_dataframes_metadata(element_type: ElementType) -> List[List[SeriesMetadata]]: ...
def get_single_line_diagram_svg(network: JavaHandle, container_id: str) -> str: ...
def get_three_windings_transformer_results(result: JavaHandle) -> SeriesArray: ...
def get_validation_level(network: JavaHandle) -> ValidationLevel: ...
def get_variant_ids(network: JavaHandle) -> List[str]: ...
def get_version_table() -> str: ...
def get_working_variant_id(network: JavaHandle) -> str: ...
def add_branch_flow_factor_matrix(sensitivity_analysis_context: JavaHandle, matrix_id: str, branches_ids: List[str], variables_ids: List[str]) -> None: ...
def add_precontingency_branch_flow_factor_matrix(sensitivity_analysis_context: JavaHandle, matrix_id: str, branches_ids: List[str], variables_ids: List[str]) -> None: ...
def add_postcontingency_branch_flow_factor_matrix(sensitivity_analysis_context: JavaHandle, matrix_id: str, branches_ids: List[str], variables_ids: List[str], contingencies_ids: List[str]) -> None: ...
def is_config_read() -> bool: ...
def get_default_loadflow_provider() -> str: ...
def get_default_security_analysis_provider() -> str: ...
def get_default_sensitivity_analysis_provider() -> str: ...
def load_network(file: str, parameters: Dict[str,str]) -> JavaHandle: ...
def load_network_from_string(file_name: str, file_content: str, parameters: Dict[str,str]) -> JavaHandle: ...
def merge(arg0: JavaHandle, arg1: List[JavaHandle]) -> None: ...
def reduce_network(network: JavaHandle, v_min: float, v_max: float, ids: List[str], vls: List[str], depths: List[int], with_dangling_lines: bool) -> None: ...
def remove_elements(network: JavaHandle, element_ids: List[str]) -> None: ...
def remove_variant(network: JavaHandle, variant: str) -> None: ...
def run_load_flow(network: JavaHandle, dc: bool, parameters: LoadFlowParameters, provider: str) -> LoadFlowComponentResultArray: ...
def run_load_flow_validation(network: JavaHandle, validation_type: ValidationType) -> SeriesArray: ...
def run_security_analysis(security_analysis_context: JavaHandle, network: JavaHandle, parameters: LoadFlowParameters, provider: str, dc: bool) -> JavaHandle: ...
def run_sensitivity_analysis(sensitivity_analysis_context: JavaHandle, network: JavaHandle, dc: bool, parameters: LoadFlowParameters, provider: str) -> JavaHandle: ...
def set_branch_flow_factor_matrix(sensitivity_analysis_context: JavaHandle, branches_ids: List[str], variables_ids: List[str]) -> None: ...
def set_bus_voltage_factor_matrix(sensitivity_analysis_context: JavaHandle, bus_ids: List[str], target_voltage_ids: List[str]) -> None: ...
def set_config_read(arg0: bool) -> None: ...
def set_logger(logger: Logger) -> None: ...
def set_default_loadflow_provider(provider: str) -> None: ...
def set_default_security_analysis_provider(provider: str) -> None: ...
def set_default_sensitivity_analysis_provider(provider: str) -> None: ...
def set_java_library_path(arg0: str) -> None: ...
def set_min_validation_level(network: JavaHandle, validation_level: ValidationLevel) -> None: ...
def set_working_variant(network: JavaHandle, variant: str) -> None: ...
def set_zones(sensitivity_analysis_context: JavaHandle, zones: List[Zone]) -> None: ...
def get_logger() -> Logger: ...
def update_connectable_status(arg0: JavaHandle, arg1: str, arg2: bool) -> bool: ...
def update_network_elements_with_series(network: JavaHandle, array: Dataframe, element_type: ElementType) -> None: ...
def update_switch_position(arg0: JavaHandle, arg1: str, arg2: bool) -> bool: ...
def validate(network: JavaHandle) -> ValidationLevel: ...
def write_network_area_diagram_svg(network: JavaHandle, svg_file: str, voltage_level_ids:  Union[str, List[str]], depth: int) -> None: ...
def write_single_line_diagram_svg(network: JavaHandle, container_id: str, svg_file: str) -> None: ...
def add_network_element_properties(network: JavaHandle, dataframe: Dataframe) -> None: ...
def remove_network_element_properties(network: JavaHandle, ids: List[str], properties: List[str]) -> None: ...
