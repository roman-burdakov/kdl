import os
import kdlc
import xml.etree.ElementTree as ET
import filecmp
import pytest

test_generated_dir = os.path.dirname(__file__) + "/generated"
test_resources_dir = os.path.dirname(__file__) + "/resources"


def test_unzip_workflow(my_setup):
    assert (
        kdlc.unzip_workflow(f"{test_resources_dir}/TestWorkflow.knwf") == "TestWorkflow"
    )
    assert os.path.isdir(f"{kdlc.INPUT_PATH}/TestWorkflow")


def test_extract_node_from_settings_xml_csv(my_setup):
    r = kdlc.Node(
        node_id="1",
        name="CSV Reader",
        factory="org.knime.base.node.io.csvreader.CSVReaderNodeFactory",
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    r.port_count = 1
    r.model = [
        {
            "url": (
                "/Users/jared/knime-workspace/Example Workflows/"
                "TheData/Misc/Demographics.csv"
            )
        },
        {"colDelimiter": ","},
        {"rowDelimiter": "%%00010"},
        {"quote": '"'},
        {"commentStart": "#"},
        {"hasRowHeader": True},
        {"hasColHeader": True},
        {"supportShortLines": False},
        {"limitRowsCount": -1, "data_type": "xlong"},
        {"skipFirstLinesCount": -1},
        {"characterSetName": "", "isnull": True},
        {"limitAnalysisCount": -1},
    ]

    assert r == kdlc.extract_node_from_settings_xml(
        "1", f"{test_resources_dir}/csv_settings.xml"
    )


def test_extract_node_from_settings_xml_cf(my_setup):
    res = kdlc.Node(
        node_id="1",
        name="Column Filter",
        factory=(
            "org.knime.base.node.preproc.filter."
            "column.DataColumnSpecFilterNodeFactory"
        ),
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    res.port_count = 1
    res.model = [
        {
            "column-filter": [
                {"filter-type": "STANDARD"},
                {
                    "included_names": [
                        {"array-size": 11},
                        {"0": "MaritalStatus"},
                        {"1": "Gender"},
                        {"2": "EstimatedYearlyIncome"},
                        {"3": "SentimentRating"},
                        {"4": "WebActivity"},
                        {"5": "Age"},
                        {"6": "Target"},
                        {"7": "Available401K"},
                        {"8": "CustomerValueSegment"},
                        {"9": "ChurnScore"},
                        {"10": "CallActivity"},
                    ]
                },
                {"excluded_names": [{"array-size": 1}, {"0": "NumberOfContracts"}]},
                {"enforce_option": "EnforceExclusion"},
                {
                    "name_pattern": [
                        {"pattern": ""},
                        {"type": "Wildcard"},
                        {"caseSensitive": True},
                    ]
                },
                {
                    "datatype": [
                        {
                            "typelist": [
                                {"org.knime.core.data.StringValue": False},
                                {"org.knime.core.data.IntValue": False},
                                {"org.knime.core.data.DoubleValue": False},
                                {"org.knime.core.data.BooleanValue": False},
                                {"org.knime.core.data.LongValue": False},
                                {
                                    (
                                        "org.knime.core.data." "date.DateAndTimeValue"
                                    ): False
                                },
                            ]
                        }
                    ]
                },
            ]
        }
    ]

    assert res == kdlc.extract_node_from_settings_xml(
        "1", f"{test_resources_dir}/cf_settings.xml"
    )


def test_extract_node_from_settings_xml_csv_var(my_setup):
    res = kdlc.Node(
        node_id="1",
        name="CSV Reader",
        factory="org.knime.base.node.io.csvreader.CSVReaderNodeFactory",
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    res.port_count = 1
    res.model = [
        {
            "url": "/Users/jared/knime-workspace/Example "
            "Workflows/TheData/Misc/Demographics.csv",
            "used_variable": "TEST",
            "exposed_variable": "TEST2",
        },
        {"colDelimiter": ","},
        {"rowDelimiter": "%%00010"},
        {"quote": '"'},
        {"commentStart": "#"},
        {"hasRowHeader": True},
        {"hasColHeader": True},
        {"supportShortLines": False},
        {"limitRowsCount": -1, "data_type": "xlong"},
        {"skipFirstLinesCount": -1},
        {"characterSetName": "", "isnull": True},
        {"limitAnalysisCount": -1},
    ]
    res.variables = [
        {"url": [{"used_variable": "TEST"}, {"exposed_variable": "TEST2"}]}
    ]

    assert res == kdlc.extract_node_from_settings_xml(
        "1", f"{test_resources_dir}/csv_var.xml"
    )


def test_extract_node_from_settings_xml_ttj_var(my_setup):
    res = kdlc.Node(
        node_id="1",
        name="Table to JSON",
        factory="org.knime.json.node.fromtable.TableToJsonNodeFactory",
        bundle_name="JSON related functionality for KNIME",
        bundle_symbolic_name="org.knime.json",
        bundle_version="3.7.1.v201901281201",
        feature_name="KNIME JSON-Processing",
        feature_symbolic_name="org.knime.features.json.feature.group",
        feature_version="3.7.1.v201901281201",
    )
    res.port_count = 1
    res.model = [
        {
            "selectedColumns": [
                {"filter-type": "STANDARD"},
                {
                    "included_names": [
                        {"array-size": 11},
                        {
                            "0": "MaritalStatus",
                            "used_variable": "TEST",
                            "exposed_variable": "TEST2",
                        },
                        {"1": "Gender"},
                        {"2": "EstimatedYearlyIncome"},
                        {"3": "SentimentRating"},
                        {"4": "WebActivity"},
                        {"5": "Age"},
                        {"6": "Target"},
                        {"7": "Available401K"},
                        {"8": "CustomerValueSegment"},
                        {"9": "ChurnScore"},
                        {"10": "CallActivity"},
                    ]
                },
                {"excluded_names": [{"array-size": 0}]},
                {"enforce_option": "EnforceExclusion"},
                {
                    "name_pattern": [
                        {"pattern": ""},
                        {"type": "Wildcard"},
                        {"caseSensitive": True},
                    ]
                },
                {
                    "datatype": [
                        {
                            "typelist": [
                                {"org.knime.core.data.StringValue": False},
                                {"org.knime.core.data.IntValue": False},
                                {"org.knime.core.data.DoubleValue": False},
                                {"org.knime.core.data.BooleanValue": False},
                                {"org.knime.core.data.LongValue": False},
                                {
                                    (
                                        "org.knime.core.data" ".date.DateAndTimeValue"
                                    ): False
                                },
                            ]
                        }
                    ]
                },
            ]
        },
        {"rowkey.key": "key"},
        {"direction": "KeepRows"},
        {"column.name.separator": "."},
        {"output.column.name": "JSON"},
        {"row.key.option": "omit"},
        {"column.names.as.path": False},
        {"remove.source.columns": False},
        {"output.boolean.asNumbers": False},
        {"missing.values.are.omitted": True},
    ]
    res.variables = [
        {
            "selectedColumns": [
                {
                    "included_names": [
                        {
                            "0": [
                                {"used_variable": "TEST"},
                                {"exposed_variable": "TEST2"},
                            ]
                        }
                    ]
                }
            ]
        }
    ]
    assert res == kdlc.extract_node_from_settings_xml(
        "1", f"{test_resources_dir}/ttj_var.xml"
    )


def test_extract_node_from_settings_xml_fail(my_setup):
    with pytest.raises(ValueError):
        kdlc.extract_node_from_settings_xml(
            "1", f"{test_resources_dir}/fail_settings.xml"
        )


def test_extract_node_from_settings_xml_fail_var(my_setup):
    with pytest.raises(ValueError):
        kdlc.extract_node_from_settings_xml(
            "1", f"{test_resources_dir}/fail_var_settings.xml"
        )


def test_extract_entry_tag_string(my_setup):
    tree = ET.fromstring('<entry key="node-name" type="xstring" value="CSV Reader"/>')

    result = {"node-name": "CSV Reader"}
    assert kdlc.extract_entry_tag(tree) == result


def test_extract_entry_tag_password(my_setup):
    tree = ET.fromstring('<entry key="node-name" type="xstring" value="CSV Reader"/>')

    result = {"node-name": "CSV Reader"}
    assert kdlc.extract_entry_tag(tree) == result


def test_extract_entry_tag_int(my_setup):
    tree = ET.fromstring('<entry key="password" type="xpassword" value="test" />')

    result = {"password": "test", "data_type": "xpassword"}
    assert kdlc.extract_entry_tag(tree) == result


def test_extract_entry_tag_long(my_setup):
    tree = ET.fromstring('<entry key="limitRowsCount" type="xlong" value="-1" />')

    result = {"limitRowsCount": -1, "data_type": "xlong"}
    assert kdlc.extract_entry_tag(tree) == result


def test_extract_entry_tag_short(my_setup):
    tree = ET.fromstring('<entry key="limitRowsCount" type="xshort" value="-1" />')

    result = {"limitRowsCount": -1, "data_type": "xshort"}
    assert kdlc.extract_entry_tag(tree) == result


def test_extract_entry_tag_float(my_setup):
    tree = ET.fromstring('<entry key="someFloat" type="xfloat" value="1.1" />')

    result = {"someFloat": 1.1}
    assert kdlc.extract_entry_tag(tree) == result


def test_extract_entry_tag_double(my_setup):
    tree = ET.fromstring('<entry key="someDouble" type="xdouble" value="1.1" />')

    result = {"someDouble": 1.1, "data_type": "xdouble"}
    assert kdlc.extract_entry_tag(tree) == result


def test_extract_entry_tag_infinity(my_setup):
    tree = ET.fromstring('<entry key="someDouble" type="xdouble" value="Infinity" />')

    result = {"someDouble": "Infinity", "data_type": "xdouble"}
    assert kdlc.extract_entry_tag(tree) == result


def test_extract_entry_tag_ninfinity(my_setup):
    tree = ET.fromstring('<entry key="someDouble" type="xdouble" value="-Infinity" />')

    result = {"someDouble": "-Infinity", "data_type": "xdouble"}
    assert kdlc.extract_entry_tag(tree) == result


def test_extract_entry_tag_char(my_setup):
    tree = ET.fromstring('<entry key="someChar" type="xchar" value="A" />')

    result = {"someChar": "A", "data_type": "xchar"}
    assert kdlc.extract_entry_tag(tree) == result


def test_extract_entry_tag_byte(my_setup):
    tree = ET.fromstring('<entry key="someByte" type="xbyte" value="A" />')

    result = {"someByte": "A", "data_type": "xbyte"}
    assert kdlc.extract_entry_tag(tree) == result


def test_extract_entry_tag_boolean_true(my_setup):
    tree = ET.fromstring('<entry key="hasRowHeader" type="xboolean" value="true" />')

    result = {"hasRowHeader": True}
    assert kdlc.extract_entry_tag(tree) == result


def test_extract_entry_tag_boolean_false(my_setup):
    tree = ET.fromstring('<entry key="hasRowHeader" type="xboolean" value="false" />')

    result = {"hasRowHeader": False}
    assert kdlc.extract_entry_tag(tree) == result


def test_extract_entry_tag_with_isnull(my_setup):
    tree = ET.fromstring(
        '<entry key="node-name" type="xstring" value="CSV Reader" isnull="true" />'
    )

    result = {"node-name": "CSV Reader", "isnull": True}
    assert kdlc.extract_entry_tag(tree) == result


def test_extract_entry_tag_error(my_setup):
    tree = ET.fromstring(
        '<entry key="node-name" type="invalid" value="CSV Reader" isnull="true" />'
    )
    with pytest.raises(Exception):
        kdlc.extract_entry_tag(tree)


def test_extract_config_tag(my_setup):
    tree = ET.fromstring(
        '<config xmlns="http://www.knime.org/2008/09/XMLConfig" '
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
        'xsi:schemaLocation="http://www.knime.org/2008/09/XMLConfig '
        'http://www.knime.org/XMLConfig_2008_09.xsd" key="settings.xml">'
        '<config key="column-filter"><entry key="filter-type" type="xstring" '
        'value="STANDARD" /></config></config>'
    )

    result = {"settings.xml": [{"column-filter": [{"filter-type": "STANDARD"}]}]}
    assert kdlc.extract_config_tag(tree) == result


def test_extract_config_tag_fail(my_setup):
    tree = ET.fromstring(
        '<config xmlns="http://www.knime.org/2008/09/XMLConfig" '
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
        'xsi:schemaLocation="http://www.knime.org/2008/09/XMLConfig '
        'http://www.knime.org/XMLConfig_2008_09.xsd" key="settings.xml">'
        '<fail key="column-filter"><entry key="filter-type" type="xstring" '
        'value="STANDARD" /></fail></config>'
    )
    with pytest.raises(Exception):
        kdlc.extract_config_tag(tree)


def test_extract_node_filenames(my_setup):
    result = [
        {
            "node_id": "1",
            "filename": "CSV Reader (#1)/settings.xml",
            "node_type": "NativeNode",
        },
        {
            "node_id": "2",
            "filename": "Table to JSON (#2)/settings.xml",
            "node_type": "NativeNode",
        },
        {
            "node_id": "3",
            "filename": "Column Filter (#3)/settings.xml",
            "node_type": "NativeNode",
        },
    ]
    assert kdlc.extract_node_filenames(f"{test_resources_dir}/workflow.knime") == result


def test_extract_node_filenames_meta(my_setup):
    result = [
        {
            "node_id": "1",
            "filename": "File Reader (#1)/settings.xml",
            "node_type": "NativeNode",
        },
        {
            "node_id": "7",
            "filename": "CSV Writer (#7)/settings.xml",
            "node_type": "NativeNode",
        },
        {
            "node_id": "8",
            "filename": "workflow_meta_2.knime",
            "node_type": "MetaNode",
            "name": "Metanode",
            "children": [
                {
                    "node_id": "2",
                    "filename": "Row Filter (#2)/settings.xml",
                    "node_type": "NativeNode",
                },
                {
                    "node_id": "3",
                    "filename": "Row Filter (#3)/settings.xml",
                    "node_type": "NativeNode",
                },
            ],
            "meta_in_ports": [{"1": "org.knime.core.node.BufferedDataTable"}],
            "meta_out_ports": [{"1": "org.knime.core.node.BufferedDataTable"}],
        },
    ]

    assert (
        kdlc.extract_node_filenames(f"{test_resources_dir}/workflow_meta.knime")
        == result
    )


def test_extract_nodes_from_filenames(my_setup):

    node_filename_list = [
        {"node_id": "1", "filename": "cf_settings.xml", "node_type": "NativeNode"},
        {
            "node_id": "8",
            "filename": "workflow_meta_4.knime",
            "node_type": "MetaNode",
            "name": "Metanode8",
            "children": [
                {
                    "node_id": "4",
                    "filename": "cf_settings.xml",
                    "node_type": "NativeNode",
                },
                {
                    "node_id": "6",
                    "filename": "workflow_meta_3.knime",
                    "node_type": "MetaNode",
                    "name": "Metanode6",
                    "children": [
                        {
                            "node_id": "4",
                            "filename": "cf_settings.xml",
                            "node_type": "NativeNode",
                        }
                    ],
                    "meta_in_ports": [{"1": "org.knime.core.node.BufferedDataTable"}],
                    "meta_out_ports": [{"1": "org.knime.core.node.BufferedDataTable"}],
                },
            ],
            "meta_in_ports": [{"1": "org.knime.core.node.BufferedDataTable"}],
            "meta_out_ports": [{"1": "org.knime.core.node.BufferedDataTable"}],
        },
    ]

    cf_model = [
        {
            "column-filter": [
                {"filter-type": "STANDARD"},
                {
                    "included_names": [
                        {"array-size": 11},
                        {"0": "MaritalStatus"},
                        {"1": "Gender"},
                        {"2": "EstimatedYearlyIncome"},
                        {"3": "SentimentRating"},
                        {"4": "WebActivity"},
                        {"5": "Age"},
                        {"6": "Target"},
                        {"7": "Available401K"},
                        {"8": "CustomerValueSegment"},
                        {"9": "ChurnScore"},
                        {"10": "CallActivity"},
                    ]
                },
                {"excluded_names": [{"array-size": 1}, {"0": "NumberOfContracts"}]},
                {"enforce_option": "EnforceExclusion"},
                {
                    "name_pattern": [
                        {"pattern": ""},
                        {"type": "Wildcard"},
                        {"caseSensitive": True},
                    ]
                },
                {
                    "datatype": [
                        {
                            "typelist": [
                                {"org.knime.core.data.StringValue": False},
                                {"org.knime.core.data.IntValue": False},
                                {"org.knime.core.data.DoubleValue": False},
                                {"org.knime.core.data.BooleanValue": False},
                                {"org.knime.core.data.LongValue": False},
                                {"org.knime.core.data.date.DateAndTimeValue": False},
                            ]
                        }
                    ]
                },
            ]
        }
    ]

    node1 = kdlc.Node(
        node_id="1",
        name="Column Filter",
        factory=(
            "org.knime.base.node.preproc.filter."
            "column.DataColumnSpecFilterNodeFactory"
        ),
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    node1.model = cf_model
    node1.port_count = 1

    node84 = kdlc.Node(
        node_id="8.4",
        name="Column Filter",
        factory=(
            "org.knime.base.node.preproc.filter."
            "column.DataColumnSpecFilterNodeFactory"
        ),
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    node84.model = cf_model
    node84.port_count = 1

    node864 = kdlc.Node(
        node_id="8.6.4",
        name="Column Filter",
        factory=(
            "org.knime.base.node.preproc.filter."
            "column.DataColumnSpecFilterNodeFactory"
        ),
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    node864.model = cf_model
    node864.port_count = 1

    connection0 = kdlc.Connection(
        connection_id=0,
        dest_id="4",
        dest_port="1",
        dest_node=node864,
        source_id="-1",
        source_port="0",
        source_node=kdlc.META_IN,
    )
    connection1 = kdlc.Connection(
        connection_id=1,
        dest_id="-1",
        dest_node=kdlc.META_OUT,
        dest_port="0",
        source_id="4",
        source_port="1",
        source_node=node864,
    )
    metanode86 = kdlc.MetaNode(
        node_id="8.6",
        name="Metanode6",
        children=[node864],
        connections=[connection0, connection1],
        meta_in_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
        meta_out_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
    )
    connection0 = kdlc.Connection(
        connection_id=0,
        dest_id="4",
        dest_node=node84,
        dest_port="1",
        source_id="-1",
        source_port="0",
        source_node=kdlc.META_IN,
    )
    connection1 = kdlc.Connection(
        connection_id=1,
        dest_id="6",
        dest_node=metanode86,
        dest_port="0",
        source_id="4",
        source_port="1",
        source_node=node84,
    )
    connection2 = kdlc.Connection(
        connection_id=2,
        dest_id="-1",
        dest_node=kdlc.META_OUT,
        dest_port="0",
        source_id="6",
        source_port="0",
        source_node=metanode86,
    )
    metanode8 = kdlc.MetaNode(
        node_id="8",
        name="Metanode8",
        children=[node84, metanode86],
        connections=[connection0, connection1, connection2],
        meta_in_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
        meta_out_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
    )

    result = [node1, metanode8]
    assert result == kdlc.extract_nodes_from_filenames(
        test_resources_dir, node_filename_list
    )


def test_flatten_node_list(my_setup):
    cf_model = [
        {
            "column-filter": [
                {"filter-type": "STANDARD"},
                {
                    "included_names": [
                        {"array-size": 11},
                        {"0": "MaritalStatus"},
                        {"1": "Gender"},
                        {"2": "EstimatedYearlyIncome"},
                        {"3": "SentimentRating"},
                        {"4": "WebActivity"},
                        {"5": "Age"},
                        {"6": "Target"},
                        {"7": "Available401K"},
                        {"8": "CustomerValueSegment"},
                        {"9": "ChurnScore"},
                        {"10": "CallActivity"},
                    ]
                },
                {"excluded_names": [{"array-size": 1}, {"0": "NumberOfContracts"}]},
                {"enforce_option": "EnforceExclusion"},
                {
                    "name_pattern": [
                        {"pattern": ""},
                        {"type": "Wildcard"},
                        {"caseSensitive": True},
                    ]
                },
                {
                    "datatype": [
                        {
                            "typelist": [
                                {"org.knime.core.data.StringValue": False},
                                {"org.knime.core.data.IntValue": False},
                                {"org.knime.core.data.DoubleValue": False},
                                {"org.knime.core.data.BooleanValue": False},
                                {"org.knime.core.data.LongValue": False},
                                {"org.knime.core.data.date.DateAndTimeValue": False},
                            ]
                        }
                    ]
                },
            ]
        }
    ]

    node1 = kdlc.Node(
        node_id="1",
        name="Column Filter",
        factory=(
            "org.knime.base.node.preproc.filter."
            "column.DataColumnSpecFilterNodeFactory"
        ),
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    node1.model = cf_model
    node1.port_count = 1

    node84 = kdlc.Node(
        node_id="8.4",
        name="Column Filter",
        factory=(
            "org.knime.base.node.preproc.filter."
            "column.DataColumnSpecFilterNodeFactory"
        ),
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    node84.model = cf_model
    node84.port_count = 1

    node864 = kdlc.Node(
        node_id="8.6.4",
        name="Column Filter",
        factory=(
            "org.knime.base.node.preproc.filter."
            "column.DataColumnSpecFilterNodeFactory"
        ),
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    node864.model = cf_model
    node864.port_count = 1

    connection0 = kdlc.Connection(
        connection_id=0,
        dest_id="4",
        dest_port="1",
        dest_node=node864,
        source_id="-1",
        source_port="0",
        source_node=kdlc.META_IN,
    )
    connection1 = kdlc.Connection(
        connection_id=1,
        dest_id="-1",
        dest_node=kdlc.META_OUT,
        dest_port="0",
        source_id="4",
        source_port="1",
        source_node=node864,
    )
    metanode86 = kdlc.MetaNode(
        node_id="8.6",
        name="Metanode6",
        children=[node864],
        connections=[connection0, connection1],
        meta_in_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
        meta_out_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
    )
    connection0 = kdlc.Connection(
        connection_id=0,
        dest_id="4",
        dest_node=node84,
        dest_port="1",
        source_id="-1",
        source_port="0",
        source_node=kdlc.META_IN,
    )
    connection1 = kdlc.Connection(
        connection_id=1,
        dest_id="6",
        dest_node=metanode86,
        dest_port="0",
        source_id="4",
        source_port="1",
        source_node=node84,
    )
    connection2 = kdlc.Connection(
        connection_id=2,
        dest_id="-1",
        dest_node=kdlc.META_OUT,
        dest_port="0",
        source_id="6",
        source_port="0",
        source_node=metanode86,
    )
    metanode8 = kdlc.MetaNode(
        node_id="8",
        name="Metanode8",
        children=[node84, metanode86],
        connections=[connection0, connection1, connection2],
        meta_in_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
        meta_out_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
    )

    input = [node1, metanode8]

    result = [node1, metanode8, node84, metanode86, node864]
    assert result == kdlc.flatten_node_list(input)


def test_unflatten_node_list(my_setup):
    cf_model = [
        {
            "column-filter": [
                {"filter-type": "STANDARD"},
                {
                    "included_names": [
                        {"array-size": 11},
                        {"0": "MaritalStatus"},
                        {"1": "Gender"},
                        {"2": "EstimatedYearlyIncome"},
                        {"3": "SentimentRating"},
                        {"4": "WebActivity"},
                        {"5": "Age"},
                        {"6": "Target"},
                        {"7": "Available401K"},
                        {"8": "CustomerValueSegment"},
                        {"9": "ChurnScore"},
                        {"10": "CallActivity"},
                    ]
                },
                {"excluded_names": [{"array-size": 1}, {"0": "NumberOfContracts"}]},
                {"enforce_option": "EnforceExclusion"},
                {
                    "name_pattern": [
                        {"pattern": ""},
                        {"type": "Wildcard"},
                        {"caseSensitive": True},
                    ]
                },
                {
                    "datatype": [
                        {
                            "typelist": [
                                {"org.knime.core.data.StringValue": False},
                                {"org.knime.core.data.IntValue": False},
                                {"org.knime.core.data.DoubleValue": False},
                                {"org.knime.core.data.BooleanValue": False},
                                {"org.knime.core.data.LongValue": False},
                                {"org.knime.core.data.date.DateAndTimeValue": False},
                            ]
                        }
                    ]
                },
            ]
        }
    ]

    node1 = kdlc.Node(
        node_id="1",
        name="Column Filter",
        factory=(
            "org.knime.base.node.preproc.filter."
            "column.DataColumnSpecFilterNodeFactory"
        ),
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    node1.model = cf_model
    node1.port_count = 1

    node84 = kdlc.Node(
        node_id="8.4",
        name="Column Filter",
        factory=(
            "org.knime.base.node.preproc.filter."
            "column.DataColumnSpecFilterNodeFactory"
        ),
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    node84.model = cf_model
    node84.port_count = 1

    node864 = kdlc.Node(
        node_id="8.6.4",
        name="Column Filter",
        factory=(
            "org.knime.base.node.preproc.filter."
            "column.DataColumnSpecFilterNodeFactory"
        ),
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    node864.model = cf_model
    node864.port_count = 1

    connection0 = kdlc.Connection(
        connection_id=0, dest_id="4", dest_port="1", source_id="-1", source_port="1"
    )
    connection1 = kdlc.Connection(
        connection_id=1, dest_id="-1", dest_port="1", source_id="4", source_port="1"
    )
    metanode86 = kdlc.MetaNode(
        node_id="8.6",
        name="Metanode6",
        children=[node864],
        connections=[connection0, connection1],
        meta_in_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
        meta_out_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
    )
    connection0 = kdlc.Connection(
        connection_id=0, dest_id="4", dest_port="1", source_id="-1", source_port="1"
    )
    connection1 = kdlc.Connection(
        connection_id=1, dest_id="6", dest_port="1", source_id="4", source_port="1"
    )
    connection2 = kdlc.Connection(
        connection_id=2, dest_id="-1", dest_port="1", source_id="6", source_port="1"
    )
    metanode8 = kdlc.MetaNode(
        node_id="8",
        name="Metanode8",
        children=[node84, metanode86],
        connections=[connection0, connection1, connection2],
        meta_in_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
        meta_out_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
    )
    input = [node1, metanode8, node84, metanode86, node864]

    result = [node1, metanode8]
    assert result == kdlc.unflatten_node_list(input)


def test_normalize_connections(my_setup):
    cf_model = [
        {
            "column-filter": [
                {"filter-type": "STANDARD"},
                {
                    "included_names": [
                        {"array-size": 11},
                        {"0": "MaritalStatus"},
                        {"1": "Gender"},
                        {"2": "EstimatedYearlyIncome"},
                        {"3": "SentimentRating"},
                        {"4": "WebActivity"},
                        {"5": "Age"},
                        {"6": "Target"},
                        {"7": "Available401K"},
                        {"8": "CustomerValueSegment"},
                        {"9": "ChurnScore"},
                        {"10": "CallActivity"},
                    ]
                },
                {"excluded_names": [{"array-size": 1}, {"0": "NumberOfContracts"}]},
                {"enforce_option": "EnforceExclusion"},
                {
                    "name_pattern": [
                        {"pattern": ""},
                        {"type": "Wildcard"},
                        {"caseSensitive": True},
                    ]
                },
                {
                    "datatype": [
                        {
                            "typelist": [
                                {"org.knime.core.data.StringValue": False},
                                {"org.knime.core.data.IntValue": False},
                                {"org.knime.core.data.DoubleValue": False},
                                {"org.knime.core.data.BooleanValue": False},
                                {"org.knime.core.data.LongValue": False},
                                {"org.knime.core.data.date.DateAndTimeValue": False},
                            ]
                        }
                    ]
                },
            ]
        }
    ]

    node1 = kdlc.Node(
        node_id="1",
        name="Column Filter",
        factory=(
            "org.knime.base.node.preproc.filter."
            "column.DataColumnSpecFilterNodeFactory"
        ),
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    node1.model = cf_model
    node1.port_count = 1

    node84 = kdlc.Node(
        node_id="8.4",
        name="Column Filter",
        factory=(
            "org.knime.base.node.preproc.filter."
            "column.DataColumnSpecFilterNodeFactory"
        ),
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    node84.model = cf_model
    node84.port_count = 1

    node864 = kdlc.Node(
        node_id="8.6.4",
        name="Column Filter",
        factory=(
            "org.knime.base.node.preproc.filter."
            "column.DataColumnSpecFilterNodeFactory"
        ),
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    node864.model = cf_model
    node864.port_count = 1

    connection_m_in_864 = kdlc.Connection(
        connection_id=0, dest_id="4", dest_port="1", source_id="-1", source_port="1"
    )
    connection_864_m_out = kdlc.Connection(
        connection_id=1, dest_id="-1", dest_port="1", source_id="4", source_port="1"
    )
    metanode86 = kdlc.MetaNode(
        node_id="8.6",
        name="Metanode6",
        children=[node864],
        connections=[connection_m_in_864, connection_864_m_out],
        meta_in_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
        meta_out_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
    )
    connection_m_in_84 = kdlc.Connection(
        connection_id=0, dest_id="4", dest_port="1", source_id="-1", source_port="1"
    )
    connection_84_86 = kdlc.Connection(
        connection_id=1, dest_id="6", dest_port="1", source_id="4", source_port="1"
    )
    connection_86_m_out = kdlc.Connection(
        connection_id=2, dest_id="-1", dest_port="1", source_id="6", source_port="1"
    )
    metanode8 = kdlc.MetaNode(
        node_id="8",
        name="Metanode8",
        children=[node84, metanode86],
        connections=[connection_m_in_84, connection_84_86, connection_86_m_out],
        meta_in_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
        meta_out_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
    )

    connection_1_8 = kdlc.Connection(
        connection_id=0, dest_id="8", dest_port="1", source_id="1", source_port="1"
    )

    # Result data begins

    res_connection_m_in_864 = kdlc.Connection(
        connection_id=0,
        dest_id="4",
        dest_port="1",
        dest_node=node864,
        source_id="-1",
        source_port="0",
        source_node=kdlc.META_IN,
    )
    res_connection_864_m_out = kdlc.Connection(
        connection_id=1,
        dest_id="-1",
        dest_node=kdlc.META_OUT,
        dest_port="0",
        source_id="4",
        source_port="1",
        source_node=node864,
    )
    res_metanode86 = kdlc.MetaNode(
        node_id="8.6",
        name="Metanode6",
        children=[node864],
        connections=[res_connection_m_in_864, res_connection_864_m_out],
        meta_in_ports=[{"0": "org.knime.core.node.BufferedDataTable"}],
        meta_out_ports=[{"0": "org.knime.core.node.BufferedDataTable"}],
    )
    res_connection_m_in_84 = kdlc.Connection(
        connection_id=0,
        dest_id="4",
        dest_node=node84,
        dest_port="1",
        source_id="-1",
        source_port="0",
        source_node=kdlc.META_IN,
    )
    res_connection_84_86 = kdlc.Connection(
        connection_id=1,
        dest_id="6",
        dest_node=res_metanode86,
        dest_port="0",
        source_id="4",
        source_port="1",
        source_node=node84,
    )
    res_connection_86_m_out = kdlc.Connection(
        connection_id=2,
        dest_id="-1",
        dest_node=kdlc.META_OUT,
        dest_port="0",
        source_id="6",
        source_port="0",
        source_node=res_metanode86,
    )
    res_metanode8 = kdlc.MetaNode(
        node_id="8",
        name="Metanode8",
        children=[node84, metanode86],
        connections=[
            res_connection_m_in_84,
            res_connection_84_86,
            res_connection_86_m_out,
        ],
        meta_in_ports=[{"0": "org.knime.core.node.BufferedDataTable"}],
        meta_out_ports=[{"0": "org.knime.core.node.BufferedDataTable"}],
    )

    res_connection_1_8 = kdlc.Connection(
        connection_id=0,
        dest_id="8",
        dest_port="0",
        dest_node=res_metanode8,
        source_id="1",
        source_port="1",
        source_node=node1,
    )

    in_nodes = [node1, metanode8]
    in_connections = [connection_1_8]

    res_connections = [res_connection_1_8]
    res_nodes = [node1, res_metanode8]

    kdlc.normalize_connections(in_nodes, in_connections)

    assert res_nodes == in_nodes
    assert res_connections == in_connections


def test_extract_connections(my_setup):
    node1 = kdlc.Node(
        node_id="1",
        name="1",
        factory="1",
        bundle_name="1",
        bundle_symbolic_name="1",
        bundle_version="1",
        feature_name="1",
        feature_symbolic_name="1",
        feature_version="1",
    )
    node2 = kdlc.Node(
        node_id="2",
        name="2",
        factory="2",
        bundle_name="2",
        bundle_symbolic_name="2",
        bundle_version="2",
        feature_name="2",
        feature_symbolic_name="2",
        feature_version="2",
    )
    node3 = kdlc.Node(
        node_id="3",
        name="3",
        factory="3",
        bundle_name="3",
        bundle_symbolic_name="3",
        bundle_version="3",
        feature_name="3",
        feature_symbolic_name="3",
        feature_version="3",
    )
    connection1 = kdlc.Connection(
        connection_id=0,
        source_id="1",
        source_node=node1,
        dest_id="3",
        dest_node=node3,
        source_port="1",
        dest_port="1",
    )
    connection2 = kdlc.Connection(
        connection_id=1,
        source_id="3",
        source_node=node3,
        dest_id="2",
        dest_node=node2,
        source_port="1",
        dest_port="1",
    )
    result = [connection1, connection2]
    assert (
        kdlc.extract_connections(
            f"{test_resources_dir}/workflow.knime", [node1, node2, node3]
        )
        == result
    )


def test_extract_var_connections(my_setup):
    node1 = kdlc.Node(
        node_id="1",
        name="1",
        factory="1",
        bundle_name="1",
        bundle_symbolic_name="1",
        bundle_version="1",
        feature_name="1",
        feature_symbolic_name="1",
        feature_version="1",
    )
    node2 = kdlc.Node(
        node_id="2",
        name="2",
        factory="2",
        bundle_name="2",
        bundle_symbolic_name="2",
        bundle_version="2",
        feature_name="2",
        feature_symbolic_name="2",
        feature_version="2",
    )
    node3 = kdlc.Node(
        node_id="3",
        name="3",
        factory="3",
        bundle_name="3",
        bundle_symbolic_name="3",
        bundle_version="3",
        feature_name="3",
        feature_symbolic_name="3",
        feature_version="3",
    )
    connection1 = kdlc.Connection(
        connection_id=0,
        source_id="1",
        source_node=node1,
        dest_id="3",
        dest_node=node3,
        source_port="1",
        dest_port="1",
    )
    connection2 = kdlc.Connection(
        connection_id=1,
        source_id="3",
        source_node=node3,
        dest_id="2",
        dest_node=node2,
        source_port="1",
        dest_port="1",
    )
    connection3 = kdlc.VariableConnection(
        connection_id=2,
        source_id="3",
        source_node=node3,
        dest_id="2",
        dest_node=node2,
        source_port="0",
        dest_port="0",
    )
    result = [connection1, connection2, connection3]
    assert (
        kdlc.extract_connections(
            f"{test_resources_dir}/workflow_var_connection.knime", [node1, node2, node3]
        )
        == result
    )


def test_extract_var_connections_meta(my_setup):
    out_connection = kdlc.VariableConnection(
        connection_id=0,
        source_id="1",
        source_port="0",
        dest_id="-1",
        dest_node=kdlc.META_OUT,
        dest_port="0",
    )
    node14 = kdlc.MetaNode(
        node_id="14",
        name="14",
        children=[],
        connections=[out_connection],
        meta_in_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
        meta_out_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
    )
    in_connection = kdlc.VariableConnection(
        connection_id=0,
        source_id="-1",
        source_port="0",
        source_node=kdlc.META_IN,
        dest_id="1",
        dest_port="0",
    )
    node15 = kdlc.MetaNode(
        node_id="15",
        name="15",
        children=[],
        connections=[in_connection],
        meta_in_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
        meta_out_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
    )
    connection14_15 = kdlc.VariableConnection(
        connection_id=0,
        source_id="14",
        source_node=node14,
        dest_id="15",
        dest_node=node15,
        source_port="0",
        dest_port="0",
    )
    result = [connection14_15]
    assert (
        kdlc.extract_connections(
            f"{test_resources_dir}/workflow_var_connection_meta.knime", [node14, node15]
        )
        == result
    )


def test_extract_global_wf_variables(my_setup):
    result = [{"test1": "test"}, {"test2": 1}, {"test3": 1.1}]
    assert result == kdlc.extract_global_wf_variables(
        f"{test_resources_dir}/workflow_var.knime"
    )


def test_create_node_settings_from_template_csv(my_setup):
    node = kdlc.Node(
        node_id="1",
        name="CSV Reader",
        factory="org.knime.base.node.io.csvreader.CSVReaderNodeFactory",
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    node.port_count = 1
    node.model = [
        {
            "url": (
                "/Users/jared/knime-workspace/Example Workflows/"
                "TheData/Misc/Demographics.csv"
            )
        },
        {"colDelimiter": ","},
        {"rowDelimiter": "%%00010"},
        {"quote": '"'},
        {"commentStart": "#"},
        {"hasRowHeader": True},
        {"hasColHeader": True},
        {"supportShortLines": False},
        {"limitRowsCount": -1, "data_type": "xlong"},
        {"skipFirstLinesCount": -1},
        {"characterSetName": "", "isnull": True},
        {"limitAnalysisCount": -1},
    ]
    expected_result = ET.parse(f"{test_resources_dir}/csv_settings.xml")
    expected_result_flattened = [i.tag for i in expected_result.iter()]

    result = kdlc.create_node_settings_from_template(node)
    result_flattened = [i.tag for i in result.iter()]

    assert result_flattened == expected_result_flattened


def test_create_node_settings_from_template_cf(my_setup):
    node = kdlc.Node(
        node_id="1",
        name="Column Filter",
        factory=(
            "org.knime.base.node.preproc.filter."
            "column.DataColumnSpecFilterNodeFactory"
        ),
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    node.port_count = 1
    node.model = [
        {
            "column-filter": [
                {"filter-type": "STANDARD"},
                {
                    "included_names": [
                        {"array-size": 11},
                        {"0": "MaritalStatus"},
                        {"1": "Gender"},
                        {"2": "EstimatedYearlyIncome"},
                        {"3": "SentimentRating"},
                        {"4": "WebActivity"},
                        {"5": "Age"},
                        {"6": "Target"},
                        {"7": "Available401K"},
                        {"8": "CustomerValueSegment"},
                        {"9": "ChurnScore"},
                        {"10": "CallActivity"},
                    ]
                },
                {"excluded_names": [{"array-size": 1}, {"0": "NumberOfContracts"}]},
                {"enforce_option": "EnforceExclusion"},
                {
                    "name_pattern": [
                        {"pattern": ""},
                        {"type": "Wildcard"},
                        {"caseSensitive": True},
                    ]
                },
                {
                    "datatype": [
                        {
                            "typelist": [
                                {"org.knime.core.data.StringValue": False},
                                {"org.knime.core.data.IntValue": False},
                                {"org.knime.core.data.DoubleValue": False},
                                {"org.knime.core.data.BooleanValue": False},
                                {"org.knime.core.data.LongValue": False},
                                {
                                    (
                                        "org.knime.core.data." "date.DateAndTimeValue"
                                    ): False
                                },
                            ]
                        }
                    ]
                },
            ]
        }
    ]

    expected_result = ET.parse(f"{test_resources_dir}/cf_settings.xml")
    expected_result_flattened = [i.tag for i in expected_result.iter()]

    result = kdlc.create_node_settings_from_template(node)
    result_flattened = [i.tag for i in result.iter()]

    assert result_flattened == expected_result_flattened


def test_create_workflow_knime_from_template(my_setup):
    node1 = kdlc.Node(
        node_id="1",
        name="CSV Reader",
        factory="org.knime.base.node.io.csvreader.CSVReaderNodeFactory",
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    node1.port_count = 1
    node1.model = [
        {
            "url": (
                "/Users/jared/knime-workspace/Example Workflows/"
                "TheData/Misc/Demographics.csv"
            )
        },
        {"colDelimiter": ","},
        {"rowDelimiter": "%%00010"},
        {"quote": '"'},
        {"commentStart": "#"},
        {"hasRowHeader": True},
        {"hasColHeader": True},
        {"supportShortLines": False},
        {"limitRowsCount": -1, "data_type": "xlong"},
        {"skipFirstLinesCount": -1},
        {"characterSetName": "", "isnull": True},
        {"limitAnalysisCount": -1},
    ]
    node2 = kdlc.Node(
        node_id="2",
        name="Column Filter",
        factory=(
            "org.knime.base.node.preproc.filter."
            "column.DataColumnSpecFilterNodeFactory"
        ),
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    node2.port_count = 1
    node2.model = [
        {
            "column-filter": [
                {"filter-type": "STANDARD"},
                {
                    "included_names": [
                        {"array-size": 11},
                        {"0": "MaritalStatus"},
                        {"1": "Gender"},
                        {"2": "EstimatedYearlyIncome"},
                        {"3": "SentimentRating"},
                        {"4": "WebActivity"},
                        {"5": "Age"},
                        {"6": "Target"},
                        {"7": "Available401K"},
                        {"8": "CustomerValueSegment"},
                        {"9": "ChurnScore"},
                        {"10": "CallActivity"},
                    ]
                },
                {"excluded_names": [{"array-size": 1}, {"0": "NumberOfContracts"}]},
                {"enforce_option": "EnforceExclusion"},
                {
                    "name_pattern": [
                        {"pattern": ""},
                        {"type": "Wildcard"},
                        {"caseSensitive": True},
                    ]
                },
                {
                    "datatype": [
                        {
                            "typelist": [
                                {"org.knime.core.data.StringValue": False},
                                {"org.knime.core.data.IntValue": False},
                                {"org.knime.core.data.DoubleValue": False},
                                {"org.knime.core.data.BooleanValue": False},
                                {"org.knime.core.data.LongValue": False},
                                {
                                    (
                                        "org.knime.core.data." "date.DateAndTimeValue"
                                    ): False
                                },
                            ]
                        }
                    ]
                },
            ]
        }
    ]
    node3 = kdlc.Node(
        node_id="3",
        name="Table to JSON",
        factory="org.knime.json.node.fromtable.TableToJsonNodeFactory",
        bundle_name="JSON related functionality for KNIME",
        bundle_symbolic_name="org.knime.json",
        bundle_version="3.7.1.v201901281201",
        feature_name="KNIME JSON-Processing",
        feature_symbolic_name="org.knime.features.json.feature.group",
        feature_version="3.7.1.v201901281201",
    )
    node3.port_count = 1
    node3.model = [
        {
            "selectedColumns": [
                {"filter-type": "STANDARD"},
                {
                    "included_names": [
                        {"array-size": 11},
                        {"0": "MaritalStatus"},
                        {"1": "Gender"},
                        {"2": "EstimatedYearlyIncome"},
                        {"3": "SentimentRating"},
                        {"4": "WebActivity"},
                        {"5": "Age"},
                        {"6": "Target"},
                        {"7": "Available401K"},
                        {"8": "CustomerValueSegment"},
                        {"9": "ChurnScore"},
                        {"10": "CallActivity"},
                    ]
                },
                {"excluded_names": [{"array-size": 0}]},
                {"enforce_option": "EnforceExclusion"},
                {
                    "name_pattern": [
                        {"pattern": ""},
                        {"type": "Wildcard"},
                        {"caseSensitive": True},
                    ]
                },
                {
                    "datatype": [
                        {
                            "typelist": [
                                {"org.knime.core.data.StringValue": False},
                                {"org.knime.core.data.IntValue": False},
                                {"org.knime.core.data.DoubleValue": False},
                                {"org.knime.core.data.BooleanValue": False},
                                {"org.knime.core.data.LongValue": False},
                                {
                                    (
                                        "org.knime.core.data" ".date.DateAndTimeValue"
                                    ): False
                                },
                            ]
                        }
                    ]
                },
            ]
        },
        {"rowkey.key": "key"},
        {"direction": "KeepRows"},
        {"column.name.separator": "."},
        {"output.column.name": "JSON"},
        {"row.key.option": "omit"},
        {"column.names.as.path": False},
        {"remove.source.columns": False},
        {"output.boolean.asNumbers": False},
        {"missing.values.are.omitted": True},
    ]
    node_list = [node1, node2, node3]
    connection_list = [
        kdlc.Connection(
            connection_id=0,
            source_id="1",
            source_port="1",
            source_node=node1,
            dest_id="3",
            dest_port="1",
            dest_node=node3,
        ),
        kdlc.Connection(
            connection_id=1,
            source_id="3",
            source_port="1",
            source_node=node3,
            dest_id="2",
            dest_port="1",
            dest_node=node2,
        ),
    ]
    global_variable_list = []
    workflow = kdlc.Workflow(
        connections=connection_list, variables=global_variable_list
    )
    expected_result = ET.parse(f"{test_resources_dir}/workflow.knime")
    expected_result_flattened = [i.tag for i in expected_result.iter()]

    result = kdlc.create_workflow_knime_from_template(node_list, workflow)
    result_flattened = [i.tag for i in result.iter()]

    assert result_flattened == expected_result_flattened


def test_create_metanode_workflow_knime_from_template(my_setup):
    node864 = kdlc.Node(
        node_id="8.6.4",
        name="Column Filter",
        factory=(
            "org.knime.base.node.preproc.filter."
            "column.DataColumnSpecFilterNodeFactory"
        ),
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    node864.model = [
        {
            "column-filter": [
                {"filter-type": "STANDARD"},
                {
                    "included_names": [
                        {"array-size": 11},
                        {"0": "MaritalStatus"},
                        {"1": "Gender"},
                        {"2": "EstimatedYearlyIncome"},
                        {"3": "SentimentRating"},
                        {"4": "WebActivity"},
                        {"5": "Age"},
                        {"6": "Target"},
                        {"7": "Available401K"},
                        {"8": "CustomerValueSegment"},
                        {"9": "ChurnScore"},
                        {"10": "CallActivity"},
                    ]
                },
                {"excluded_names": [{"array-size": 1}, {"0": "NumberOfContracts"}]},
                {"enforce_option": "EnforceExclusion"},
                {
                    "name_pattern": [
                        {"pattern": ""},
                        {"type": "Wildcard"},
                        {"caseSensitive": True},
                    ]
                },
                {
                    "datatype": [
                        {
                            "typelist": [
                                {"org.knime.core.data.StringValue": False},
                                {"org.knime.core.data.IntValue": False},
                                {"org.knime.core.data.DoubleValue": False},
                                {"org.knime.core.data.BooleanValue": False},
                                {"org.knime.core.data.LongValue": False},
                                {"org.knime.core.data.date.DateAndTimeValue": False},
                            ]
                        }
                    ]
                },
            ]
        }
    ]
    node864.port_count = 1

    connection_m_in_864 = kdlc.Connection(
        connection_id=0,
        dest_id="4",
        dest_port="1",
        dest_node=node864,
        source_id="-1",
        source_port="0",
        source_node=kdlc.META_IN,
    )
    connection_864_m_out = kdlc.Connection(
        connection_id=1,
        dest_id="-1",
        dest_node=kdlc.META_OUT,
        dest_port="0",
        source_id="4",
        source_port="1",
        source_node=node864,
    )
    metanode86 = kdlc.MetaNode(
        node_id="8.6",
        name="Metanode6",
        children=[node864],
        connections=[connection_m_in_864, connection_864_m_out],
        meta_in_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
        meta_out_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
    )

    expected_result = ET.parse(f"{test_resources_dir}/workflow_meta_5.knime")
    expected_result_flattened = [i.tag for i in expected_result.iter()]

    result = kdlc.create_metanode_workflow_knime_from_template(metanode86)
    result_flattened = [i.tag for i in result.iter()]

    assert result_flattened == expected_result_flattened


def test_create_node_files(my_setup):
    node21 = kdlc.Node(
        node_id="2.1",
        name="Column Filter",
        factory=(
            "org.knime.base.node.preproc.filter."
            "column.DataColumnSpecFilterNodeFactory"
        ),
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    node21.model = [
        {
            "column-filter": [
                {"filter-type": "STANDARD"},
                {
                    "included_names": [
                        {"array-size": 11},
                        {"0": "MaritalStatus"},
                        {"1": "Gender"},
                        {"2": "EstimatedYearlyIncome"},
                        {"3": "SentimentRating"},
                        {"4": "WebActivity"},
                        {"5": "Age"},
                        {"6": "Target"},
                        {"7": "Available401K"},
                        {"8": "CustomerValueSegment"},
                        {"9": "ChurnScore"},
                        {"10": "CallActivity"},
                    ]
                },
                {"excluded_names": [{"array-size": 1}, {"0": "NumberOfContracts"}]},
                {"enforce_option": "EnforceExclusion"},
                {
                    "name_pattern": [
                        {"pattern": ""},
                        {"type": "Wildcard"},
                        {"caseSensitive": True},
                    ]
                },
                {
                    "datatype": [
                        {
                            "typelist": [
                                {"org.knime.core.data.StringValue": False},
                                {"org.knime.core.data.IntValue": False},
                                {"org.knime.core.data.DoubleValue": False},
                                {"org.knime.core.data.BooleanValue": False},
                                {"org.knime.core.data.LongValue": False},
                                {"org.knime.core.data.date.DateAndTimeValue": False},
                            ]
                        }
                    ]
                },
            ]
        }
    ]
    node21.port_count = 1

    connection_m_in_21 = kdlc.Connection(
        connection_id=0,
        dest_id="1",
        dest_port="1",
        dest_node=node21,
        source_id="-1",
        source_port="0",
        source_node=kdlc.META_IN,
    )
    connection_21_m_out = kdlc.Connection(
        connection_id=1,
        dest_id="-1",
        dest_node=kdlc.META_OUT,
        dest_port="0",
        source_id="2",
        source_port="1",
        source_node=node21,
    )
    metanode2 = kdlc.MetaNode(
        node_id="1",
        name="Metanode2",
        children=[node21],
        connections=[connection_m_in_21, connection_21_m_out],
        meta_in_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
        meta_out_ports=[{"1": "org.knime.core.node.BufferedDataTable"}],
    )
    node1 = kdlc.Node(
        node_id="1",
        name="CSV Reader",
        factory="org.knime.base.node.io.csvreader.CSVReaderNodeFactory",
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    node1.port_count = 1
    node1.model = [
        {
            "url": (
                "/Users/jared/knime-workspace/Example Workflows/"
                "TheData/Misc/Demographics.csv"
            )
        },
        {"colDelimiter": ","},
        {"rowDelimiter": "%%00010"},
        {"quote": '"'},
        {"commentStart": "#"},
        {"hasRowHeader": True},
        {"hasColHeader": True},
        {"supportShortLines": False},
        {"limitRowsCount": -1, "data_type": "xlong"},
        {"skipFirstLinesCount": -1},
        {"characterSetName": "", "isnull": True},
        {"limitAnalysisCount": -1},
    ]
    node_list = [node1, metanode2]

    kdlc.create_node_files(f"{test_generated_dir}/test", node_list)

    expected_result_1 = ET.parse(f"{test_resources_dir}/csv_settings.xml")
    expected_result_flattened_1 = [i.tag for i in expected_result_1.iter()]
    result_1 = ET.parse(f"{test_generated_dir}/test/CSV Reader (#1)/settings.xml")
    result_flattened_1 = [i.tag for i in result_1.iter()]

    expected_result_2 = ET.parse(f"{test_resources_dir}/cf_settings.xml")
    expected_result_flattened_2 = [i.tag for i in expected_result_2.iter()]
    result_2 = ET.parse(
        f"{test_generated_dir}/test/Metanode2 (#1)/Column Filter (#1)/settings.xml"
    )
    result_flattened_2 = [i.tag for i in result_2.iter()]

    expected_result_3 = ET.parse(f"{test_resources_dir}/workflow_meta_6.knime")
    expected_result_flattened_3 = [i.tag for i in expected_result_3.iter()]
    result_3 = ET.parse(f"{test_generated_dir}/test/Metanode2 (#1)/workflow.knime")
    result_flattened_3 = [i.tag for i in result_3.iter()]
    assert result_flattened_1 == expected_result_flattened_1
    assert result_flattened_2 == expected_result_flattened_2
    assert result_flattened_3 == expected_result_flattened_3


def test_set_class_for_global_variables_str(my_setup):
    variables = [{"test1": "test"}, {"test2": 2}, {"test3": 3.0}]
    result = [
        {"test1": "test", "var_class": "STRING"},
        {"test2": 2, "var_class": "INTEGER"},
        {"test3": 3.0, "var_class": "DOUBLE"},
    ]
    kdlc.set_class_for_global_variables(variables)
    assert result == variables


def test_set_entry_element_type_string(my_setup):
    entry = {"url": "/Path/To/TheData/Demographics.csv"}
    result = {"url": "/Path/To/TheData/Demographics.csv", "data_type": "xstring"}
    kdlc.set_entry_element_type(entry)
    assert result == entry


def test_set_entry_element_type_password(my_setup):
    entry = {"password": "test", "data_type": "xpassword"}
    result = {"password": "test", "data_type": "xpassword"}
    kdlc.set_entry_element_type(entry)
    assert result == entry


def test_set_entry_element_type_int(my_setup):
    entry = {"skipFirstLinesCount": -1}
    result = {"skipFirstLinesCount": "-1", "data_type": "xint"}
    kdlc.set_entry_element_type(entry)
    assert result == entry


def test_set_entry_element_type_long(my_setup):
    entry = {"limitRowsCount": -1, "data_type": "xlong"}
    result = {"limitRowsCount": "-1", "data_type": "xlong"}
    kdlc.set_entry_element_type(entry)
    assert result == entry


def test_set_entry_element_type_short(my_setup):
    entry = {"limitRowsCount": -1, "data_type": "xshort"}
    result = {"limitRowsCount": "-1", "data_type": "xshort"}
    kdlc.set_entry_element_type(entry)
    assert result == entry


def test_set_entry_element_type_float(my_setup):
    entry = {"someFloat": 1.1}
    result = {"someFloat": "1.1", "data_type": "xfloat"}
    kdlc.set_entry_element_type(entry)
    assert result == entry


def test_set_entry_element_type_double(my_setup):
    entry = {"someDouble": 1.1, "data_type": "xdouble"}
    result = {"someDouble": "1.1", "data_type": "xdouble"}
    kdlc.set_entry_element_type(entry)
    assert result == entry


def test_set_entry_element_type_char(my_setup):
    entry = {"someChar": "A", "data_type": "xchar"}
    result = {"someChar": "A", "data_type": "xchar"}
    kdlc.set_entry_element_type(entry)
    assert result == entry


def test_set_entry_element_type_byte(my_setup):
    entry = {"someByte": "A", "data_type": "xbyte"}
    result = {"someByte": "A", "data_type": "xbyte"}
    kdlc.set_entry_element_type(entry)
    assert result == entry


def test_set_entry_element_type_boolean_true(my_setup):
    entry = {"hasRowHeader": True}
    result = {"hasRowHeader": "true", "data_type": "xboolean"}
    kdlc.set_entry_element_type(entry)
    assert result == entry


def test_set_entry_element_type_boolean_false(my_setup):
    entry = {"hasRowHeader": False}
    result = {"hasRowHeader": "false", "data_type": "xboolean"}
    kdlc.set_entry_element_type(entry)
    assert result == entry


def test_set_entry_element_type_fail(my_setup):
    entry = {"test": None}
    with pytest.raises(Exception):
        kdlc.set_entry_element_type(entry)


def test_set_config_element_type(my_setup):
    config = {"included_names": [{"array-size": 12}, {"0": "MaritalStatus"}]}
    result = {
        "included_names": [
            {"array-size": "12", "data_type": "xint"},
            {"0": "MaritalStatus", "data_type": "xstring"},
        ],
        "data_type": "config",
    }
    kdlc.set_config_element_type(config)
    assert result == config


def test_save_node_settings_xml(my_setup):
    tree = ET.parse(f"{test_resources_dir}/csv_settings.xml")
    kdlc.save_node_settings_xml(tree, f"{test_generated_dir}/settings.xml")
    assert filecmp.cmp(
        f"{test_resources_dir}/csv_settings.xml", f"{test_generated_dir}/settings.xml"
    )


def test_save_workflow_knime(my_setup):
    tree = ET.parse(f"{test_resources_dir}/workflow.knime")
    kdlc.save_workflow_knime(tree, test_generated_dir)
    assert filecmp.cmp(
        f"{test_resources_dir}/workflow.knime", f"{test_generated_dir}/workflow.knime"
    )


def test_create_output_workflow(mocker):
    workflow_name = "test"

    make_archive = mocker.MagicMock()
    mocker.patch("shutil.make_archive", new=make_archive)

    rename = mocker.MagicMock()
    mocker.patch("os.rename", new=rename)

    kdlc.create_output_workflow(workflow_name)
    make_archive.assert_called_with(workflow_name, "zip", kdlc.OUTPUT_PATH)
    rename.assert_called_with(f"{workflow_name}.zip", f"{workflow_name}.knwf")


def test_save_output_kdl_workflow(my_setup):
    node1 = kdlc.Node(
        node_id="1",
        name="CSV Reader",
        factory="org.knime.base.node.io.csvreader.CSVReaderNodeFactory",
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    node1.port_count = 1
    node1.model = [
        {
            "url": (
                "/Users/jared/knime-workspace/Example Workflows/"
                "TheData/Misc/Demographics.csv"
            )
        },
        {"colDelimiter": ","},
        {"rowDelimiter": "%%00010"},
        {"quote": '"'},
        {"commentStart": "#"},
        {"hasRowHeader": True},
        {"hasColHeader": True},
        {"supportShortLines": False},
        {"limitRowsCount": -1, "data_type": "xlong"},
        {"skipFirstLinesCount": -1},
        {"characterSetName": "", "isnull": True},
        {"limitAnalysisCount": -1},
    ]
    node2 = kdlc.Node(
        node_id="2",
        name="Column Filter",
        factory=(
            "org.knime.base.node.preproc.filter."
            "column.DataColumnSpecFilterNodeFactory"
        ),
        bundle_name="KNIME Base Nodes",
        bundle_symbolic_name="org.knime.base",
        bundle_version="3.7.1.v201901291053",
        feature_name="KNIME Core",
        feature_symbolic_name="org.knime.features.base.feature.group",
        feature_version="3.7.1.v201901291053",
    )
    node2.port_count = 1
    node2.model = [
        {
            "column-filter": [
                {"filter-type": "STANDARD"},
                {
                    "included_names": [
                        {"array-size": 11},
                        {"0": "MaritalStatus"},
                        {"1": "Gender"},
                        {"2": "EstimatedYearlyIncome"},
                        {"3": "SentimentRating"},
                        {"4": "WebActivity"},
                        {"5": "Age"},
                        {"6": "Target"},
                        {"7": "Available401K"},
                        {"8": "CustomerValueSegment"},
                        {"9": "ChurnScore"},
                        {"10": "CallActivity"},
                    ]
                },
                {"excluded_names": [{"array-size": 1}, {"0": "NumberOfContracts"}]},
                {"enforce_option": "EnforceExclusion"},
                {
                    "name_pattern": [
                        {"pattern": ""},
                        {"type": "Wildcard"},
                        {"caseSensitive": True},
                    ]
                },
                {
                    "datatype": [
                        {
                            "typelist": [
                                {"org.knime.core.data.StringValue": False},
                                {"org.knime.core.data.IntValue": False},
                                {"org.knime.core.data.DoubleValue": False},
                                {"org.knime.core.data.BooleanValue": False},
                                {"org.knime.core.data.LongValue": False},
                                {
                                    (
                                        "org.knime.core.data." "date.DateAndTimeValue"
                                    ): False
                                },
                            ]
                        }
                    ]
                },
            ]
        }
    ]
    node3 = kdlc.Node(
        node_id="3",
        name="Table to JSON",
        factory="org.knime.json.node.fromtable.TableToJsonNodeFactory",
        bundle_name="JSON related functionality for KNIME",
        bundle_symbolic_name="org.knime.json",
        bundle_version="3.7.1.v201901281201",
        feature_name="KNIME JSON-Processing",
        feature_symbolic_name="org.knime.features.json.feature.group",
        feature_version="3.7.1.v201901281201",
    )
    node3.port_count = 1
    node3.model = [
        {
            "selectedColumns": [
                {"filter-type": "STANDARD"},
                {
                    "included_names": [
                        {"array-size": 11},
                        {"0": "MaritalStatus"},
                        {"1": "Gender"},
                        {"2": "EstimatedYearlyIncome"},
                        {"3": "SentimentRating"},
                        {"4": "WebActivity"},
                        {"5": "Age"},
                        {"6": "Target"},
                        {"7": "Available401K"},
                        {"8": "CustomerValueSegment"},
                        {"9": "ChurnScore"},
                        {"10": "CallActivity"},
                    ]
                },
                {"excluded_names": [{"array-size": 0}]},
                {"enforce_option": "EnforceExclusion"},
                {
                    "name_pattern": [
                        {"pattern": ""},
                        {"type": "Wildcard"},
                        {"caseSensitive": True},
                    ]
                },
                {
                    "datatype": [
                        {
                            "typelist": [
                                {"org.knime.core.data.StringValue": False},
                                {"org.knime.core.data.IntValue": False},
                                {"org.knime.core.data.DoubleValue": False},
                                {"org.knime.core.data.BooleanValue": False},
                                {"org.knime.core.data.LongValue": False},
                                {
                                    (
                                        "org.knime.core.data" ".date.DateAndTimeValue"
                                    ): False
                                },
                            ]
                        }
                    ]
                },
            ]
        },
        {"rowkey.key": "key"},
        {"direction": "KeepRows"},
        {"column.name.separator": "."},
        {"output.column.name": "JSON"},
        {"row.key.option": "omit"},
        {"column.names.as.path": False},
        {"remove.source.columns": False},
        {"output.boolean.asNumbers": False},
        {"missing.values.are.omitted": True},
    ]
    node_list = [node1, node2, node3]
    connection_list = [
        kdlc.Connection(
            connection_id=0,
            source_id="1",
            source_port="1",
            source_node=node1,
            dest_id="3",
            dest_port="1",
            dest_node=node3,
        ),
        kdlc.Connection(
            connection_id=1,
            source_id="3",
            source_port="1",
            source_node=node3,
            dest_id="2",
            dest_port="1",
            dest_node=node2,
        ),
    ]
    global_variable_list = []
    workflow = kdlc.Workflow(
        connections=connection_list, variables=global_variable_list
    )
    kdlc.save_output_kdl_workflow(f"{test_generated_dir}/out.kdl", workflow, node_list)
    assert filecmp.cmp(f"{test_resources_dir}/in.kdl", f"{test_generated_dir}/out.kdl")


def test_cleanup(my_setup):
    kdlc.cleanup()
    assert os.path.exists(kdlc.TMP_INPUT_DIR.name) is False
    assert os.path.exists(kdlc.TMP_OUTPUT_DIR.name) is False
