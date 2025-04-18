/**
 * Copyright (c) 2020-2023, RTE (http://www.rte-france.com)
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 * SPDX-License-Identifier: MPL-2.0
 */
package com.powsybl.python.dynamic;

import com.powsybl.commons.report.ReportNode;
import com.powsybl.dynamicsimulation.OutputVariable;
import com.powsybl.dynamicsimulation.OutputVariablesSupplier;
import com.powsybl.dynawo.outputvariables.DynawoOutputVariablesBuilder;
import com.powsybl.iidm.network.Network;

import java.util.*;
import java.util.function.BiConsumer;
import java.util.function.Consumer;

/**
 * @author Nicolas Pierre <nicolas.pierre@artelys.com>
 * @author Laurent Issertial {@literal <laurent.issertial at rte-france.com>}
 */
public class PythonOutputVariablesSupplier implements OutputVariablesSupplier {

    private final List<BiConsumer<Consumer<OutputVariable>, ReportNode>> outputVariablesSupplierList = new ArrayList<>();

    public void addOutputVariables(String elementId, List<String> variables, boolean isDynamic, OutputVariable.OutputType type) {
        outputVariablesSupplierList.add((c, r) -> {
            DynawoOutputVariablesBuilder builder = new DynawoOutputVariablesBuilder(r)
                .variables(variables)
                .outputType(type);
            if (isDynamic) {
                builder.dynamicModelId(elementId);
            } else {
                builder.staticId(elementId);
            }
            builder.add(c);
        });
    }

    @Override
    public List<OutputVariable> get(Network network, ReportNode reportNode) {
        List<OutputVariable> curves = new ArrayList<>();
        ReportNode supplierReportNode = SupplierReport.createSupplierReportNode(reportNode,
                "pypowsyblOutputVariables",
                "PyPowsybl Output Variables Supplier");
        outputVariablesSupplierList.forEach(c -> c.accept(curves::add, supplierReportNode));
        return curves;
    }
}
