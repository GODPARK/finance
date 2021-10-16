package com.finance.data.controller;

import com.finance.data.entity.ExchangeRate;
import com.finance.data.service.ExchangeRateService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.validation.Valid;

@RestController
@RequestMapping(value = "/api/exchange_rate")
public class ExchangeRateController {

    @Autowired
    private ExchangeRateService exchangeRateService;

    @PostMapping(value = "", consumes = "application/json", produces = "application/json")
    public ResponseEntity<ExchangeRate> saveApi (@Valid @RequestBody ExchangeRate exchangeRate) {
        return ResponseEntity.ok().body(exchangeRateService.saveExchangeRate(exchangeRate));
    }
}
