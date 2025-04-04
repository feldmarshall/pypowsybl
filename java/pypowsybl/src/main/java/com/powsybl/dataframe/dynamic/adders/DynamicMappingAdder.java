/**
* Copyright (c) 2022, RTE (http://www.rte-france.com)
* This Source Code Form is subject to the terms of the Mozilla Public
* License, v. 2.0. If a copy of the MPL was not distributed with this
* file, You can obtain one at http://mozilla.org/MPL/2.0/.
* SPDX-License-Identifier: MPL-2.0
*/
package com.powsybl.dataframe.dynamic.adders;

import com.powsybl.dataframe.SeriesMetadata;
import com.powsybl.dataframe.update.UpdatingDataframe;
import com.powsybl.dynawo.builders.ModelInfo;
import com.powsybl.python.dynamic.PythonDynamicModelsSupplier;

import java.util.Collection;
import java.util.List;

/**
 * @author Nicolas PIERRE {@literal <nicolas.pierre@artelys.com>}
 */
public interface DynamicMappingAdder {

    /**
     * Get the list of metadata: one list of columns metadata for each input dataframe.
     */
    List<List<SeriesMetadata>> getMetadata();

    /**
     * Adds elements to the dynamic model mapping, based on a list of dataframes.
     * The first dataframe is considered the "primary" dataframe, other dataframes
     * can provide additional data (e.g. list of transformers id for a Tap Changer Blocking Automation System).
     */
    void addElements(PythonDynamicModelsSupplier modelMapping, List<UpdatingDataframe> dataframe);

    /**
     * Returns supported model names for the given adder
     */
    Collection<ModelInfo> getSupportedModels();
}
