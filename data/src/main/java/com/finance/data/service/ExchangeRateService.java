package com.finance.data.service;

import com.finance.data.entity.ExchangeRate;
import com.finance.data.repository.ExchangeRateRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Date;
import java.util.Locale;

@Service
public class ExchangeRateService {

    @Autowired
    private ExchangeRateRepository exchangeRateRepository;

    public ExchangeRate saveExchangeRate(ExchangeRate exchangeRate) {
        ExchangeRate newExchangeRate = ExchangeRate.builder()
                .currencyCode(exchangeRate.getCurrencyCode().toUpperCase(Locale.ROOT))
                .currencyPrice(exchangeRate.getCurrencyPrice())
                .standardDate(new Date(exchangeRate.getTimestamp()*1000L))
                .fromData(exchangeRate.getFromData())
                .updateDate(new Date())
                .build();
        return exchangeRateRepository.save(newExchangeRate);
    }
}
