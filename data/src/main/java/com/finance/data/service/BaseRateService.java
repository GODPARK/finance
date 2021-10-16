package com.finance.data.service;

import com.finance.data.entity.BaseRate;
import com.finance.data.repository.BaseRateRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Date;
import java.util.Locale;

@Service
public class BaseRateService {

    @Autowired
    private BaseRateRepository baseRateRepository;

    public BaseRate saveBaseRate(BaseRate baseRate) {
        BaseRate newBaseRate = BaseRate.builder()
                .countryCode(baseRate.getCountryCode().toUpperCase(Locale.ROOT))
                .rate(baseRate.getRate())
                .updateDate(new Date())
                .build();
        return baseRateRepository.save(newBaseRate);
    }
}
