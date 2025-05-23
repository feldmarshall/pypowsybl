/**
 * Copyright (c) 2021, RTE (http://www.rte-france.com)
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 * SPDX-License-Identifier: MPL-2.0
 */
package com.powsybl.python.network;

import com.powsybl.iidm.network.IdentifiableType;

/**
 * @author Etienne Lesot {@literal <etienne.lesot at rte-france.com>}
 */
public record NodeContext(int node, String connectableId, IdentifiableType connectableType) {
}
