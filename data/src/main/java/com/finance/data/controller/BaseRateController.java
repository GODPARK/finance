package com.finance.data.controller;

import com.finance.data.entity.BaseRate;
import com.finance.data.service.BaseRateService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.validation.Valid;

@RestController
@RequestMapping(value = "/api/base_rate")
public class BaseRateController {

    @Autowired
    private BaseRateService baseRateService;

    @PostMapping(value = "", consumes = "application/json", produces = "application/json")
    public ResponseEntity<BaseRate> saveApi (@Valid @RequestBody BaseRate baseRate) {
        return ResponseEntity.ok().body(baseRateService.saveBaseRate(baseRate));
    }
}
