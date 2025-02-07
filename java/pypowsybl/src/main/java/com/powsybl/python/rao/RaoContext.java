/**
 * Copyright (c) 2024, RTE (http://www.rte-france.com)
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 * SPDX-License-Identifier: MPL-2.0
 */
package com.powsybl.python.rao;

import com.powsybl.commons.PowsyblException;
import com.powsybl.glsk.api.GlskDocument;
import com.powsybl.iidm.network.Network;
import com.powsybl.loadflow.LoadFlowParameters;
import com.powsybl.openrao.data.crac.api.Crac;
import com.powsybl.openrao.data.raoresult.api.RaoResult;
import com.powsybl.openrao.monitoring.Monitoring;
import com.powsybl.openrao.monitoring.MonitoringInput;
import com.powsybl.openrao.monitoring.results.MonitoringResult;
import com.powsybl.openrao.monitoring.results.RaoResultWithAngleMonitoring;
import com.powsybl.openrao.monitoring.results.RaoResultWithVoltageMonitoring;
import com.powsybl.openrao.raoapi.Rao;
import com.powsybl.openrao.raoapi.RaoInput;
import com.powsybl.openrao.raoapi.parameters.RaoParameters;

/**
 * @author Bertrand Rix {@literal <bertrand.rix at artelys.com>}
 */
public class RaoContext {

    public RaoContext() {
    }

    private RaoResult results;

    private Crac crac;

    private GlskDocument glsks;

    public void setCrac(Crac crac) {
        this.crac = crac;
    }

    public void setGlsks(GlskDocument gklss) {
        this.glsks = glsks;
    }

    public void run(Network network, RaoParameters parameters) {
        if (crac == null) {
            throw new PowsyblException("Providing a crac source is mandatory to run a Rao.");
        }
        RaoInput.RaoInputBuilder inputBuilder = RaoInput.build(network, crac);
        if (glsks != null) {
            inputBuilder.withGlskProvider(glsks.getZonalGlsks(network));
        }
        results = Rao.run(inputBuilder.build(), parameters);
    }

    public void runVoltageMonitoring(Network network, String provider, LoadFlowParameters parameters) {
        Monitoring raoMonitoring = new Monitoring(provider, parameters);
        MonitoringInput inputs = MonitoringInput.buildWithVoltage(network, crac, results).build();
        MonitoringResult monitoringResult = raoMonitoring.runMonitoring(inputs, 1);
        results = new RaoResultWithVoltageMonitoring(results, monitoringResult);
    }

    public void runAngleMonitoring(Network network, String provider, LoadFlowParameters parameters) {
        Monitoring raoMonitoring = new Monitoring(provider, parameters);
        MonitoringInput inputs = MonitoringInput.buildWithAngle(network, crac, results, glsks.getZonalScalable(network)).build();
        MonitoringResult monitoringResult = raoMonitoring.runMonitoring(inputs, 1);
        results = new RaoResultWithAngleMonitoring(results, monitoringResult);
    }

    public RaoResult getResults() {
        return results;
    }

    public Crac getCrac() {
        return crac;
    }

    public GlskDocument getGlsks() {
        return glsks;
    }
}
